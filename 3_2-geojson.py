import pandas as pd
import matplotlib.pyplot as plt #if using matplotlib
import geopandas as gpd
import geopy.distance
import datetime
import numpy as np
from shapely.geometry import Point, Polygon, shape 
import math
import random 

df_segments = pd.read_csv(r'segment_table_TO.csv')

# df_segments = df_segments[:30]

#%%
minLat = 44.96282106687191
minLon = 7.502048016422193
maxLat = 45.19265016665321 
maxLon = 7.791812422724604

#%%
# dy = dx = 200/1000 #squares of 200 meters width and height
r_earth = 6378.137 #km
pi = math.pi
df_geojson = pd.DataFrame()
df_geojson['polygon_id'] = df_geojson['polygon'] = ""
df_data = pd.DataFrame()
#%%
# shiftInMeterLat = 0.0017966305682364236 # 200m in adad az ekhtelaf lat ghabli va lat shift shode bedast miad
# shiftInMeterLon = 0.002541289066976482

# shiftInMeterLat = 0.00017966305682364236 # 20m
# shiftInMeterLon = 0.0002541289066976482

# shiftInMeterLat = 0.0004491576420591059 #50m
# shiftInMeterLon = 0.0006353222667438985

shiftInMeterLat = 0.0008983152841182118 #100m
shiftInMeterLon = 0.001270644533487797

# shiftInMeterLat = 0.0035932611364799527 # 400m
# shiftInMeterLon = 0.005082578133952076

range_lat = (maxLat - minLat)/shiftInMeterLat 
range_lon = (maxLon - minLon)/shiftInMeterLon
coords={}
minLonCopy = minLon
#creating cells
for i in range(math.ceil(range_lat)):
    minLon = minLonCopy
    new_latitude  = minLat + shiftInMeterLat
    for j in range(math.ceil(range_lon)):
        new_longitude = minLon + shiftInMeterLon
        coords[f'{i+1}_{j+1}'] = [[minLon,minLat],[new_longitude,minLat],
        [new_longitude,new_latitude],[minLon,new_latitude]]
        minLon = new_longitude  
    minLat = new_latitude    
#%%
df_geojson['polygon_id']=coords.keys()
df_geojson['polygon'] = coords.values()
df_geojson['polygon'] = df_geojson['polygon'].apply(Polygon)

df_data['id'] = coords.keys() 
#%%
# df_geojson['polygon'] = gpd.GeoSeries.from_wkt(df_geojson['polygon'])
gdf = gpd.GeoDataFrame(df_geojson, geometry='polygon',crs="EPSG:4326")
#%%
# gdf.plot(figsize=(20, 10))
# gdf.to_file("temp_coord.shp")
# gdf.to_file('100m/coords_TO.geojson',driver="GeoJSON")  
df_data['count'] = 0
df_data.to_csv('100m/data_TO.csv',index=False)