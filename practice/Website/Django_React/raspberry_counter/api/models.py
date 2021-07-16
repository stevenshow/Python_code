from django.db import models

# Create your models here.

class Dates(models.Model):
    # Special event
    event_Name = models.CharField(max_length=50, unique=True)
    event_Date = models.CharField(max_length=50, unique=True)
    