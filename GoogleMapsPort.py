import json
import requests

API_key = "&key=AIzaSyDjxQG1nLTRjlCFbVB4mq_jMtu40GMR5D4"
lat = 37.7510
long = -97.8220
radial_dist = 50
API_base_url = "https://maps.googleapis.com/maps/api/"
textsearch = "place/textsearch/json?query="
search_term = input("Enter Search Term: ")
r = requests.get(API_base_url + textsearch + search_term + "&location=" +
                 str(lat) + "," + str(long) + "&radius=" + str(radial_dist)
                 + API_key)
r = r.json()
for i in r["results"]:
    print(i["name"])
