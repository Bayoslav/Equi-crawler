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
from RaceApp.models import Country
global headers
def get_races(eventlist):
    for race in eventlist:
        url = race['url']
        try:
            r = requests.get(url)
        except:
            time.sleep(3)
            r = requests.get(url)
        racelist = []
        soup = bs.BeautifulSoup(r.text,'lxml')
        for tr in soup.find_all('table'):
            tds = tr.find_all('td')
            length = len(tds)
            for i in range(0,length,8):
                #print(tds[i])
                #print(tds)
                x = tds[2+i].text.strip(' \t\n\r')
            # print("X = " + x)
                #print(dir(x))
            # x = str(x)
                #print(type(x))
                x = x.replace(" ", "")
                url = tds[0+i].find('a')
                #print(url)
                url = 'http://www.equibase.com' + url.get('href')
                tabledic = {
                    'Race: ' : tds[0+i].text,
                    'URL' : url,
                    'Purse' : tds[1+i].text,
                    'Race Type' : x,
                    'Distance' : tds[3+i].text,
                    'Surface' : tds[4+i].text,
                    'Starters' : tds[5+i].text,
                    'Est. Post' : tds[6+i].text,
                    'Horses' : [],
                }
                #print(type(tabledic))
                racelist.append(tabledic)
        race['races'] = get_horses(racelist)
    jsonero = json.dumps(eventlist)
    jsonic = json.loads(jsonero)
    print("DATE:", date) #datum
    o = Country('1','America',jsonero,date) #datum
    o.save()
    datic = datetime.date.today()
    d = str(datic)
    filename = 'USA' + d + '.json'
    path = "USFiles"
    fullpath = os.path.join(path, filename)
    f = open(fullpath,'w')
    f.write(jsonero)
    f.close()

