# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:26:59 2021

@author: gabba
"""

import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

def stage4(stg3csv):
    # Read the CSV
    locdata = pd.read_csv(stg3csv)
    for current_ip in locdata['ip']:
        numattempts = (locdata['ip'] == current_ip).sum()
        locdata.loc[locdata['ip'] == current_ip , 'num attempts'] = numattempts
        
    # ensure datetime
    locdata.datetime = pd.to_datetime(locdata.datetime)
    
    # bar graph unique ips by country
    unique_loc = locdata.groupby(by='country',as_index=False).agg({'ip': pd.Series.nunique})
    fig1 = px.bar(unique_loc,x='country',y="ip",labels={'ip':"Unique IP's"},text='ip',title='Unique ip by country')
    fig1.update_traces(texttemplate='%{text:.2s}',textposition='outside')

    # Map plot locations of ip
    fig2 = px.scatter_geo(data_frame = locdata, lat = 'latitude', lon = 'longitude', color = 'continent', size = 'num attempts', hover_name='ip', projection='natural earth')

    # count total ip by week
    locdata_week = locdata.groupby(pd.Grouper(key='datetime',freq='W')).size().reset_index(name='count')
    fig3 = px.bar(locdata_week,x='datetime',y="count",labels={'count':"ip count per week"},text='count',title='Banned count by week')
    fig3.update_traces(texttemplate='%{text:.2s}',textposition='outside')

    # histograme ips banned by time of day
    times = pd.to_datetime(locdata.datetime)
    df_hour = locdata.groupby(times.dt.hour).ip.count()
    fig4 = px.bar(df_hour,y='ip',labels={'ip':"ip count",'datetime':'Hour'},text='ip',title='Banned count by time of day')
    fig4.update_traces(texttemplate='%{text:.2s}',textposition='outside')

    #ips banned by time of day for china
    df_hour_china = locdata[locdata['country'] == 'China'].groupby(times.dt.hour).ip.count()
    fig5 = px.bar(df_hour_china,y='ip',labels={'ip':"ip count",'datetime':'Hour'},text='ip',title='Banned count by time of day: China')
    fig5.update_traces(texttemplate='%{text:.2s}',textposition='outside')

    # same as above but subplot for multiple countries
    #fig6 = make_subplots(rows=2,cols=3)
    #countries = ['China','Finland','United States','Vietnam']

    # Map plot location animation
    locdata['num attempts'] = 1
    df_week = locdata.groupby(['ip',pd.Grouper(key='datetime',freq='W')])['num attempts'].sum().reset_index()
    df_week['cumulative attempts'] = df_week.groupby('ip')['num attempts'].cumsum()
    df_week = pd.merge(left=df_week,right=locdata.drop(columns=['datetime','num attempts']),how='left',on=['ip'])
    df_week = df_week.sort_values(by='datetime')
    df_week['datetime'] = df_week.datetime.apply(lambda x: x.date()).apply(str)
    fig6 = px.scatter_geo(data_frame = df_week, lat = 'latitude', lon = 'longitude', color = 'continent', size = 'cumulative attempts', hover_name='ip',
                          projection='natural earth',animation_frame="datetime",animation_group='country')

    
    fig1.show()
    fig2.show()
    fig3.show()
    fig4.show()
    fig5.show()
    fig6.show()
