import pandas as pd
import plotly as pl
import ipstack as i
from ipstack import GeoLookup

geo_lookup = GeoLookup("004fe3a3435401b81ac4ea493a0834cf")

def stage3(df):
    for a in df.index:
        current_ip = df.loc[a, 'IP']
        location = geo_lookup.get_location(current_ip)
        continent = location["continent_name"]
        country = location["country_name"]
        region = location["region_name"]
        city = location["city"]
        latitude = location["latitude"]
        longitude = location["longitude"]
        df.loc[a, 'continent'] = continent
        df.loc[a, 'country'] = country
        df.loc[a, 'region'] = region
        df.loc[a, 'city'] = city
        df.loc[a, 'latitude'] = latitude
        df.loc[a, 'longitude'] = longitude
    df.to_csv('Stage3.csv')
    return df
        
    
        
        
        
        
    
        
