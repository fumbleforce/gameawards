from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from gallery.models import GamePic

class GamePicForm(ModelForm):
    
    class Meta:
        model = GamePic
        exclude = ('added_date', 'owner', 'game')
