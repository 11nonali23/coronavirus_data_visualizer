from matplotlib.figure import Figure
import mpld3
import tracker as track

#This script create html file that are added with iframe into index.html

#parse the date to remove the year
def parse(date):
    
    #getting last element
    date_len = len(date) - 1
    
    #removing the year part
    date = date[5: date_len]
    
    result = ""
    
    #adding only day and month
    for char in date:
        if char == " ":
            break
        result += char
    
    return result

#getting italian dictionary
italy_list = track.get_Italy()

#creating italy graph with mpld3 and matplotlib and saving it into html file
def italy_graph():
    
    #get total cases
    affected = [dic.get('totale_casi') for dic in italy_list]
    #getting all dates
    history =[dic.get('data') for dic in italy_list]

    #creating x and y coordinates
    x = [i for i in range(0,len(italy_list))]
    y = [int(num) for num in affected]
    ticks = [parse(date) for date in history]

    #creating the figure with matplotlib
    fig = Figure(figsize=(10, 4))

    #divinding into subplots
    ax = fig.subplots()

    #setting x label
    ax.set_xticks(x)

    ax.set_xticklabels(ticks, rotation=45)

    #plotting diagram
    ax.plot(x,y, color=	'magenta')

    #setting labels
    ax.set_ylabel('affected people', size=20)
    ax.set_title('People discovered to have virus', size=40)

    #save html with library function
    mpld3.save_html(fig, 'dynamic_html_files/graph.html')
    
#creating italy cure graph with mpld3 and matplotlib and saving it into html file
def italy_cure_graph():
    
    #get total cases
    intensiva = [dic.get('terapia_intensiva') for dic in italy_list]
    ricoverati = [dic.get('ricoverati_con_sintomi') for dic in italy_list]
    domiciliare = [dic.get('isolamento_domiciliare') for dic in italy_list]

    #getting all dates
    history =[dic.get('data') for dic in italy_list]

    #creating x and y coordinates
    x = [i for i in range(0,len(italy_list))]
    y_intensiva = [int(num) for num in intensiva]
    y_ric_sintomi = [int(num) for num in ricoverati]
    y_domiciliare = [int(num) for num in domiciliare]
    
    
    ticks = [parse(date) for date in history]

    #creating the figure with matplotlib
    fig = Figure(figsize=(10, 4))

    #divinding into subplots
    ax = fig.subplots()

    #setting x label
    ax.set_xticks(x)

    ax.set_xticklabels(ticks, rotation=45)

    #plotting diagram
    ax.plot(x,y_intensiva, color=	'magenta')
    ax.plot(x,y_ric_sintomi, color=	'green')
    ax.plot(x,y_domiciliare, color=	'blue')

    #setting labels
    ax.set_ylabel('values for all', size=20)
    ax.set_title('Growth of care methods', size=40)

    ax.legend(["terapia intensiva", "ricoverati con sintomi", "isolamento domiciliare"], prop={'size': 13})
    
    #save html with library function
    mpld3.save_html(fig, 'dynamic_html_files/cure_graph.html')
    
#creating italy deaths and recovered graph with mpld3 and matplotlib and saving it into html file
def italy_death_rec_graph():
    
    #get total cases
    deceduti = [dic.get('deceduti') for dic in italy_list]
    dimessi = [dic.get('dimessi_guariti') for dic in italy_list]

    #getting all dates
    history =[dic.get('data') for dic in italy_list]

    #creating x and y coordinates
    x = [i for i in range(0,len(italy_list))]
    y_deceduti = [int(num) for num in deceduti]
    y_dimessi = [int(num) for num in dimessi]
    
    
    ticks = [parse(date) for date in history]

    #creating the figure with matplotlib
    fig = Figure(figsize=(10, 4))

    #divinding into subplots
    ax = fig.subplots()

    #setting x label
    ax.set_xticks(x)

    ax.set_xticklabels(ticks, rotation=45)

    #plotting diagram
    ax.plot(x,y_deceduti, color=	'magenta')
    ax.plot(x,y_dimessi, color=	'green')

    #setting labels
    ax.set_ylabel('values for both', size=20)
    ax.set_title('Deaths and Recovers', size=40)

    ax.legend(["deceduti", "dimessi e guariti"], prop={'size': 15})
    
    #save html with library function
    mpld3.save_html(fig, 'dynamic_html_files/deceduti_rimessi.html')

        
