# Install and Import Packages
import requests
import pandas as pd
import numpy as np
import re
import geopandas as gpd
import matplotlib.pyplot as plt
import urllib.parse
import os
import requests
import time
import pandas as pd
from geopy.geocoders import GoogleV3

# pip install -q -U googlemaps
import googlemaps
import pandas as pd

# Authenticate with Google Maps API with API Key
api_key = "AIzaSyBqpXVgyXNwPZZx71Gzgtpg_tf3GFWcoMQ"
gmaps = googlemaps.Client(key=api_key)

# Load in the Datasets
# Load the dataset
addresses_df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/fulldata_assignment7_slim_hospital_addresses.csv')
addresses_df

# Load the dataset
coordinates_df = pd.read_csv('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/fulldata_assignment7_slim_hospital_coordinates.csv')
coordinates_df

# Randomly select 100 rows from each dataset
addresses_sample = addresses_df.sample(n=100, random_state=42)
addresses_df

# Randomly select 100 rows from each dataset
coordinates_sample = coordinates_df.sample(n=100, random_state=42)
coordinates_sample

# Geocoding
geocoded_addresses = []

for index, row in addresses_sample.iterrows():
    address = row['ADDRESS']
    geocode_result = gmaps.geocode(address)

    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        lat, lng = location['lat'], location['lng']
        geocoded_addresses.append({'ADDRESS': address, 'Latitude': lat, 'Longitude': lng})

geocoded_df = pd.DataFrame(geocoded_addresses)
geocoded_df

# Reverse Geocoding 
reverse_geocoded_addresses = []

for index, row in coordinates_sample.iterrows():
    lat = row['X']
    lng = row['Y']
    reverse_geocode_result = gmaps.reverse_geocode((lat, lng))

    if reverse_geocode_result:
        address = reverse_geocode_result[0]['formatted_address']
        reverse_geocoded_addresses.append({'X': lat, 'Y': lng, 'Address': address})

reverse_geocoded_df = pd.DataFrame(reverse_geocoded_addresses)
reverse_geocoded_df