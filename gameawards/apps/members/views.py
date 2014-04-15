from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from members.models import UserProfile
from members.forms import LoginForm, UserRegistrationForm, UserEditForm, ForgotUsernameForm, ResetPasswordForm
import ayah
from runs.models import Game, Upload, Run
from django.core.mail import send_mail
import random
import string

def pass_gen(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


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
        reg = Run.objects.get(current_run=True).submission_open
        uploads = Upload.objects.filter(game__leader=user)
        context = {'user':user, 'games':games,'profile':profile, 'uploads':uploads, 'registration':reg}
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
    
    


def sent_email_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members/profile/')
    
    userform = ResetPasswordForm()
    emailform = ForgotUsernameForm(request.POST)
    
    user = User.objects.get(email=request.POST['email'])
    if user:
        newpass = pass_gen()
        user.set_password(newpass)
        user.save()
        status = "Mail containing username and new password sent."
        send_mail('Password Reset', 'Here is your new login information. You can change your password on your profile page once logged in. Username: '+ user.username + " Password: "+ str(newpass), 'no-reply@gameawards.no',
    [user.email], fail_silently=False)
        
    else:
        status = "Could not find a user with that email address."
        
    return render_to_response(
        'members/resetpassword.html', 
        {'status':status, 'userform':userform, 'emailform':emailform}, 
        context_instance=RequestContext(request))



def sent_user_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members/profile/')

    userform = ResetPasswordForm(request.POST)
    emailform = ForgotUsernameForm()
    
    try:
        user = User.objects.get(username=request.POST['username'])

        if user:
            newpass = pass_gen()
            user.set_password(newpass)
            user.save()
            status = "Mail containing username and new password sent."
            send_mail('Password Reset', 'Here is your new login information. You can change your password on your profile page once logged in. Username: '+ user.username + " Password: "+ str(newpass), 'no-reply@gameawards.no',[user.email], fail_silently=False)
    
    except User.DoesNotExist:
        status = "Could not find a user with that username."
        
    return render_to_response(
        'members/resetpassword.html', 
        {'status':status, 'userform':userform, 'emailform':emailform}, 
        context_instance=RequestContext(request))
    
    



def reset_password_request(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/members/profile/')
        
    userform = ResetPasswordForm()
    emailform = ForgotUsernameForm()
    status = "Fill in either the username field or the email field and press submit"
           
    return render_to_response(
        'members/resetpassword.html', 
        {'status':status, 'userform':userform, 'emailform':emailform}, 
        context_instance=RequestContext(request))
    
    
    
    
    
    
def edit_member_request(request):
    
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/members/login/')
        
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = request.user
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data["password"])
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
        ab = request.user.get_profile().about
        form = UserEditForm(instance=request.user, initial={'about':ab})
        context = {'form':form}
        
    return render_to_response(
        'members/edit_member.html', 
        context, 
        context_instance=RequestContext(request))
           

