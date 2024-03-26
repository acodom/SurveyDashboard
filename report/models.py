from django.db import models

# Create your models here.
# report/models.py
class DataPoint(models.Model):
    timestamp = models.DateTimeField()
    value = models.FloatField()
