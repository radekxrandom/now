from django.db import models
import os
# Create your models here.


class GetPies(models.Model):
    u_name = models.CharField(max_length=20,null=True,blank=True)
    u_mail = models.CharField(max_length=20,null=True,blank=True)
    u_reason = models.CharField(max_length=20,null=True,blank=True)

class Info(models.Model):
    get = models.CharField(null=True,blank=True,max_length=30)

class MainCMS(models.Model):
    line_eng = models.CharField(max_length=150,null=True,blank=True)
    line_pl = models.CharField(max_length=150,null=True,blank=True)

class PrzedCMS(models.Model):
    line_eng = models.CharField(max_length=150,null=True,blank=True)
    line_pl = models.CharField(max_length=150,null=True,blank=True)

class PoCMS(models.Model):
    line_eng = models.CharField(max_length=150,null=True,blank=True)
    line_pl = models.CharField(max_length=150,null=True,blank=True)

class GetInfoCMS(models.Model):
    line_eng = models.CharField(max_length=150,null=True,blank=True)
    line_pl = models.CharField(max_length=150,null=True,blank=True)
