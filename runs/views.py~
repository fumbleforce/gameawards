from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.template import RequestContext
from runs.forms import RegistrationForm, LoginForm
from runs.models import UserProfile
from django.contrib.auth import authenticate, login, logout


def member_registration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
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
            profile.portrait = form.cleaned_data['portrait']
            profile.save()

            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('runs/register.html', {'form':form}, context_instance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = {'form':form}
        return render_to_response('runs/register.html', context, context_instance=RequestContext(request))
        
        
def login_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            member = authenticate(username=username, password=password)
            if member is not None:
                login(request, member)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('runs/login.html', {'form':form}, context_instance=RequestContext(request))
        else:
            return render_to_response('runs/login.html', {'form':form}, context_instance=RequestContext(request))
    else:
        form = LoginForm()
        context = {'form':form}
        return render_to_response('runs/login.html', context, context_instance=RequestContext(request))
        
        
def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/')
    
    
    
def profile_request(request):
    if request.user.is_authenticated():
        user = request.user
        context = {'user':user}
        return render_to_response('runs/profile.html', context)
    else:
        return HttpResponseRedirect('/login/')
    
    
    
    
