from django.db import models
from django.contrib.auth.models import User
from members.models import Team
from gallery.models import GamePic

class Run(models.Model):
    year = models.CharField(max_length = 4)
    start_date = models.DateTimeField()
    current_run = models.BooleanField()
    submission_open = models.BooleanField()
    
    def __unicode__(self):
        return self.year
        
        
    def open_submission(self):
        self.submission_open = True



class Game(models.Model):
    name = models.CharField(max_length = 50)
    added_date = models.DateTimeField('date added')
    description = models.TextField(null=True, blank=True)
    short_desc = models.TextField(null=True, blank=True, max_length=170)
    team = models.CharField(max_length = 50, null=True, blank=True)
    leader = models.ForeignKey(User)
    run = models.ForeignKey(Run)
    likes = models.IntegerField(default=0)
    concept_only = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.name
        
    def get_devs(self):
        return Developer.objects.filter(game=self)
        
    def get_screens(self):
        return GamePic.objects.filter(game=self, game_icon=False)
        
    def get_icon(self):
        return GamePic.objects.get(game=self, game_icon=True)
    
    def get_screen_height(self):
        sc = GamePic.objects.filter(game=self, game_icon=False).count();
        r = 1
        c = 0
        if sc > 8:
            r+=1
            for i in range(sc-8):
                c += 1
                if c== 8:
                    r += 1
                    c = 0
        return r*80+(r-1)*10

class Developer(models.Model):
    user = models.ForeignKey(User)
    role = models.CharField(max_length = 300)
    game = models.ForeignKey(Game)
    
    def __unicode__(self):
        return self.user.username
        
        
class Upload(models.Model):
    """
    Model for uploads, allowed formats are in Settings.
    """
    title = models.CharField(max_length = 100)
    version = models.CharField(max_length = 10,null=True, blank=True)
    game = models.ForeignKey(Game)
    uploaded_file = models.FileField(upload_to=('submissions/'+game.name))
    
