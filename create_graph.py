from matplotlib.figure import Figure
import mpld3
import tracker as track

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

#ax.set_xticklabels([val for val in italy_dict], rotation=45)
ax.set_xticklabels(ticks, rotation=45)


ax.plot(x,y)

ax.set_xlabel('days from first affected person', size=20)
ax.set_ylabel('affected people', size=20)
ax.set_title('People discovered to have virus', size=40)

mpld3.save_html(fig, 'graph.html')
