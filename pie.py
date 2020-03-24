from matplotlib.figure import Figure
import mpld3
from mpld3 import plugins
import tracker as track
import numpy as np

regions_data = track.get_Italy_Regions()

def set_text(pct, allvals):
    absolute = int(pct/100.*np.sum(allvals))
    return "{:.1f}%".format(pct, absolute)


def create_pie_chart():
    
    import matplotlib.pyplot as plt
    wanted_regions = {"Lombardia"}
    max_size = 0
    max_reg = "Lombardia"

    #initializing labels and sizes only with regions i want
    labels = []
    sizes = []

    #setting most amount of swabs regions
    for i in range(0,7):
        max_size = 0
        for dic in regions_data:
            if dic.get('denominazione_regione') not in wanted_regions and dic.get('tamponi') > max_size:
                max_size = dic.get('tamponi')
                max_reg = dic.get('denominazione_regione')
            else:
                continue
        wanted_regions.add(max_reg)
    
    
    total_others = 0 #other regions total swabs

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

    #explode = [0.1 for val in labels]  #setting margin between slices

    fig1, ax1 = plt.subplots(figsize=(9, 11))
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', textprops={'fontsize': 15}, labeldistance=0.98,
            shadow=False, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.



    mpld3.save_html(fig1, "/home/andrean/Scrivania/ht.html")
	
create_pie_chart()
