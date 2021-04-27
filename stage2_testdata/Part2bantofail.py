#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:02:20 2021

Cal Bigham
COMP 240 -- Computer Applications
Part 2 Presentation 1 SandBox/Work

"""

import pandas as pd

# Make the Dataset By Hand

bandict = {'date':[pd.to_datetime('2021-04-06 16:08:17,141'),pd.to_datetime('2021-04-06 16:08:57,864'),
                   pd.to_datetime('2021-04-06 16:09:18,238'),pd.to_datetime('2021-04-06 16:09:39,100'),
                   pd.to_datetime('2021-04-06 16:09:59,778'),pd.to_datetime('2021-04-06 16:10:20,315'),
                   pd.to_datetime('2021-04-06 16:10:40,667'),pd.to_datetime('2021-04-06 16:11:01,018'),
                   pd.to_datetime('2021-04-06 16:11:21,372'),pd.to_datetime('2021-04-06 16:11:41,725')],
           'ip':['117.21.173.4','121.18.238.12','121.18.238.19','121.18.238.20',
                 '121.18.238.22','121.18.238.31','121.18.238.32','121.18.238.6',
                 '121.18.238.7','121.18.238.8']}

ipdataset = pd.DataFrame(data=bandict)
print(ipdataset)

# Get Stats from the Dataset

print('\n')
print('Number of Attempts by IP:')
valuecount = ipdataset['ip'].value_counts()
print(valuecount)

print('\n')
print('Number of Total IPs and entries')
numunique = (len(pd.unique(ipdataset['ip'])))
totalnumber = ipdataset.shape[0]
print('Total Unique IPs: ' + str(numunique))
print('Total Entries: ' + str(totalnumber))