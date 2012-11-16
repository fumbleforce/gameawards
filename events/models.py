from django.db import models

class Event(models.Model):
    name = models.CharField(max_length = 200)
    date_created = models.DateTimeField()
    date_happens = models.DateTimeField()
    date_opens = models.DateTimeField()
    date_closes = models.DateTimeField()
    max_participants = models.IntegerField()
    location = models.CharField(max_length = 300)
    info = models.TextField(null=True, blank=True)
    key = models.CharField(max_length = 100)
    
    def __unicode__(self):
        return self.name
        
    def embed(self):
        return '<iframe src="https://docs.google.com/spreadsheet/embeddedform?formkey='+self.key+'" width="760" height="390" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>"'
    

