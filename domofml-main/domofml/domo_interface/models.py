from django.db import models


# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=80)
    type = models.CharField(max_length=80)
