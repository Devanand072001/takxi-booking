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

import geocoder
g = geocoder.ip('me')
print(g.latlng)