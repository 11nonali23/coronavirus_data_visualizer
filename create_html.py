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
    #getting the italy dictionary from JSON file
    italy_dict = track.get_Italy().get('history')

    #creating x and y coordinates
    x = [i for i in range(0,len(italy_dict))]
    y = [int(italy_dict.get(date)) for date in italy_dict]

    #writing the date value every two of them
    ticks = []
    iter = 0;
    for val in italy_dict:
        if iter == 0:
            ticks.append(parse(val))
            iter = iter + 1
        if iter == 1:
            ticks.append("")
            iter = 0


    #creating the figure with matplotlib
    fig = Figure(figsize=(15, 4))

    #divinding into subplots
    ax = fig.subplots()

    #setting x label
    ax.set_xticks(range(len(italy_dict)))

    ax.set_xticklabels(ticks, rotation=45)

    #plotting diagram
    ax.plot(x,y)

    #setting labels
    ax.set_xlabel('days from first affected person', size=20)
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
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of people are dead</h3></li>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of people are recovered from virus disease</h3></li>
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
            <li><h3 style="font-family: courier,arial,helvetica;"><b> about {}%</b> of people are dead</h3></li>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of people are recovered from virus disease</h3></li>
        </ul>
    </div>
""".format(data.get('confirmed'), data.get('deaths'), data.get('recovered'), percentage.get('deaths'), percentage.get('recovered'))

    #write on file
    with open('dynamic_html_files/world.html', 'w') as file:
        file.write(html)
    
        
   
#exec methods
italy_graph()

save_html_from_sole_24()

save_html_word()
