from django.db import models

class General(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
        
class Slide(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    
    def __unicode__(self):
        return self.title
