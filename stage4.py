# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:26:59 2021

@author: gabba
"""

import plotly.express as px
import pandas as pd

def stage4(stg3csv):
    # Read the CSV
    locdata = pd.read_csv(stg3csv)
    for current_ip in locdata['ip']:
        numattempts = (locdata['ip'] == current_ip).sum()
        locdata.loc[locdata['ip'] == current_ip , 'num attempts'] = numattempts
    fig = px.scatter_geo(data_frame = locdata, lat = 'latitude', lon = 'longitude', color = 'continent', size = 'num attempts', hover_name='ip', projection='natural earth')
    fig.show()
    