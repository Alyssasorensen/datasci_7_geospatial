import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

## Loading dataset
df1 = gpd.read_file('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/Technology_Access_Computers_-_2017-2021_-_ACS_-_TempeTracts___.geojson')
df1.sample(5) ## Previewing a sample of 5 rows from the dataset

df1.plot('Total_households', legend=True)

### Summary

# This dataset provides details on technology access across Arizona, encompassing information such as types of technology. This includes tablets, smartphones, and laptops. 

# According to the map legend, the color scale ranges from purple to yellow, where purple indicates lower access percentages and yellow indicates higher percentages.

# Dobson Shores boasts the highest technology access percentage, whereas Guadalupe showcases the lowest technology access percentage.

## Loading dataset
df2 = gpd.read_file('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/National_Obesity_By_State.geojson')
df2.sample(5) ## Previewing a sample of 5 rows from the dataset

## Removing "Hawaii" from dataset as it contains 'None' in the geometry column in order to create the interactive map below.
remove = df2['NAME'] == 'Hawaii'
df2 = df2[~remove]

df2.plot('Obesity', legend=True)

### Summary

# This dataset provides details on obesity percentages across U.S. states, encompassing information such as state names, obesity rates, and geospatial data.

# According to the map legend, the color scale ranges from purple to yellow, where purple indicates lower obesity percentages and yellow indicates higher percentages.

# Louisiana boasts the highest obesity percentage, registering at 36.2, whereas Colorado showcases the lowest obesity rate at 20.2.

## Loading dataset
df3 = gpd.read_file('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/Cancer_Rates%20(1).geojson')
df3.sample(5) ## Previewing a sample of 5 rows from the dataset

print('Visualization of rates of all cancer by zipcode in Libertyville, Illinois')
df3.plot('All_Cancer', legend=True)

### Summary

# This dataset comprises data on cancer rates specific to Libertyville, Illinois. Included cancer types in the dataset encompass colorectal cancer, lung cancer, breast cancer, prostate cancer, urinary system cancer, and the overall cancer rate.

# The visualization focused on the "All_Cancer" column to examine comprehensive cancer rates, organized by zip codes. In each map, a deeper color signifies a lower rate, whereas a lighter color indicates a higher rate.

# The lowest rate is observed in Zipcode 60085, recording a value of 1465.294184. Conversely, the highest rate is identified in Zipcode 60069, reaching a value of 4505.481267.

## Loading dataset
df4 = gpd.read_file('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/Hospitalization_Discharge_Rates.geojson')
df4.sample(5) ## Previewing a sample of 5 rows from the dataset

df4.plot('Asthma', legend=True)

## Summary 

# This dataset encompasses details regarding hospitalization rates for asthma in Lake County, Illinois, categorized by zip code. The information includes rates per 100,000 population for various health conditions and hospital discharge rates.

# The map above visualizes the "Asthma" column, which provides details on hospital asthma rates, organized by zip code.

# According to the map legend, the color scale ranges from purple to yellow, where purple signifies a lower discharge rate, and yellow signifies a higher discharge rate. Zipcode 60020 exhibits the highest discharge rate, recording a value of 13394.28, while zipcode 60089 displays the lowest discharge rate, with a value of 7512.07.

## Loading dataset
df5 = gpd.read_file('https://raw.githubusercontent.com/Alyssasorensen/datasci_7_geospatial/main/datasets/Birth_Statistics.geojson')
df5.sample(5) ## Previewing a sample of 5 rows from the dataset

print('Birth rates by zipcode in Chicago, Illinois')
df5.plot('Birth_Rate', legend=True)

## Summary

# This dataset includes data on birth rates in Chicago, Illinois, organized by ZIP Code. The information encompasses rates for low birth weight, preterm birth, teen birth, overall birth rate, and the provision of first-trimester care.

# The map visualized the "Birth_Rate" column, portraying the comprehensive birth rates defined as the number of live births per 1,000 populations. The data is organized by ZIP codes, and in each map, a darker color signifies a lower rate, while a lighter color indicates a higher rate.

# The lowest rate is observed in Zipcode 60010, recording a value of 3.219561. Conversely, the highest rate is identified in Zipcode 60085, reaching a value of 18.080633.
