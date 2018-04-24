import requests 
import bs4 as bs 

proxies = {
    'http' : 'http://159.65.107.239:8888',
    'https' : 'https://159.65.107.2398888',
    }
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 
                'x-requested-with': 'XMLHttpRequest','Accept-Encoding' : 'gzip, deflate', 
                'Cache-Control': 'max-age=0', 'Connection' : 'keep-alive', 'Cookie' : 'CFID=42760483; CFTOKEN=bdd03ad8b9d75f10%2D2152DD43%2D5056%2DBE2F%2D78E5D1FFBA809844; TIMEVISITED=%7Bts%20%272018%2D04%2D21%2015%3A43%3A55%27%7D; __unam=10bb875-162e9bbc10f-42955c48-10',
                'Host' : 'www.equineline.com','Referer' : "equineline.com",
                'Upgrade-Insecure-Requests' : '1' }
                 #http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=' + horsename + '&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y'
                 #http://www.equineline.com/Free-5X-Pedigree.cfm/=Winner%20(JPN)?page_state=DISPLAY_REPORT&reference_number=9851563&registry=T&horse_name==Winner%20(JPN)&dam_name==Winner%20Balance%20(JPN)&foaling_year=2013&include_sire_line=Y
horsename = "Jack(AUS)"
horsereq = requests.get("http://www.equineline.com/Free5XPedigreeSearchResults.cfm?horse_name=" + horsename + "&page_state=LIST_HITS&foaling_year=&dam_name=&include_sire_line=Y",headers=headers,proxies=proxies)
soup = bs.BeautifulSoup(horsereq.text, 'lxml')
print(horsereq.text)
horsrl = soup.find('a').get('href')
url = 'http://www.equineline.com/' + horsrl
print(url)
start = url.find('reference_number=')
end = url.find('&registry')
refnum = url[start+17:end]
print(refnum)

referer = "http://www.equineline.com/Free-5X-Pedigree.cfm?page_state=PROCESS_SUBMIT&horse_name=" + horsename.replace(" ", "%20")
headers = {'user-agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)', 
                'x-requested-with': 'XMLHttpRequest','Accept-Encoding' : 'gzip, deflate', 
                'Cache-Control': 'max-age=0', 'Connection' : 'keep-alive', 'Cookie' : "FID=42804404; CFTOKEN=8f6e8476d60b4c3c%2D56A61811%2D5056%2DBE2F%2D782EE3F328AD8376; TIMEVISITED=%7Bts%20%272018%2D04%2D22%2016%3A35%3A43%27%7D; __unam=10bb875-162e9bbc10f-42955c48-26",
                'Host' : 'www.equineline.com','Referer' : referer,
                'Upgrade-Insecure-Requests' : '1' }
link = url
maker = requests.get(link,headers=headers,timeout=9,proxies=proxies)
supica = bs.BeautifulSoup(maker.text,'lxml')
table = supica.find_all('div',class_='col-xs-2 col2-pedigree')
print(table)
#print(maker.text)
f = open('example3.html','w')
f.write(maker.text)
f.close()
#print("\n\nKEK\n\n")
#print(table[0])
horsebride = table[0].find_all('div')[0].text #prvi zavrsen
#print(horsebride)
def name_fix(horse_html):
    horsebride = horse_html
    if(horsebride[0]==" "):
        horsebride = horsebride[1:]
    sechorseb = horsebride[1:]
    zarezj = sechorseb.find(",")

    sechorseb = sechorseb[zarezj+2:].replace("  ", "")


    #dudu = sechorseb.find_all(" ")
    #print(sechosreb[dudu:])
    sechorseb = sechorseb.replace(" ", ",")
    print(sechorseb[-1])
    sechorseb = sechorseb[:-1]
    if(sechorseb[-1]==","):
        sechorseb = sechorseb[:-1]
    #print(listic)
    lenic = len(sechorseb)
    firsthorse = horsebride[1:zarezj-1] + (sechorseb[0:lenic-2])
    return firsthorse



tabletwo = supica.find_all('div',class_='col-xs-2 col3-pedigree')
horsehuss = tabletwo[0].find_all('div')[1].text

final_string = (name_fix(horsebride)) + "," + (name_fix(horsehuss))

#print(r.headers)

