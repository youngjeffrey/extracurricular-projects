import folium
import pandas

data = pandas.read_csv("../data/Volcanoes.txt")
lon = list(data["LON"])
lat = list(data["LAT"])
elev = list(data["ELEV"])
name = list(data["NAME"])

data2 = pandas.read_csv("../data/US_Cities.csv")
lng = list(data2["lng"])
lati = list(data2["lat"])
city = list(data2["city"])
pop = list(data2["pop"])

def color_producer(elevation):
    if elevation < 500:
        return 'pale green'
    elif 500 <= elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 1500:
        return 'yellow'
    elif 1500 <= elevation < 2000:
        return 'red'
    else:
        return 'brown'

def color_producer_2(population):
    if population < 20000:
        return 'light yellow'
    elif 20000 <= population < 100000:
        return 'light goldenrod'
    elif 100000 <= population < 500000:
        return 'light salmon'
    elif 500000 <= population < 1000000:
        return 'tomato'
    elif 1000000 <= population < 3000000:
        return 'red'
    else:
        return 'brown'

def density(population):
    if population < 20000:
        return 2
    elif 20000 <= population < 100000:
        return 3
    elif 100000 <= population < 500000:
        return 4
    elif 500000 <= population < 1000000:
        return 6
    elif 1000000 <= population < 3000000:
        return 8
    else:
        return 10

map = folium.Map(location = [38.58, -99.99], zoom_start=10, tiles="Mapbox Bright")

fgv= folium.FeatureGroup(name="Volcanoes")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    fgv.add_child(folium.RegularPolygonMarker(location=[lt, ln], popup=nm + ", " + str(el) + " m",
                  fill_color=color_producer(el), number_of_sides=3, radius=6, rotation=180))

fgp= folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('../data/world.json', 'r', encoding='utf-8-sig'),
                             style_function=lambda x: {'fillColor':'ivory'
                                            if x['properties']['POP2005'] < 5000000 else 'bisque'
                                            if 5000000 <= x['properties']['POP2005'] < 10000000 else 'sandy brown'
                                            if 10000000 <= x['properties']['POP2005'] < 20000000 else 'chocolate'
                                            if 20000000 <= x['properties']['POP2005'] < 50000000 else 'firebrick'}))

fgc= folium.FeatureGroup(name="US Cities")

for lt, ln, pp, cty in zip(lati, lng, pop, city):
    fgc.add_child(folium.CircleMarker(location=[lt, ln], popup=cty + "\n" + "Population: " + str(pp),
                                      fill_color=color_producer_2(pp), color='white', radius=density(pp),
                                      fill_opacity=0.8))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(fgc)
map.add_child(folium.LayerControl())
map.save("Map1.html")
