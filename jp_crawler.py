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
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}

def get_table(table):
    #soup = bs.BeautifulSoup(table,'lxml')
    i=0
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
            'starters' : tds[3].text,
            'winners' :  tds[4].text,
            'BW (%)' : tds[5].text,
            'earnings' : tds[6].text,
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
            'starters' : tds[3].text,
            'winners' :  tds[4].text,
            'BW (%)' : tds[5].text,
            'earnings' : tds[6].text,
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
                'starters' : tds[3].text,
                'winners' :  tds[4].text,
                'BW (%)' : tds[5].text,
                'earnings' : tds[6].text,
                'ael' : tds[7].text,
                }   
                #print(dict)
                dictlist.append(dict)
    return dictlist             
#r = requests.get('http://210.145.16.108/jair/SelectRaceYear.do?command=GO',headers=headers)
def get_events(datic):
    global fontic
    formData = {
        'raceYmd' : datic,
        'command' : 'displayRaceList'
    }
    print(formData)
    while(1):
        try:
            kk = requests.post('http://210.145.16.108/jair/SelectRace.do',headers=headers,data=formData)
        except:
            tim.sleep(5)
            pass
        else:
            break
        
    soup = bs.BeautifulSoup(kk.text,'lxml')
    print(soup)
    fontic = datic
    #print(fontic[2])
    #print(soup)
    #print(time.strftime("%Y/%m/%d"))
    soup = soup.find('table', attrs={'width': 584})
    tr = soup.find_all('tr')
    #print(tr[0].find('strong'))
    td = tr[0].find_all('td', attrs={'width' : '32%'})
    events = []
    print(len(td))
    for i in range(0,len(td)):
        txt = td[i].find('strong').text
        if(txt == ''):
            print("nothing")
        else:
            event = {
                'name' : txt,
                'races' : []
            }
        events.append(event)
    print(events)
    get_races(events)
    
