#Run in AGOL
from arcgis.gis import GIS
gis = GIS("home")


from arcgis.gis import GIS
gis = GIS()


item = GIS(verify_cert=False).content.get("85d0ca4ea1ca4b9abf0c51b9bd34de2e")
flayer = item.layers[0]


sdf = flayer.query(where="AGE_45_54 < 1500").df

map1 = gis.map('Reno, NV', zoomlevel=4)
map1


sdf.plot(kind='map', map_widget=map1,
        renderer_type='c',  
        method='esriClassifyNaturalBreaks', 
        class_count=20,  
        col='POPULATION', 
       cmap='prism',  
        alpha=0.7  
       )

map1.layers

dict(map1.layers[0].layer.layerDefinition.drawingInfo.renderer).keys()

class_breaks = mapq.layers[0].layer.layerDefinition.drawingInfo.renderer.classBreakInfos
print(len(class_breaks))


cbs_list = []
cmap_list = []
for cb in class_breaks:
    print(cb.description)  
    cbs_list.append(cb.classMaxValue)
    cmap_list.append([x/255.0 for x in cb.symbol.color])


# histogram
import matplotlib.pyplot as plt

n, bins, patches = plt.hist(sdf['POPULATION'], bins=cbs_list)






