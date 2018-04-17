import requests 


proxies = { 
    'http' : 'http://159.65.107.239:8888'
}

r = requests.get('http://equineline.com',proxies=proxies)

print(r.headers)