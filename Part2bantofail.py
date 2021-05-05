#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 21:02:20 2021

Cal Bigham
COMP 240 -- Computer Applications
Part 2 Presentation 1 SandBox/Work

"""

import pandas as pd
import sys
max_rows = None
max_cols = None
pd.set_option("display.max_rows", max_rows, "display.max_columns", max_cols)
sys.stdout = open('runtimelog', 'w')


def stage2(sourcefile):
    # Read the csv file
    finished = pd.read_csv(sourcefile, names = ['datetime','ip'], parse_dates= True, infer_datetime_format= True)
    # Get Stats from the Dataset
    print('Number of Attempts by IP:')
    valuecount = finished['ip'].value_counts()
    print(valuecount)

    print('\n')
    print('Number of Total IPs and entries')
    numunique = (len(pd.unique(finished['ip'])))
    totalnumber = finished.shape[0]
    print('Total Unique IPs: ' + str(numunique))
    print('Total Entries: ' + str(totalnumber))
    return(finished)
