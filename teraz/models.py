from django.db import models
import os
# Create your models here.

class Info(models.Model):
    get = models.CharField(null=True,blank=True,max_length=30)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=30)
    reason = models.CharField(max_length=30)