#create html for general updates
def general_updates():
    #getting last element index
    last_element = len(italy_list) - 1
    #getting last element data
    data = italy_list[last_element]
    
    #deaths percentual
    dperc = str(int(100/((data.get('totale_casi'))/(data.get('deceduti')))))
    
    #recovered percentual
    rperc = str(int(100/((data.get('totale_casi'))/(data.get('dimessi_guariti')))))
    
    #getting plus amount of deaths
    plus_deaths = "+" + str(data.get('deceduti') - italy_list[(last_element - 1)].get('deceduti'))
    
    #getting plus amount of recovered
    plus_rec = "+" + str(data.get('dimessi_guariti') - italy_list[(last_element - 1)].get('dimessi_guariti'))
    
    #getting plus amount of total
    plus_tot = "+" + str(data.get('totale_casi') - italy_list[(last_element - 1)].get('totale_casi'))
    
    html = """
    <link rel="stylesheet" type="text/css" href="general_info.css">
    <div class="row">
        <div class="column">
            <h2 style="color: #91067a; text-align: center"><p>TOTAL:</p> <p>{}</p></h2>
        </div>
        <div class="column">
            <h2 style="color: #181c6b; text-align: center"><p>POSITIVES:</p> <p>{}</p></h2>
        </div>
        <div class="column">
            <h2 style="color: #994d00; text-align: center"><p>DEATHS:</p> <p>{}</p></h2>
        </div>
        <div class="column">
            <h2 style="color: #009933; text-align: center"> <p>HEALINGS:</p> <p>{}</p></h2>
        </div>
    </div>
    <div class="row">
        <div class="increment">
            <h3 class="plus" style="color: #bf005c;">{}</h3>
        </div>
        <div class="increment">
            <h3 class="plus" style="color: #bf005c;">{}</h3>
        </div>
        <div class="increment">
            <h3 class="plus" style="color: #bf005c;">{}</h3>
        </div>
        <div class="increment">
            <h3 class="plus" style="color: #bf005c;">{}</h3>
        </div>
    </div>
    <div class="percentage_shower" style="margin-top: 40px;">
        <ul>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of known people are dead</h3></li>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of known people are healed </h3></li>
        </ul>
    </div>""".format(str(data.get('totale_casi')), str(data.get('totale_attualmente_positivi')), str(data.get('deceduti')), str(data.get('dimessi_guariti')),
                     plus_tot, "+" + str(data.get('nuovi_attualmente_positivi')), plus_deaths, plus_rec, dperc, rperc)
    
        
    
    with open('dynamic_html_files/general_updates.html', 'w') as file:
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
            <h2 style="color: #ff3300; text-align: center"><p>TOTAL:</p> <p>{}</p></h2>
        </div>
        <div class="column">
            <h2 style="color: #994d00; text-align: center"><p>DEATHS:</p> <p>{}</p></h2>
        </div>
        <div class="column">
            <h2 style="color: #009933; text-align: center"><p>HEALINGS:</p> <p>{}</p></h2>
        </div>
    </div>
    <div class="percentage_shower">
        <ul>
            <li><h3 style="font-family: courier,arial,helvetica;"><b> about {}%</b> of the known people are dead</h3></li>
            <li><h3 style="font-family: courier,arial,helvetica;"><b>about {}%</b> of the known people are recovered from virus disease</h3></li>
        </ul>
    </div>
    """.format(data.get('confirmed'), data.get('deaths'), data.get('recovered'), percentage.get('deaths'), percentage.get('recovered'))

    #write on file
    with open('dynamic_html_files/world.html', 'w') as file:
        file.write(html)
        
        
#getting per region data        
regions_data = track.get_Italy_Regions()
        
#creating html for region table
def create_html_italyTable():
        
    #creating the html string and appending the table definition
    html = """
<link rel="stylesheet" type="text/css" href="table.css">
<table align="center">
    <tr>
        <th>Region</th>
        <th>Positives to swab</th>
        <th>Hospitalized</th>
        <th>Intensive Care</th>
        <th>Home Isolation</th>
        <th>Healings</th>
        <th>Deaths</th>
        <th>Number of Swabs (tamponi)</th>
    </tr>
"""
    
    #adding the data to the stirng for every region
    for dic in regions_data:
        html += "<tr>\n"
        html += "<td>{}</td>\n".format(dic.get('denominazione_regione'))
        html += "<td>{}</td>\n".format(dic.get('totale_attualmente_positivi'))
        html += "<td>{}</td>\n".format(dic.get('ricoverati_con_sintomi'))
        html += "<td>{}</td>\n".format(dic.get('terapia_intensiva'))
        html += "<td>{}</td>\n".format(dic.get('isolamento_domiciliare'))        
        html += "<td>{}</td>\n".format(dic.get('dimessi_guariti'))
        html += "<td>{}</td>\n".format(dic.get('deceduti'))
        html += "<td>{}</td>\n".format(dic.get('tamponi'))
        html += "</tr>\n"
    
    #adding table close tag
    html += "</table>"

                
    #write on file
    with open('dynamic_html_files/table.html', 'w') as file:
        file.write(html) 
        
        
#creating html with mpld3 for pie graph

def create_pie_chart():
    
    import matplotlib.pyplot as plt
    
    #setting regions i want to display
    wanted_regions = {'Lombardia','Emilia Romagna','Veneto','Marche','Piemonte','Toscana','Lazio','Campania'}
    
    #initializing labels and sizes only with regions i want
    labels = []
    sizes = []
    total_others = 0 #other regions total tamponi
    region = ''
    for dic in regions_data:
        region = dic.get('denominazione_regione')
        if region in wanted_regions:
            labels.append(region)
            sizes.append(dic.get('tamponi'))
        else:
            total_others = total_others + int(dic.get('tamponi'))

    #appending other regions and other regions total sum
    labels.append('Other Regions')
    sizes.append(total_others)

    explode = [0.05 for val in labels]  #setting margin between slices

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 12}, labeldistance=1
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.axis('off')
    #plt.tight_layout()

    mpld3.save_html(fig1, "dynamic_html_files/tamponi_pie.html")
    
   
#exec methods
italy_graph()

general_updates()

save_html_word()

create_html_italyTable()

create_pie_chart()

italy_cure_graph()

italy_death_rec_graph()
