from matplotlib.figure import Figure
import mpld3
import tracker as track
import numpy as np

regions_data = track.get_Italy_Regions()



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


    explode = [0.1 for val in labels]  #setting margin between slices

    fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(aspect="equal"))

    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%".format(pct, absolute)


    wedges, texts, autotexts = ax.pie(sizes, explode = explode, labels=labels, 
					autopct=lambda pct: func(pct, sizes),
                                  		textprops=dict(color="w"))

    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.setp(autotexts, size=14, weight="bold")

    ax.set_title("Swabs for regions in percentage")

    plt.tight_layout()
    
    plt.show()

    mpld3.save_html(fig, "/home/andrean/Scrivania/ht.html")
	
create_pie_chart()
