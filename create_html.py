from matplotlib.figure import Figure
import mpld3
import tracker as track
import soup_sole24ore as ss24

#This script create html file that are added with iframe into index.html

#parse the date to remove the year
def parse(date):
    result = ""
    
    if (date[1] == "/"):
        result +=date[0:2]
        if (date[3] == "/"):
            result += date[2]
        else:
            result += date[2:4]
    else:
        result += date[0:3]
        if(date[4] == "/"):
            result += date[3]
        else:
            result += date[3:5]
        
    return result

#creating italy graph with mpld3 and matplotlib and saving it into html file
def italy_graph():
    
    #getting italian dictionary
    italy_dict = track.get_Italy().get('history')
    
    #getting the italy history from dictionary of italy    
    history = [val for val in italy_dict]
    affected = [italy_dict[val] for val in italy_dict]
    history = history[23:len(history)]
    affected = affected[23:len(affected)]

    #creating x and y coordinates
    x = [i for i in range(0,len(history))]
    y = [int(num) for num in affected]
    ticks = [parse(val) for val in history]

    #creating the figure with matplotlib
    fig = Figure(figsize=(10, 4))

    #divinding into subplots
    ax = fig.subplots()

    #setting x label
    ax.set_xticks(x)

    ax.set_xticklabels(ticks, rotation=45)

    #plotting diagram
    ax.plot(x,y)

    #setting labels
    ax.set_ylabel('affected people', size=20)
    ax.set_title('People discovered to have virus', size=40)

    #save html with library function
    mpld3.save_html(fig, 'dynamic_html_files/graph.html')
    


#get data from sole 24 ore and create an html file to after include in index.html with iframe
def save_html_from_sole_24():
    
    data = ss24.soupCounters()
    
    #total cases
    gen = data.get('general')
    
    #deaths percentual
    dperc = data.get('deathperc')
    
    #recovered percentual
    rperc = data.get('recperc')
    
    #creating dyinamic html 
    html = """
    <link rel="stylesheet" type="text/css" href="general_info.css">
    <div class="row">
        <div class="column">
            <h2 style="color: #ff3300; text-align: center">TOTAL: {}</h2>
        </div>
        <div class="column">
            <h2 style="color: #994d00; text-align: center">DEATHS: {}</h2>
        </div>
        <div class="column">
            <h2 style="color: #009933; text-align: center">RECOVERED: {}</h2>
        </div>
    </div>
    <div class="percentage_shower">
        <ul>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of the TESTED people are dead</h3></li>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of the TESTED people are recovered from virus disease</h3></li>
        </ul>
    </div>
""".format(gen[3],gen[1],gen[2], dperc, rperc)

    #write on file
    with open('dynamic_html_files/soup_sole24_ore.html', 'w') as file:
        file.write(html)
        
 
#get data from api server and create file to after include in index.html with iframe
def save_html_word():
    
    #get latest data
    data = track.getLatest()
    
    #get percentage of latest data
    percentage = track.get_world_percentage()
    
    html = """
    <link rel="stylesheet" type="text/css" href="general_info.css">
    <div class="row">
        <div class="column">
            <h2 style="color: #ff3300; text-align: center">TOTAL: {}</h2>
        </div>
        <div class="column">
            <h2 style="color: #994d00; text-align: center">DEATHS: {}</h2>
        </div>
        <div class="column">
            <h2 style="color: #009933; text-align: center">RECOVERED: {}</h2>
        </div>
    </div>
    <div class="percentage_shower">
        <ul>
            <li><h3 style="font-family: courier,arial,helvetica;"><b> about {}%</b> of the TESTED people are dead</h3></li>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of the TESTED people are recovered from virus disease</h3></li>
        </ul>
    </div>
""".format(data.get('confirmed'), data.get('deaths'), data.get('recovered'), percentage.get('deaths'), percentage.get('recovered'))

    #write on file
    with open('dynamic_html_files/world.html', 'w') as file:
        file.write(html)
        
def create_html_italyTable():
    
    #getting per region data
    data = track.get_Italy_Regions()
    
    #creating the html string and appending the table definition
    html = """
<link rel="stylesheet" type="text/css" href="table.css">
<table align="center">
    <tr>
        <th>Regione</th>
        <th>Numero Infetti</th>
        <th>Totali Positivi al Test</th>
        <th>Terapia Intensiva</th>
        <th>Isolamento Domiciliare</th>
        <th>Guariti</th>
        <th>Deceduti</th>
        <th>Numero tamponi</th>
    </tr>
"""
    
    #adding the data to the stirng for every region
    for dic in data:
        html += "<tr>\n"
        html += "<td>{}</td>\n".format(dic.get('regione'))
        html += "<td>{}</td>\n".format(dic.get('numero infetti'))
        html += "<td>{}</td>\n".format(dic.get('casi totali'))
        html += "<td>{}</td>\n".format(dic.get('terapia intensiva'))
        html += "<td>{}</td>\n".format(dic.get('isolamento domiciliare'))
        html += "<td>{}</td>\n".format(dic.get('guariti'))
        html += "<td>{}</td>\n".format(dic.get('deceduti'))
        html += "<td>{}</td>\n".format(dic.get('tamponi'))
        html += "</tr>\n"
    
    #adding table close tag
    html += "</table>"

                
    #write on file
    with open('dynamic_html_files/table.html', 'w') as file:
        file.write(html) 
   
#exec methods
italy_graph()

save_html_from_sole_24()

save_html_word()

create_html_italyTable()
