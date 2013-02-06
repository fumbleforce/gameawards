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
    
    def __unicode__(self):
        return self.name
    
    def get_icon(self):
        return GamePic.objects.filter(game=self, game_icon=True)
        
    def get_devs(self):
        return Developer.objects.filter(game=self)
        
    def get_screens(self):
        return GamePic.objects.filter(game=self, game_icon=False)

        
class Developer(models.Model):
    user = models.ForeignKey(User)
    role = models.CharField(max_length = 300)
    game = models.ForeignKey(Game)
    
    def __unicode__(self):
        return self.user.username
        
    
