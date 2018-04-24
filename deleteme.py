    import bs4 as bs

    word = '<ons-list-item id="itembtn" name="itembtn" value="{{ record [0] }}" tappable>'

    soup = bs.BeautifulSoup(word,'lxml')

    supa = soup.find('ons-list-item',attrs={'id' : 'itembtn'})
    #print(supa)
    print(supa.get('value'))