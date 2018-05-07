import requests,uuid
import time as tim
import bs4 as bs
import django,os 
from treciproj import settings
import os,ast
import datetime 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country, Podesavanja
import json
global fontic

o = Country.objects.get(id=4)

o.date = {20180414,20180422,20180421,20180415,20180408,20180407,20180401}
o.save()

