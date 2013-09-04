from django.db import models

# Create your models here.

class Record(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    work_phone = models.CharField(max_length=20)
    home_phone = models.CharField(max_length=20)
    notes = models.CharField(max_length=2000)
    dob = models.DateTimeField('date of birth')