def get_horses(racelist):
    proxies = {
    'http' : 'http://35.190.142.78:8888',
    'https' : 'https://35.190.142.78:8888',
    }
    headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}
    for race in racelist:
            ##proxies = get_proxy()
            horselist = []
            #http://www.equibase.com/static/entry/
            url = race['URL']
            try:
                reqhor = requests.get(url)
            except:
                time.sleep(6)
                reqhor = requests.get(url)
            supa = bs.BeautifulSoup(reqhor.text, 'lxml')
            for tr in supa.find_all('tr'):
                tds = tr.find_all('td')
            #print(type(tds))
                if(len(tds)==12 or len(tds)==11):
                    #print(tds)
                    horsename = tds[2].text.strip(' \t\n\r').strip()[:-4].replace(" ", "%20")
                    #print(horsename)
                    print("itsthis")
                    horseurl = 'http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + horsename + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'
                    print(horseurl)
                    print('kauboj')
                    try:
                        horsereq = requests.get(horseurl,headers=headers,timeout=9,proxies=proxies)
                    except: 
                        print("182 L")
                        time.sleep(2)
                        horsereq = requests.get(horseurl,headers=headers,timeout=9,proxies=proxies)
                    soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                    h4 = soup.find('h4')
                    print(h4)
                    if(str(h4)=='<h4><strong>No Matches Found</strong></h4>'):
                        print("Horse doesn't exist in DB")
                        inftab = 'n/a'
                        inftab = [
                                {
                                    "sire": "",
                                    "name": "",
                                    "foals": "",
                                    "starters": "",
                                    "winners": "",
                                    "BW (%)": "",
                                    "earnings": "",
                                    "ael": ""
                                },
                                {
                                    "sire": "",
                                    "name": "",
                                    "mares": "",
                                    "foals": "",
                                    "starters": "",
                                    "winners": "",
                                    "BW (%)": "",
                                    "earnings": "",
                                    "ael": ""
                                },
                                {
                                    "sire": "",
                                    "mares": "",
                                    "foals": "",
                                    "starters": "",
                                    "winners": "",
                                    "BW (%)": "",
                                    "earnings": "",
                                    "ael": ""
                                }
                            ]
                    else:
                        try:
                            horsrl = soup.find('a').get('href')
                        except:
                            print("Captcha error")
                            try:
                                ime = horsereq.history[0].headers['x-cache-proxyname']
                            except:
                                print("ime error")
                                time.sleep(3)
                            else:
                                payld = {
                                'name' : ime,
                                }
                                print(ime)
                                headers={'Authorization' : 'd2VhcmVzZWN1cmU='}
                                ipic = proxies.get('http')
                                ipic = ipic[0:-1] + '9'
                                print(ipic)
                                stop = requests.post(ipic + '/instances/stop', json=payld,headers=headers)
                            print("success")
                        while(1):
                            #try:
                            ##proxies = get_proxy()
                            headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                            'x-requested-with': 'XMLHttpRequest'}
                            horsereq = requests.get(horseurl,headers=headers,timeout=9,proxies=proxies)
                            soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                            horsrl = soup.find('a').get('href')
                        #except:
                            print("Error at 195 line.")
                            try:
                                ime = horsereq.history[0].headers['x-cache-proxyname']
                            except:
                                time.sleep(3)
                            else:
                                payld = {
                                'name' : ime,
                                }
                                print(ime)
                                headers={'Authorization' : 'd2VhcmVzZWN1cmU='}
                                ipic = proxies.get('http')
                                ipic = ipic[0:-1] + '9'
                                print(ipic)
                                stop = requests.post(ipic + '/instances/stop', json=payld,headers=headers)
                                #continue
                        #else:
                            break
                        url = 'http://www.equineline.com/' + horsrl
                        start = url.find('reference_number=')
                        end = url.find('&registry')
                        refnum = url[start+17:end]
                        print(refnum)
                        link = 'http://www.equineline.com/Free5XPedigreeNickingDisplay.cfm?page_state=DISPLAY_REPORT&reference_number=' + refnum
                        while(1):
                            
                            ##proxies = get_proxy()
                            maker = requests.get(link,headers=headers,timeout=9,proxies=proxies)
                            supica = bs.BeautifulSoup(maker.text,'lxml')
                            try:
                                table = supica.find('table')
                            except:
                                table = None 
                            else:
                                if(table is None):
                                    ##proxies = get_proxy()
                                    #soup = bs.BeautifulSoup(r.text,'lxml')
                                    try:
                                        a = supica.find('a').get('href')
                                    except:
                                        a=''
                                    if(a=='mailto:help@equineline.com'):
                                        print("NO horse")
                                        table='Notable'
                                    else:
                                        print("stvorena")
                                        maker = requests.get(link,headers=headers,timeout=9,proxies=proxies)
                                        supica = bs.BeautifulSoup(maker.text,'lxml')
                                        table = supica.find('table')
                                        break
                        if(table=='Notable'):
                            inftab = [
                            {
                                "sire": "",
                                "name": "",
                                "foals": "",
                                "starters": "",
                                "winners": "",
                                "BW (%)": "",
                                "earnings": "",
                                "ael": ""
                            },
                            {
                                "sire": "",
                                "name": "",
                                "mares": "",
                                "foals": "",
                                "starters": "",
                                "winners": "",
                                "BW (%)": "",
                                "earnings": "",
                                "ael": ""
                            },
                            {
                                "sire": "",
                                "mares": "",
                                "foals": "",
                                "starters": "",
                                "winners": "",
                                "BW (%)": "",
                                "earnings": "",
                                "ael": ""
                            }
                        ]
                        else:
                            inftab = get_table(table)
                    ud = str(uuid.uuid4())
                    if(len(tds)==12): 
                        horsedict = {
                            'P#' : tds[0].text.strip(' \t\n\r').replace(" ", ""),
                            'PP' : tds[1].text,
                            'Name' : tds[2].text.strip(' \t\n\r').strip()[:-5],
                            'Claim' : tds[6].text,
                            'Jockey': tds[7].text,
                            'Wgt' : tds[8].text,
                            'Trainer' : tds[9].text,
                            'M/L' : tds[10].text,
                            'Info' : inftab,
                            'uuid' : ud,
                        }
                    else:
                        horsedict = {
                            'P#' : tds[0].text.strip(' \t\n\r').replace(" ", ""),
                            'PP' : tds[1].text,
                            'Name' : tds[2].text.strip(' \t\n\r').strip()[:-5],
                            'Claim' : 'No claim',
                            'Jockey': tds[6].text,
                            'Wgt' : tds[7].text,
                            'Trainer' : tds[8].text,
                            'M/L' : tds[9].text,
                            'Info' : inftab,
                            'uuid' : ud,
                        }
                    horselist.append(horsedict)
            race['Horses'] = horselist
            print("list: ", horselist)
    return racelist
                        
                            
                    #print(url)
                    #print(link)

                        




