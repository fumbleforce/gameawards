from django.db import models

class Run(models.Model):
    year = models.IntegerField(max_length = 4)
    start_date = models.DateTimeField()
    
    def __unicode__(self):
        return 'Run ' + str(self.year)
    
    
class Game(models.Model):
    name = models.CharField(max_length = 200)
    added_date = models.DateTimeField('date added')
    description = models.TextField()
    icon_url = models.UrlField()
    team = models.ForeignKey(Team)
    leader = models.ForeignKey(Member)
    
    def __unicode(self):
        return self.title
   
    
class Team(models.Model):
    name = models.CharField(max_length = 200)
    created_date = models.DateTimeField('date created')
    members = models.ManyToManyField(Developer)
    
    def __unicode(self):
        return self.name
        
        
class Member(models.Model):
    name = models.CharField(max_length = 200)
    joined_date = models.DateTimeField('date joined')
    about = models.TextField()
    portrait = models.UrlField()
    
    def __unicode(self):
        return self.name
        
        
class Developer(models.Model):
    member = models.ForeignKey(Member)
    game = models.ForeignKey(Game)
    role = models.CharField(max_Length = 300)
    
    def __unicode(self):
        return self.member.name
