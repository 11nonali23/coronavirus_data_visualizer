import requests, json

#This script is made to request and parse data (JSON format)

#return latest data in global scale
def getLatest():
    latest =	{
    "confirmed": get_confirmed(),
    "deaths": get_deaths(),
    "recovered": get_recovered()
    } 
    
    return latest

#return word percenual values
def get_world_percentage():
    
    con = int(get_confirmed())
    rec = int(get_recovered())
    death = int(get_deaths())
    
    perc = {
        "recovered" : int(100/(con/rec)),
        "deaths": int(100/(con/death))
    }
    
    return perc

def get_Italy(): 
    
    with open ('/home/andrean/Scaricati/ProtCivileDati/COVID-19/dati-json/dpc-covid19-ita-andamento-nazionale.json', 'r') as file:
        
        data = json.load(file)
        
        return data
            
    return None

def get_Italy_Regions():
    
    with open ('/home/andrean/Scaricati/ProtCivileDati/COVID-19/dati-json/dpc-covid19-ita-regioni.json', 'r') as file:
        
        data = json.load(file)
        
        #getting length of data and sub 1 to get last element
        data_lenght = len(data) - 1
        
        #returing the last datas
        data = data[(data_lenght - 20 ) : (data_lenght + 1)]
        
        return data
    
    return None
