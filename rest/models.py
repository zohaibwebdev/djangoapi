from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField(max_length=50)
    city = models.CharField(max_length=100)