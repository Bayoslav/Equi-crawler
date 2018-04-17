import json,time,django
from treciproj import settings
import os
import ast,datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "treciproj.settings")
django.setup()
from RaceApp.models import Country
import requests
o = Country.objects.get(id=4)

#jsonic = f.read()
#dicti = ast.literal_eval(jsonic)
#dictionary = ast.literal_eval(o.dicts)
datic = datetime.date.today()
d = str(datic)
filename = 'JP' + d + '.json'
path = "JPFiles"
fullpath = os.path.join(path, filename)
f=open(fullpath,'w')

jsonic = json.dumps(o.dicts)
#jsonero = json.dumps(events)
f.write(jsonic)
f.close()


#print(jsonero)
headers = {'content-type' : 'application/json','Accept':'application/json', 'user-agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
#r = requests.post('https://konji-187909.appspot.com/api/regions/america',json=jsonero,timeout=1200)

#print(r.text)
print("\n\n KEK \n\n")
