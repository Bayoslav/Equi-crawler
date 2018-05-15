from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from datetime import datetime


# Create your models here.
    

class Podesavanja(models.Model):
    is_scraping = models.BooleanField(default=False)

#
class Country(models.Model):
    name = models.CharField(max_length=500)
    dicts = models.TextField(max_length=500000)
    date = models.CharField(max_length=500)


class Form_names(models.Model):
    eng_name = models.CharField(max_length=500)
    form_name = models.CharField(max_length=500)
    sire = models.CharField(max_length=500)
    dam = models.CharField(max_length=500)
    country = models.CharField(max_length=500)
    age = models.IntegerField()
    