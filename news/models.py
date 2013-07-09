from django.db import models
from django.utils import timezone

class Newspost(models.Model):
    title = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published',default=timezone.now())
    content = models.TextField(blank=True, null=True)
    
    def __unicode__(self):
        return self.title
        

