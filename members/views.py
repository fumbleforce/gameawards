from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from members.models import UserProfile
from members.forms import LoginForm, UserRegistrationForm, UserEditForm
import ayah
from runs.models import Game


def member_registration(request):
    '''
    This view controls User registration. 
    '''
    
    ayah_html = ayah.get_publisher_html()
    
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members/profile/')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            secret = request.POST['session_secret']
            passed = ayah.score_result(secret)
            if passed:
                user = User.objects.create_user(
                    username=form.cleaned_data['username'], 
                    email = form.cleaned_data['email'], 
                    password = form.cleaned_data['password'],
                )
                user.first_name = form.cleaned_data['first_name']
                user.last_name = form.cleaned_data['last_name']
                user.save()
                
                profile = user.get_profile()
                profile.about = form.cleaned_data['about']
                profile.save()
                member = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
                login(request, member)
                return HttpResponseRedirect('/members/profile/')
            else:
                context = {'form':form, 'ayah_html':ayah_html}
        else:
            context = {'form':form, 'ayah_html':ayah_html}
    else:
        form = UserRegistrationForm()
        context = {'form':form, 'ayah_html':ayah_html}
        
    return render_to_response(
        'members/register_member.html', 
        context, 
        context_instance=RequestContext(request))
        
    
def profile_request(request):
    if request.user.is_authenticated():
        user = request.user
        profile = user.get_profile()
        games = Game.objects.filter(leader=user)
        context = {'user':user, 'games':games,'profile':profile}
        return render_to_response(
            'members/profile.html', 
            context, 
            context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/members/login/')


def login_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            member = authenticate(username=username, password=password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/members/profile/')
            else:
                context = {'form':form}
        else:
            context = {'form':form}
    else:
        form = LoginForm()
        context = {'form':form}
        
    return render_to_response(
        'members/login.html', 
        context, 
        context_instance=RequestContext(request))
        
        
def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')
    
    
def reset_password_request(request):
    return render_to_response(
        'members/resetpassword.html', 
        {}, 
        context_instance=RequestContext(request))
    
    
def edit_member_request(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/members/login/')
        
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data['email']
            user.set_password(self.cleaned_data["password"])
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            
            profile = user.get_profile()
            profile.about = form.cleaned_data['about']
            profile.save()

            return HttpResponseRedirect('/members/profile/')
        else:
            context = {'form':form}
    else:
        form = UserEditForm(instance=request.user)
        context = {'form':form}
        
    return render_to_response(
        'members/edit_member.html', 
        context, 
        context_instance=RequestContext(request))
           

