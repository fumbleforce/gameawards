from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField('date created')
    devs = models.ManyToManyField(User)
    icon = models.ImageField(upload_to='images/teams', null=True, blank=True)
    
    def __unicode__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User)
    about = models.TextField()
    portrait = models.ImageField(upload_to='images/members', null=True, blank=True)
    
    def __unicode__(self):
        return self.user.username
        
    class Meta:
        app_label = 'members'



def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)


        
