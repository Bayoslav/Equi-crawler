import requests 
#'http://35.231.21.43:8888'
proxies = {
    'http' : 'http://35.190.142.78:8888',
    'https' : 'https://35.190.142.78:8888',
    }
req = requests.get('http://chicago.craigslist.org/search/cto?query=ford+mustang&sort=rel&max_price=5000&min_auto_year=2001',proxies=proxies, allow_redirects=False)
#print(dir(req.connection.proxy_manager))
#print(getattribute(req.connection.proxy_headers))
#print(str(req.connection.proxy_manager.values))
#print(req.text)
print(req.headers)
ime = req.history[0].headers['x-cache-proxyname']
#print(r.headers)
payld = {
'name' : ime,
}
print(ime)
headers={'Authorization' : 'd2VhcmVzZWN1cmU='}
ipic = proxies.get('http')
ipic = ipic[0:-1] + '9'
print(ipic)
stop = requests.post(ipic + '/instances/stop', json=payld,headers=headers)