def get_races(events):
    global fontic
    headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'https://www.equibase.com',
                'x-requested-with': 'XMLHttpRequest'}
    formData = {
        'raceYmd' : fontic,
        'command' : 'displayRaceList'
    }
    kk = requests.post('http://210.145.16.108/jair/SelectRace.do',headers=headers,data=formData)
    soup = bs.BeautifulSoup(kk.text,'lxml')
    #print(soup)
    #print(time.strftime("%Y/%m/%d"))
    soup = soup.find('table', attrs={'width': 584})
    tr = soup.find_all('tr')
    lop=0
    ev=0
    proxies = {
    'http' : 'http://159.65.107.239:8888',
    'https' : 'https://159.65.107.239:8888',
    }
    for trs in tr[1:len(tr)]:
        tds = trs.find_all('td')
        for i in range(0,len(tds),3):
            
            #tds0 - vremeprva, #tds1  uputstva za slanje linka 
            #tds2 - vremedruga, #tds3 uputstva za slanje linka
            time = tds[0+i].text.replace(" ","")
            inform = tds[1+i]
            
            a = inform.find('a') #informator za post rikvest
        #print(inform)
            #print(a)
            kek = (a.get('href')[19:400].replace("(","").replace(")","").replace(" ", "")).strip(' \t\n\r') #isto kao dolje
            kek = kek.split(',')
            nl = []
            for word in kek: #uklanja /n i ostalo
                word = word.strip(" \t\n\r ' ")
                #print(word)
                nl.append(word)
            print(nl)
            res = {
                'command':'dispDenmaList',
                'raceY':nl[0],
                'raceMd':nl[1],
                'raceJoCd':nl[2],
                'raceKai':nl[3],
                'raceHi':nl[4],
                'raceNo':nl[5],
                'dataKbn':nl[6],
            }
            race = { 
                    'time' : time,
                    'instr' : res,
                    }
            uuu = int(i/3)
            events[uuu]['races'].append(race)
        
       # W#event[lop]['races'] = 
        #p#rint(res)
    for me in events:
       for race in (me['races']):
            #horselist = []
            #print(race['time'])
            no = race['instr']['raceNo'].replace(" ", "")
            #print(race['time'] + " - " +  race['instr']['raceNo'])
    #print(events)
            if(no == ''):
                print("no race")
            else:

                url = 'http://210.145.16.108/jair/SelectDenma.do'
                #formData = {'command': 'dispRaceResult', 'raceY': '2017', 'raceMd': '1126', 'raceJoCd': '05', 'raceKai': '05', 'raceHi': '08', 'raceNo': '01', 'dataKbn': '7'}
                formData = race['instr']
                req = requests.post(url,data=formData)
                #<table cellspacing="0" cellpadding="2" width="720" border="0">
                soup = bs.BeautifulSoup(req.text,'lxml')
                tablic = soup.find_all('table',attrs={'cellspacing' : 0, 'cellpadding' : 2, 'width' : 720, 'border' : 0})
                #print(tablic)
                print("\n\nHERE\n\n")
                #<td nowrap=""><font size="2">March 4, 2018, 1800m, Dirt,
     
                print(tablic[1])
                kupa = tablic[1].find_all('td')
                first = kupa[0].text.split(",")
                second = kupa[1].text.split(",") 
                distance = first[2]
                surface = first[3]
                age = second[2]
                try:
                    value = second[4][-2:] + second[5] + second[6]
                except: 
                    value = second[4][-2:] + second[5]
                print(second[4])
                weight = second[1]
                race['distance'] = distance
                race['surface'] = surface
                race['age'] = age 
                race['value'] = value 
                race['weight type'] = weight
                print(race)
                
                table = soup.find('table',attrs={'cellspacing' : 0, 'cellpadding' : 0, 'width' : 720, 'bgcolor' : '#ffffff', 'border' : 0})
                tr = table.find_all('tr')
                #print(tablic)
                #newtr = tablic[1].find_all('tr')
                length = len(tr)
                eventlist = []
                #print("kek", length)
                horselist = []
                for i in range(4,length,1):
                    #print(i)
                    tds = tr[i].find_all('td')
                    #print(tds[5])
                    fontsss = tds[5].find_all('font')
                    Sire = (fontsss[0].text)
                    Dam = fontsss[1].text
                    fontsss = tds[7].find_all('font')
                    Jockey = fontsss[0].text
                    Trainer = fontsss[1].text
                    #print(tds[2])
                    #break
                    #newtds = newtr[i-4].find_all('td')
                    #print(newtds)
                    #hor = newtds[4].find_all('font')
                    #siredam = newtds[2].find_all('font')
                    #print(tds[2].text + " " + tds[3].text + " Jockey: " + hor[0].text + " Trainer: " + hor[1].text + "Sire" + siredam[0].text + "dam" + siredam[1].text)
                    ##print("itsthis")

                    horseurl = 'http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + tds[2].text  + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'
                    print(horseurl)
                    #print("itsthis")
                    while(1):
                        try:
                            ###proxies = get_proxy()
                            horsereq = requests.get(horseurl,headers=headers,timeout=9,proxies=proxies)
                        except:
                            print('error')
                            tim.sleep(12)
                            horsereq = requests.get(horseurl,headers=headers,timeout=9,proxies=proxies)
                            continue
                        else:
                            #print("mek")
                            break              
                    soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                    h4 = soup.find('h4')
                    #print(h4)
                    if(str(h4)=='<h4><strong>No Matches Found</strong></h4>'):
                        print("Horse doesn't exist in DB")
                        inftab = 'n/a'
                    else:
                    #print(soup)
                        try:
                            horsrl = soup.find('a').get('href')
                        except:
                            print("Captcha error")
                            try:
                                ime = horsereq.headers['x-cache-proxyname']
                            except:
                                print("ime error")
                                tim.sleep(3)
                            else:
                                payld = {
                                'name' : ime,
                                }
                                print(ime)
                                headers={'Authorization' : 'Zm9ybXVsYTE='}
                                ipic = proxies.get('http')
                                ipic = ipic[0:-1] + '9'
                                print(ipic)
                                stop = requests.post(ipic + '/api/instances/stop', json=payld,headers=headers)
                                print("success")
                            
                            ###proxies = get_proxy()
                            #time.sleep(6)
                            while(1):
                                try:
                                    ##proxies = get_proxy()
                                    headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 'origin': 'http://www.equibase.com',
                                    'x-requested-with': 'XMLHttpRequest'}
                                    horsereq = requests.get(horseurl,headers=headers,timeout=9,proxies=proxies)
                                    soup = bs.BeautifulSoup(horsereq.text, 'lxml')
                                    horsrl = soup.find('a').get('href')
                                except:
                                    print("Error at 195 line.")
                                    #print(soup)
                                    try:
                                        ime = horsereq.headers['x-cache-proxyname']
                                    except:
                                        print("ime error")
                                        #print(horsereq.headers)
                                        print(horsereq.headers)
                                        print(horsereq.history)
                                        tim.sleep(3)
                                    else:
                                        payld = {
                                        'name' : ime,
                                        }
                                        print(ime)
                                        headers={'Authorization' : 'Zm9ybXVsYTE='}
                                        ipic = proxies.get('http')
                                        ipic = ipic[0:-1] + '9'
                                        print(ipic)
                                        stop = requests.post(ipic + '/api/instances/stop', json=payld,headers=headers)
                                        print(stop)
                                        time.sleep(6)
                                        #continue
                                else:
                                    break
                            ###proxies = get_proxy()
                            #tim.sleep(6)
                            
                            #soup = bs.BeautifulSoup(horsereq.text, 'lxml') 
                        #h#orsrl = soup.find('a').get('href')
                        url = 'http://www.equineline.com/' + horsrl
                        start = url.find('reference_number=')
                        end = url.find('&registry')
                        refnum = url[start+17:end]
                        print(refnum)
                        link = 'http://www.equineline.com/Free5XPedigreeNickingDisplay.cfm?page_state=DISPLAY_REPORT&reference_number=' + refnum
                        #print(url)
                        #print(link)
                        while(1):
                            try:
                                ##proxies = get_proxy()
                                maker = requests.get(link,headers=headers,timeout=9,proxies=proxies)
                                supica = bs.BeautifulSoup(maker.text,'lxml')
                                table = supica.find('table')
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
                            except:
                                continue
                            else:
                                break
                        #print(supica)
                    # table = supica.find('table')
                        #print(table)
                        #print(type(table))
                        while(1):
                            try:
                                if(table is None):
                                    tim.sleep(6)
                                    ##proxies = get_proxy()
                                    raise EnvironmentError
                                else:
                                    break
                            except:
                                while(1):
                                    try:
                                        maker = requests.get(link,headers=headers,timeout=9,proxies=proxies)
                                    except:
                                        continue
                                    else:
                                        break
                                break

                                supica = bs.BeautifulSoup(maker.text,'lxml')
                                table = supica.find('table')
                            
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
                    #print(tds)
                    #print("K")
                    
                    #print(tds[6])
                    fontsss = tds[8].find_all('font')
                    #print(fontsss[0].text)
                    horsedic = {
                        'P#' : tds[1].text,
                        'Name' : tds[2].text,
                        'Claim' : 'No claim',
                        'Wgt' : tds[4].text,
                        'Jockey' : Jockey,
                        'Trainer' : Trainer,
                        'Sire' : Sire,
                        'Dam' : Dam,
                        'info' : inftab,
                        'uuid' : ud,
                    }
                    #print(horsedic)
                    horselist.append(horsedic)
                race['horses'] = horselist
            #print(horselist)
    print(events)
    #print(formData)
    #print(formData.get('raceYmd'))
    obj = Country.objects.get(id=4)
    realdate = ast.literal_eval(obj.date)
    realdate.add(fontic)
    obj.date = realdate
    obj.dicts = events 
    obj.save()
    
    
    #datic = datetime.date.today()
    d = str(fontic)
    filename = 'JP' + d + '.json'
    path = "JPFiles"
    fullpath = os.path.join(path, filename)
    f=open(fullpath,'w')
    jsonero = json.dumps(events)
    f.write(jsonero)
    f.close()
    p = Podesavanja.objects.get(id=1)
    p.is_scraping = 0
    p.save()
    scaling_payload = {
                    "min": "0",
                    "required": "0",
                    "max": "9",
                    }
    headers={'Authorization' : 'Zm9ybXVsYTE='}
    rer = requests.patch('http://159.65.107.239:8889/api/scaling',json=scaling_payload,headers=headers)
    print(rer)

    #print(events)
        #print(events)
                #for ev in range(0,len(events),2):
                
      
        
