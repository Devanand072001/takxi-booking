import webbrowser
import folium
# import pandas as pd
import geocoder
g = geocoder.ip('me')


class Map:
    def __init__(self, center, zoom_start):
        self.center = center
        self.zoom_start = zoom_start
        self.showMap()

    def showMap(self):
        # Create the map
        my_map = folium.Map(location=self.center, zoom_start=self.zoom_start)
        tooltip = "Click me!"
        folium.Marker(g.latlng,  tooltip=tooltip
                      ).add_to(my_map)
        # Display the map
        my_map.save("templates/map.html")
        webbrowser.open("templates/map.html")


map = Map(center=g.latlng, zoom_start=5)


print(map)
