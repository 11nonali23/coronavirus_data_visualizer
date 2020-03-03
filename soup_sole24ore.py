
#this script soup il sole 24 ore page to get the current general data


import requests
from bs4 import BeautifulSoup


def soupCounters():
    
    targetUrl = 'https://lab24.ilsole24ore.com/coronavirus/'

    page = requests.get(targetUrl)

    soup = BeautifulSoup(page.content, "html.parser")

    data = [val["data-to"] for val in soup.findAll("h2",{"class":"timer"})]
    
    return data

