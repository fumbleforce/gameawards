from django.db import models
from django.contrib.auth.models import User
from members.models import Team


class Run(models.Model):
    year = models.CharField(max_length = 4)
    start_date = models.DateTimeField()
    current_run = models.BooleanField()
    
    def __unicode__(self):
        return self.year



class Game(models.Model):
    name = models.CharField(max_length = 200)
    added_date = models.DateTimeField('date added')
    description = models.TextField()
    icon = models.ImageField(upload_to='images/games', null=True, blank=True)
    team = models.ForeignKey(Team)
    leader = models.ForeignKey(User)
    run = models.ForeignKey(Run)
    
    def __unicode__(self):
        return self.name

        
class Developer(models.Model):
    user = models.ForeignKey(User)
    role = models.CharField(max_length = 300)
    game = models.ForeignKey(Game)
    
    def __unicode__(self):
        return self.user.username
        
    
