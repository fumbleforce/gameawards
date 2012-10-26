from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Run(models.Model):
    year = models.IntegerField(max_length = 4)
    start_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.year
    
    
        

class Developer(models.Model):
    user = models.ForeignKey(User)
    role = models.CharField(max_length = 300)
    
    def __unicode__(self):
        return user.username
        
        
        
        
class Team(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField('date created')
    devs = models.ManyToManyField(Developer)
    icon = models.ImageField(upload_to='pics/teams', null=True, blank=True)
    
    def __unicode__(self):
        return self.name


 
class Game(models.Model):
    name = models.CharField(max_length = 200)
    added_date = models.DateTimeField('date added')
    description = models.TextField()
    icon = models.ImageField(upload_to='pics/games', null=True, blank=True)
    team = models.ForeignKey(Team)
    leader = models.ForeignKey(Developer)
    run = models.ForeignKey(Run)
    
    def __unicode__(self):
        return self.title


class UserProfile(models.Model):

    user = models.OneToOneField(User)
    about = models.TextField()
    portrait = models.ImageField(upload_to='pics/members', null=True, blank=True)
    
    def __unicode__(self):
        return self.user.username
        
        
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
        

        

        

        
    
