#this script uses beatifulsoup the "sole 24 ore web page" (you can find it on readme.md) to get the current general data


import requests
from bs4 import BeautifulSoup


#use beaftiful soup to find general data
def soupCounters():
    
    targetUrl = 'https://lab24.ilsole24ore.com/coronavirus/'

    page = requests.get(targetUrl)

    soup = BeautifulSoup(page.content, "html.parser")
    
    general = [val["data-to"] for val in soup.findAll("h2",{"class":"timer"})]
    
    tot = int(general[3])
    
    deaths = int(general[1])
    
    rec = int(general[2])
    
    dperc = int(100/(tot/deaths))
    
    rperc = int(100/(tot/rec))
    
    data = {
        "general": general,
        "deathperc": dperc,
        "recperc": rperc
    }
    
    return data
