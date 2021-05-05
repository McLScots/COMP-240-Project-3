import pandas as pd
import plotly as pl
import ipstack as i
from ipstack import GeoLookup

geo_lookup = GeoLookup("ef0cd3eb3df26d42fd82ff1586b7dd04")

def stage3(df):
    uniques = pd.unique(df['ip'])
    for current_ip in uniques:
        location = geo_lookup.get_location(current_ip)
        continent = location["continent_name"]
        country = location["country_name"]
        region = location["region_name"]
        city = location["city"]
        latitude = location["latitude"]
        longitude = location["longitude"]
        df.loc[df['ip'] == current_ip ,'continent'] = continent
        df.loc[df['ip'] == current_ip , 'country'] = country
        df.loc[df['ip'] == current_ip , 'region'] = region
        df.loc[df['ip'] == current_ip , 'city'] = city
        df.loc[df['ip'] == current_ip , 'latitude'] = latitude
        df.loc[df['ip'] == current_ip , 'longitude'] = longitude
    df.to_csv('Stage3.csv')
    return df
        
    
        
        
        
        
    
        
