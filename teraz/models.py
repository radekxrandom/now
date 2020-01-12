from django.db import models
import os
# Create your models here.


class GetPies(models.Model):
    u_name = models.CharField(max_length=20,null=True,blank=True)
    u_mail = models.CharField(max_length=20,null=True,blank=True)
    u_reason = models.CharField(max_length=20,null=True,blank=True)

class Info(models.Model):
    get = models.CharField(null=True,blank=True,max_length=30)