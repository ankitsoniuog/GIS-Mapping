#!/usr/bin/env python
# coding: utf-8

# In[15]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
#geopandas for working with geospatial data.
#pandas for working with tabular data, including CSV files.
#matplotlib.pyplot for creating plots.

# This code loads the shapefile using geopandas.read_file() and stores it in the variable gdf_india. 
# Adjust the shapefile_path to the actual path of your shapefile.
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
excel_file_path = r'D:\python\GIS Plotting\Economic_Data.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='Economic_18-19', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Per Capita Income (INR) in Different Indian States, Year 18-19', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[9]:


import geopandas as gpd
import matplotlib.pyplot as plt
from adjustText import adjust_text

# Load the shapefile with India's geometrical and attribute data
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'
gdf_india = gpd.read_file(shapefile_path)

# Project the geometries to a suitable projected CRS (e.g., UTM)
gdf_india = gdf_india.to_crs(epsg=3395)  # Use the appropriate EPSG code for your region

# Plot the map with different colors for each state
fig, ax = plt.subplots(figsize=(15, 10))
gdf_india.boundary.plot(ax=ax, linewidth=1.2)
gdf_india.plot(column='st_nm', cmap='Set3', ax=ax, edgecolor='black', legend=False)

# Add state names as labels with adjusted positions to avoid overlap
texts = []
for x, y, label in zip(gdf_india.geometry.centroid.x, gdf_india.geometry.centroid.y, gdf_india['st_nm']):
    texts.append(plt.text(x, y, label, fontsize=8, ha='center', va='center'))

# Adjust text labels to avoid overlap
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))

# Add labels and title
ax.set_title('Indian Map with State Names', fontdict={'fontsize': '15', 'fontweight' : '3'})

# Show the plot
plt.show()


# In[6]:


pip install adjustText


# In[41]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 

excel_file_path = r'D:\python\GIS Plotting\Economic_Data.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='Economic_20-21', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Per Capita Income (INR) in Different Indian States, Year 20-21', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[20]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
excel_file_path = r'D:\python\GIS Plotting\Population_Data.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='TotalPopulation', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Population in Different Indian States, Year 22-23', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[24]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
excel_file_path = r'D:\python\GIS Plotting\Population_Data.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='UrbanPopulationPercentage', cmap='Purples', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Urban Population Percentage in Different Indian States, Year 22-23', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[26]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
excel_file_path = r'D:\python\GIS Plotting\Population_Data.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='RuralPopulationPercentage', cmap='Greens', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Rural Population Percentage in Different Indian States, Year 22-23', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[40]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
excel_file_path = r'D:\python\GIS Plotting\TapWaterConnection.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='Total Household', cmap='BuPu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Variation in the Total Number of Households', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[27]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
#Adjust the csv_path to the actual path of your CSV file.
excel_file_path = r'D:\python\GIS Plotting\TapWaterConnection.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='TapWaterSupplyHouseholds(%)2019', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Tap Water Connection Percentage in Different Indian States, 2019', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[35]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

#Here, we import the necessary libraries:
shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 
excel_file_path = r'D:\python\GIS Plotting\TapWaterConnection.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

# Merge the tap water supply data with the India map data based on state names
merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')

# Plot the map
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='TapWaterSupplyHouseholds(%)2023', cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
# These lines add a title to the plot and turn off the axis to create a cleaner visualization.
ax.set_title('Tap Water Connection Percentage in Different Indian States, 2023', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[2]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt


shapefile_path = r'D:\python\GIS Plotting\india-polygon.shx'


excel_file_path = r'D:\python\GIS Plotting\Water_Future_in_India.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)


merged_data = india_map.merge(df, left_on='st_nm', right_on='State', how='left')


fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='WaterLevel', cmap='Reds', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot

ax.set_title('Water Future in India', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[4]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


shapefile_path = r'D:\python\GIS Plotting\Map_Files\India_Districts.shx'


excel_file_path = r'D:\python\GIS Plotting\Water_Future_in_India.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)


merged_data = india_map.merge(df, left_on='Dist_Name', right_on='District', how='left')

# Create a custom colormap based on per capita water availability categories
colors = ['darkred', 'lightblue', 'firebrick', 'lightcoral']  # Dark Red, Light Red, Dark Red, White
cmap = ListedColormap(colors)


fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='WaterLevel2025', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot
ax.set_title('India Water Future 2025 (Per Capita Water Availability)', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[3]:


import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


# This code loads the shapefile using geopandas.read_file() and stores it in the variable gdf_india. 

shapefile_path = r'D:\python\GIS Plotting\Map_Files\India_Districts.shx'

#This code loads the CSV file containing tap water connection data using pandas.read_csv() and stores it in the variable df_tap_water. 

excel_file_path = r'D:\python\GIS Plotting\Water_Future_in_India.xlsx'

# Read data from Excel into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Read the shapefile for India
india_map = gpd.read_file(shapefile_path)

merged_data = india_map.merge(df, left_on='Dist_Name', right_on='District', how='left')

# Create a custom colormap based on per capita water availability categories
colors = ['darkred', 'lightblue', 'firebrick', 'lightcoral']  # Dark Red, Light Red, Dark Red, White
cmap = ListedColormap(colors)

# Plot the map

fig, ax = plt.subplots(1, 1, figsize=(15, 10))
merged_data.plot(column='WaterLevel2050', cmap=cmap, linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Customize the plot

ax.set_title('India Water Future 2050 (Per Capita Water Availability)', fontdict={'fontsize': '20', 'fontweight' : '3'})
ax.set_axis_off()

# Display the plot
plt.show()


# In[ ]:




