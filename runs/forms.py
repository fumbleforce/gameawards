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
    user = forms.CharField(label=(u'User name'))
    
    class Meta:
        model = Developer
        exclude = ('game', 'user')
    
    
    def clean(self):
        username = self.cleaned_data['user']
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('This is not a registered User.')
        return self.cleaned_data
    
