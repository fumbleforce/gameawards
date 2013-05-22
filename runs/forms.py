from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from runs.models import Game, Developer, Upload
from django.conf import settings

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
        

class UploadForm(ModelForm):

    class Meta:
        model = Upload
        
    def clean_uploaded_file(self):
        f = self.cleaned_data['uploaded_file']
        
        try:
            if f:
                file_type = f.content_type.split('/')[0]
                if len(f.name.split('.')) == 1:
                    raise forms.ValidationError(_('Only pdf files, or zip/rar archives are allowed'))
                
                if file_type in settings.ACCEPTED_UPLOAD_FILETYPES:
                    if f._size > settings.MAX_UPLOAD_SIZE:
                        raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s. Consider splitting archive into smaller parts.') % (filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(f._size)))
                else:
                    raise forms.ValidationError(_('Only pdf files, or zip/rar archives are allowed'))
        except:
            pass

        return f
    
