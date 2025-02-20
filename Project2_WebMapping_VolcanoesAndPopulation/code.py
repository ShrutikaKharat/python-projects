import folium
import pandas

data = pandas.read_csv("volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])


def color_producer(elevat):
    if elevat < 1000:
        return 'yellow'
    elif 1000 <= elevat < 3000:
        return 'blue'
    else:
        return 'red'


map = folium.Map(location=[45, -120], zoom_start=6, tiles="Stamen Terrain")

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=7, popup=nm + " "+str(el) + "m",
                                      fill_color=color_producer(el), color='black', fill_opacity=0.6))


fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
                             style_function=lambda x: {'fillColor': 'yellow' if x['properties']['POP2005'] < 10000000 else 'blue' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")
