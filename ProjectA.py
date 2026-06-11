import requests
from geopy.distance import geodesic
from Aldi import search_aldi
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from Functions import button_class
from Functions import button_id
from Functions import input_class
import sys
import time

API_KEY = "a78aeebcce1042a3a39ba96e79667666"

##asks for address
print("Enter your address. Example: 1423 Dual Highway, Hagerstown MD 21740")
address = input("Input: ")

# Geocode with Geoapify
geo_resp = requests.get(
    "https://api.geoapify.com/v1/geocode/search",
    params={"text": address, "apiKey": API_KEY}
)
geo_data = geo_resp.json()

while not geo_data["features"]:
    print("Could not find address. Please enter again.")
    address = input("Input: ")
    geo_resp = requests.get(
        "https://api.geoapify.com/v1/geocode/search",
        params={"text": address, "apiKey": API_KEY}
    )
    geo_data = geo_resp.json()

coords = geo_data["features"][0]["geometry"]["coordinates"]
input_lon = coords[0]
input_lat = coords[1]

##radius calculates how far to check
miles = int(input("Enter mile range: "))
MILESTOMETER = 1609
radius_meters = miles * MILESTOMETER

# Find nearby supermarkets with Geoapify
places_resp = requests.get(
    "https://api.geoapify.com/v2/places",
    params={
        "categories": "commercial.supermarket",
        "filter": f"circle:{input_lon},{input_lat},{radius_meters}",
        "limit": 20,
        "apiKey": API_KEY
    }
)
places_data = places_resp.json()

stores = []
for feature in places_data["features"]:
    props = feature["properties"]
    name = props.get("name", "Unnamed Store")
    website = props.get("website", "No website found")
    store_lat = feature["geometry"]["coordinates"][1]
    store_lon = feature["geometry"]["coordinates"][0]
    distance = geodesic((input_lat, input_lon), (store_lat, store_lon)).miles

    stores.append({
        "name": name,
        "lat": store_lat,
        "lon": store_lon,
        "distance_miles": round(distance, 2),
        "website": website
    })

print(stores)

##asks for lookup item to search on stores nearby
print("Enter lookup item")
lookup_item = input("Input: ")

for name in stores:
    if "aldi" in name["name"].lower():
        search_aldi(address, lookup_item)
    else:
        print(f"No {name['name']} available right now.") 