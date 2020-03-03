import requests, json
import soup_sole24ore as ss24

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

#return Italy dictionary of data and save data in italyData.json
def get_Italy(): 
    for obj in data.get('confirmed').get('locations'):
        
        #save in italyData.json
        with open('italyData.json', 'w') as file: 
            json.dump(obj, file)
            
        #here i modify the data from 2/3 to 2/9 because they are wrong.
        #i just put the same value as 1/3
        if obj.get('country') == 'Italy':
            obj.get('history')['2/3/20'] = '1128'
            obj.get('history')['2/4/20'] = '1128'            
            obj.get('history')['2/5/20'] = '1128'
            obj.get('history')['2/6/20'] = '1128'
            obj.get('history')['2/7/20'] = '1128'
            obj.get('history')['2/8/20'] = '1128'
            obj.get('history')['2/9/20'] = '1128'
            return(obj)
    return None

def save_html_from_sole_24():
    
    data = ss24.soupCounters()
    
    html = """
    <link rel="stylesheet" type="text/css" href="general_info.css">
    <div class="row">
        <div class="column">
            <h2 style="color: #ff3300;">TOTAL: {}</h2>
        </div>
        <div class="column">
            <h2 style="color: #994d00;">DEATHS: {}</h2>
        </div>
        <div class="column">
            <h2 style="color: #00cc00;">RECOVERED: {}</h2>
        </div>
    </div>
""".format(data[3],data[1],data[2])

    with open('soup_sole24_ore.html', 'w') as file:
        file.write(html)

get_Italy()

save_html_from_sole_24()




















