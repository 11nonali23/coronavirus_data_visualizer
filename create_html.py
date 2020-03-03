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

def italy_graph():
    #getting the italy dictionary from JSON file
    italy_dict = track.get_Italy().get('history')

    #creating x and y coordinates
    x = [i for i in range(0,len(italy_dict))]
    y = [int(italy_dict.get(date)) for date in italy_dict]

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
    fig = Figure(figsize=(8, 4))

    ax = fig.subplots()

    ax.set_xticks(range(len(italy_dict)))

    ax.set_xticklabels(ticks, rotation=45)


    ax.plot(x,y)

    ax.set_xlabel('days from first affected person', size=20)
    ax.set_ylabel('affected people', size=20)
    ax.set_title('People discovered to have virus', size=40)

    mpld3.save_html(fig, 'graph.html')

def save_html_from_sole_24():
    
    data = ss24.soupCounters()
    
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
            <h2 style="color: #00cc00; text-align: center">RECOVERED: {}</h2>
        </div>
    </div>
""".format(data[3],data[1],data[2])

    with open('soup_sole24_ore.html', 'w') as file:
        file.write(html)
        
 
def save_html_word():
    
    data = track.getLatest()
    
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
            <h2 style="color: #00cc00; text-align: center">RECOVERED: {}</h2>
        </div>
    </div>
""".format(data.get('confirmed'), data.get('deaths'), data.get('recovered'))

    with open('world.html', 'w') as file:
        file.write(html)
    
        
        
italy_graph()

save_html_from_sole_24()

save_html_word()
