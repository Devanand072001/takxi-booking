# import geocoder
# import socket
# import requests
# # ip = socket.gethostbyname(socket.gethostname())
# # g = geocoder.freegeoip(ip)
# # g.json


# from requests import get

# ip = get('https://api.ipify.org').text

# def get_ip():
#     response = requests.get('https://api64.ipify.org?format=json').json()
#     return response["ip"]


# def get_location():
#     ip_address = ip
#     response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
#     location_data = {
#         "ip": ip_address,
#         "city": response.get("city"),
#         "region": response.get("region"),
#         "country": response.get("country_name"),
#         "latitude": response.get("latitude"),
#         "longitude": response.get("longitude")
#     }
#     return location_data


# print(get_location())

# import geocoder
# g = geocoder.ip('me')
# print(g.latlng[0])

# import requests
# import urllib.parse

# bang_add = 'Bangalore'
# url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(bang_add) +'?format=json'

# response = requests.get(url).json()
# print(response[0]["lat"])
# print(response[0]["lon"])

# chen_add = 'Chennai '
# url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(chen_add) +'?format=json'

# response = requests.get(url).json()
# print(response[0]["lat"])
# print(response[0]["lon"])

import osmnx as ox
import networkx as nx
ox.config(log_console=True, use_cache=True)
# define the start and end locations in latlng
start_latlng = (37.78497, -122.43327)
end_latlng = (37.78071, -122.41445)
# location where you want to find your route
place = 'San Francisco, California, United States'
# find shortest route based on the mode of travel
mode = 'walk'        # 'drive', 'bike', 'walk'
# find shortest path based on distance or time
optimizer = 'time'        # 'length','time'
# create graph from OSM within the boundaries of some
# geocodable place(s)
graph = ox.graph_from_place(place, network_type=mode)
# find the nearest node to the start location
orig_node = ox.get_nearest_node(graph, start_latlng)
# find the nearest node to the end location
dest_node = ox.get_nearest_node(graph, end_latlng)
#  find the shortest path
shortest_route = nx.shortest_path(graph,
                                  orig_node,
                                  dest_node,
                                  weight=optimizer)

shortest_route_map = ox.plot_route_folium(graph, shortest_route)
