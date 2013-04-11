from django.db import models
from django.utils import timezone

class Newspost(models.Model):
    title = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(default=timezone.now())
    
    def __unicode__(self):
        return self.title
        

