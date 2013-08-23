from django.db import models

class Thing(models.Model):  
    title = models.CharField(max_length=255)
    description = models.TextField()
    quantity = models.IntegerField()
    creation_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
        
    class Meta:
        ordering = ['title']
