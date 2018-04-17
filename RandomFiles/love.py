import requests
global date
import bs4 as bs 
import datetime
import pytz
#import os
import uuid
import json,time,django
from treciproj import settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country,Podesavanja

o = Podesavanja('1',0)
o.save()