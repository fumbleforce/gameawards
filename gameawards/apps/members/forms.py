from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from members.models import UserProfile

class UserRegistrationForm(ModelForm):
    username = forms.CharField(label=('User Name'))
    email = forms.EmailField(label=('Email Address'))
    password = forms.CharField(label=('Password'), widget = forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=('Verify Password'), widget = forms.PasswordInput(render_value=False))
    first_name = forms.CharField(label=('First Name'))
    last_name = forms.CharField(label=('Last Name'))
    
    class Meta:
        model = UserProfile
        exclude = ('user', 'portrait')
        
        
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError('Username is taken.')
        
        
    def clean(self):
        password = self.cleaned_data.get('password', None)
        password1 = self.cleaned_data.get('password1', None)
        
        if password and password1 and password != password1:
            raise forms.ValidationError('Passwords did not match.')
            
        return self.cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(label=(u'User name'))
    password = forms.CharField(label=(u'Password'), widget = forms.PasswordInput(render_value=False))
    
    
class UserEditForm(ModelForm):
    email = forms.EmailField(label=('Email Address'))
    password = forms.CharField(label=('Password'), widget = forms.PasswordInput(render_value=False))
    password1 = forms.CharField(label=('Verify Password'), widget = forms.PasswordInput(render_value=False))
    first_name = forms.CharField(label=('First Name'))
    last_name = forms.CharField(label=('Last Name'))

    class Meta:
        model = UserProfile
        exclude = ('user', 'portrait')
    
    
    
class ResetPasswordForm(forms.Form):
    username = forms.CharField(label=(u'User name'))
    
class ForgotUsernameForm(forms.Form):
    email = forms.EmailField(label=('Email Address'))
