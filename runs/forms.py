from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from runs.models import Game, Developer

class GameRegistrationForm(ModelForm):
    '''
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(GameRegistrationForm, self).__init__(*args, **kwargs)
    '''
    
    class Meta:
        model = Game
        exclude = ('added_date', 'run', 'leader', 'likes')
        
        
class GameDevForm(ModelForm):
    
    class Meta:
        model = Developer
        exclude = ('game')
