import requests, json

#This script is made to request and parse data (JSON format)

#load JSON file from the implicit url
def loadJSON(url = 'https://coronavirus-tracker-api.herokuapp.com/all'):
    data = requests.get(url)
    content = data.content
    output = json.loads(content)
    return output

data = loadJSON()

#return confirmed cases
def get_confirmed():
    return data.get('latest').get('confirmed')

#return deaths
def get_deaths():
    return data.get('latest').get('deaths')

#return recovered people
def get_recovered():
    return data.get('latest').get('recovered')


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
    

#return Italy dictionary of data and save data in italyData.json
def get_Italy(): 
    for obj in data.get('confirmed').get('locations'):
            
        #here i modify the data from 2/3 to 2/9 because they are wrong. I refer other data from sole 24 ore site (find it on readme.md)
        if obj.get('country') == 'Italy':
            obj.get('history')['2/3/20'] = '1180'
            obj.get('history')['2/4/20'] = '1280'            
            obj.get('history')['2/5/20'] = '1350'
            obj.get('history')['2/6/20'] = '1450'
            obj.get('history')['2/7/20'] = '1520'
            obj.get('history')['2/8/20'] = '1555'
            obj.get('history')['2/9/20'] = '1600'
            return(obj)
            
    return None
