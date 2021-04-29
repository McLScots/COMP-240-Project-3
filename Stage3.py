import pandas as pd
import plotly as pl
import ipstack as i
from ipstack import GeoLookup

geo_lookup = GeoLookup("004fe3a3435401b81ac4ea493a0834cf")

def stage3(df):
    for a in df.index:
        current_ip = df.loc[a, 'ip']
        location = geo_lookup.get_location(current_ip)
        continent = location["continent_name"]
        country = location["country_name"]
        region = location["region_name"]
        city = location["city"]
        latitude = location["latitude"]
        longitude = location["longitude"]
        df['continent'] = continent
        df['country'] = country
        df['region'] = region
        df['city'] = city
        df['latitude'] = latitude
        df['longitude'] = longitude
        return df
    pd.to_csv('Stage3.csv')
    
        
        
        
        
    
        
