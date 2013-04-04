from django.db import models


class Newspost(models.Model):
    title = models.CharField(max_length = 300)
    pub_date = models.DateTimeField('date published')
    content = models.TextField(default=datetime.now)
    
    def __unicode__(self):
        return self.title
        

