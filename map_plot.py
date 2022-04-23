import webbrowser
import folium
import json
# import pandas as pd
import geocoder
import polyline
import openrouteservice
import os
import convert

g = geocoder.ip('me')

client = openrouteservice.Client(key='5b3ce3597851110001cf6248ef6af4cfbd7147f18189b7aded6b4e64')
coords = ((80.21787585263182,6.025423265401452),(80.23990263756545,6.018498276842677))
res = client.directions(coords)
#set location coordinates in longitude,latitude order

#call API

#test our response

geometry = client.directions(coords)['routes'][0]['geometry']
decoded =  polyline.decode(geometry)

distance_txt = "<h4> <b>Distance :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['distance']/1000,1))+" Km </strong>" +"</h4></b>"
duration_txt = "<h4> <b>Duration :&nbsp" + "<strong>"+str(round(res['routes'][0]['summary']['duration']/60,1))+" Mins. </strong>" +"</h4></b>"
m = folium.Map(location=[6.074834613830474, 80.25749815575348],zoom_start=10, control_scale=True,tiles="cartodbpositron")

# county_path = os.path.join(os.getcwd(),'data', 'test.json') 
# county_geojson = json.load(open(county_path))
# folium.GeoJson(decoded).add_child(folium.Popup(distance_txt + duration_txt,max_width=300)).add_to(m)
 
# folium.GeoJson(
#     # decoded
#      county_geojson,
#     name='geojson'
#     ).add_to(m)

# folium.GeoJson.add_child(folium.Popup(distance_txt+duration_txt,max_width=300)).add_to(m)
folium.GeoJson(decoded).add_to(m).add_child(folium.Popup(distance_txt+duration_txt,max_width=300))

folium.Marker(
    location=list(coords[0][::-1]),
    popup="Galle fort",
    icon=folium.Icon(color="green"),
).add_to(m)

folium.Marker(
    location=list(coords[1][::-1]),
    popup="Jungle beach",
    icon=folium.Icon(color="red"),
).add_to(m)


m.save('map.html')


# class Map:
#     def __init__(self, center, zoom_start):
#         self.center = center
#         self.zoom_start = zoom_start
#         self.showMap()

#     def showMap(self):
#         # Create the map
#         my_map = folium.Map(location=self.center, zoom_start=self.zoom_start)
#         tooltip = "Click me!"
#         folium.Marker(g.latlng,  tooltip=tooltip
#                       ).add_to(my_map)
#         # Display the map
#         my_map.save("static/map.html")
#         # webbrowser.open("static/map.html")


# map = Map(center=g.latlng, zoom_start=5)


# print(map)
