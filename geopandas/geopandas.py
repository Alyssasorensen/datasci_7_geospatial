pip install geopandas
pip install matplotlib
pip install folium

import geopandas as gpd
import matplotlib.pyplot as plt
import folium
import numpy as np

# First Dataset
df_gpd = gpd.read_file('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/Grocery_Stores.csv')
df_gpd

# Replace empty strings or non-numeric values with NaN
df_gpd['Better_Lat'] = df_gpd['Better_Lat'].apply(lambda x: np.nan if x == '' else x)
df_gpd['Better_Long'] = df_gpd['Better_Long'].apply(lambda x: np.nan if x == '' else x)

# Remove rows with missing or non-numeric values in the 'Better_Lat' and 'Better_Long' columns
df_gpd = df_gpd[df_gpd['Better_Lat'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]
df_gpd = df_gpd[df_gpd['Better_Long'].apply(lambda x: str(x).replace('.', '', 1).isdigit())]

# Now, we convert the columns to float
df_gpd['Better_Lat'] = df_gpd['Better_Lat'].astype(float)
df_gpd['Better_Long'] = df_gpd['Better_Long'].astype(float)
df_gpd

# Create a basic map plot
df_gpd.plot(figsize=(12, 8))
plt.title("Geospatial Data Visualization")
plt.show()

m = folium.Map(location=[42.373652, -83.162775], zoom_start=10)

# Add markers to the map based on your dataset
for index, row in df_gpd.iterrows():
    folium.Marker([row['Better_Lat'], row['Better_Long']], tooltip=row['Common_Name']).add_to(m)

m.save('folium_map.html')