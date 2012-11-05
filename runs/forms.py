from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from members.models import UserProfile, Team

class GameRegistrationForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(GameRegistrationForm, self).__init__(*args, **kwargs)
    
    
    name = forms.CharField(label=('Name'))
    description = forms.TextField(label=('First Name'))
    CHOICES = Team.objects.filter(devs__contains=user)
    team = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    icon = forms.ImageField(upload_to="images/games")
    
    