def get_events():
    global date
    while(1):
        try:
            r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
        except:
            time.sleep(3)
            #r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
        else:
            break
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            date = tds[1].find('a').text
        except:
            print("No event today at " + name)
        else:
            print(url)
            #url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            events = {
                'date' : date,
                'name' : name,
                'url' : url,
            }
            eventlist.append(events)
    print(eventlist)
    get_races(eventlist)
while(1):
    #r = requests.get('https://www.equibase.com/static/entry/index.html')
    #soup = bs.BeautifulSoup(r.text,'lxml')
    aa = Country.objects.get(id=1)
    dated = aa.date
    proxies = {
    'http' : 'http://35.190.142.78:8888',
    'https' : 'https://35.190.142.78:8888',
    }
    try:
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN',proxies=proxies)
    except:
        time.sleep(6)
        r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN',proxies=proxies)
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            baba = tds[1].find('a').text
        except:
            print("No event today at ")
        else:
            break
    if(dated==baba): 
        print("No new races for date ", dated) #proverava ako je dd jednak dd u u bazi ako jeste spava, ako nije zove event
        print("\nSleeping for 20 minutes")
        time.sleep(1200)
        continue 
    else:
        print("New race! Scraping.")
        get_events()
def get_table(table):
    #soup = bs.BeautifulSoup(table,'lxml')
    i=0
    print("Table TEST")
    dictlist = []
    for tr in table.find_all('tr'):
            
            i+=1
            tds = tr.find_all('td')
            if(i==1):
                sire = (tds[0].text)
            if(i==3):
                dict = {
            'sire' : sire,
            'name' : tds[0].text,
            'foals' : tds[2].text,
            'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
            'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
            'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
            'earnings' : tds[6].text.replace("$", "").replace(",",""),
            'ael' : tds[7].text,
                }
            # print(dict)
                dictlist.append(dict)
            if(i==5):
                sire = (tds[0].text)
            if(i==7):
                dict = {
                'sire' : sire,
                'name' : tds[0].text,
                'mares' : tds[1].text,
                'foals' : tds[2].text,
                'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
                'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
                'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
                'earnings' : tds[6].text.replace("$", "").replace(",",""),
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
            if(i==9):
                sire = (tds[0].text)
            if(i==11):
                dict = {
                'sire' : sire,
                'mares' : tds[1].text,
                'foals' : tds[2].text,
                'starters' : tds[3].text.replace(" ", "").replace("(", ",").replace(")",""),
                'winners' :  tds[4].text.replace(" ", "").replace("(", ",").replace(")",""),
                'BW (%)' : tds[5].text.replace(" ", "").replace("(", ",").replace(")",""),
                'earnings' : tds[6].text.replace("$", "").replace(",",""),
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
    return(dictlist)
def get_events():
    global date
    while(1):
        try:
            r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
        except:
            time.sleep(3)
            #r = requests.get('http://www.equibase.com/static/entry/index.html?SAP=TN')
        else:
            break
    soup = bs.BeautifulSoup(r.text,'lxml')
    #print(soup)
    table = soup.find('table')
    #print(table)
    tr = table.find_all('tr')
    #Featured Tracks	Today	Tomorrow	Future	Past
    length = len(tr)
    eventlist = []
    for i in range(1,length,1):
        tds = tr[i].find_all('td')
        #print(tds[1])
        name = tds[0].text
        try:
            url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            date = tds[1].find('a').text
        except:
            print("No event today at " + name)
        else:
            print(url)
            #url = 'http://www.equibase.com' + tds[1].find('a').get('href')
            events = {
                'date' : date,
                'name' : name,
                'url' : url,
            }
            eventlist.append(events)
    print(eventlist)
    get_races(eventlist)