while(1):
    obj  = Country.objects.get(id=4)
    dat = obj.date
    curr_date = (datetime.date.today())
    dat = ast.literal_eval(dat)
    curr_date = curr_date.strftime('%Y%m%d')
    #print(type(datke))
    #print(datke)
    while(1):
        try:
            r = requests.get('http://210.145.16.108/jair/SelectRaceYear.do?command=GO')
        except: 
            pass 
        else:
            break
    soup = bs.BeautifulSoup(r.text,'lxml')
    #fontic = soup.find_all('font', attrs={'color' : '#0000ff', 'size' : 3 })
    tdis = soup.find_all('td', attrs={'valign' : 'middle'})
    #print(tdis)
    #print(fontic)
    #datic = (fontic[2].text).replace('/', '') #after 2 increment +67
    datelist = set()
    #print(fontic[4].text).replace('/', '')
    for i in range(2,16,2):
        datic = (tdis[i].text).replace('/', '')
        print(datic)
        if(datic==''):
            pass
        else:

            datelist.add(datic)
    

    print("d")
    #print
    print(datelist)
    dates_list = datelist - dat
    print(dates_list)
    print(dat)
    #print(fontic[14])
    #print(datic)
    print(len(dates_list))
    if(len(dates_list)==0):
        print("No new races for today - ", curr_date)
        time.sleep(1200)
    else:
        #dates_list = list(dates_list)
        for datke in dates_list:
            print(datke)
            print("New race! Scraping")
            p = Podesavanja.objects.get(id=1)
            while(1):
                if (p.is_scraping):
                    print("Waiting for other crawlers to finish scraping")
                    tim.sleep(1200)
              
                scaling_payload = {
                    "min": "1",
                    "required": "7",
                    "max": "9",
                    }
                headers={'Authorization' : 'Zm9ybXVsYTE='}
                rer = requests.patch('http://159.65.107.239:8889/api/scaling',json=scaling_payload, headers=headers)
                print(rer)
                #tim.sleep(60)
                #p.is_scraping = 1
                #p.save()
                print(datke)
                print("Saving P")
                get_events(datke)
                break
        #get_events(datke)
  
    #get_events("20180304")
    #get_events(datic)   
#get_life()
#print(fontic)
#cities = td[0].find('strong').text + "  " + td[1].find('strong').text


#print(soup)'''
'''for trs in tbody[2:len(tbody)]:
    print
    trs = trs.find('font').text.replace(" ", "")
    print(trs)'''
#trs = tbody.find_all('font')
#print(trs)
    
    


#print(fonts)
