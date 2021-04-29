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
import subprocess
max_rows = None
max_cols = None
pd.set_option("display.max_rows", max_rows, "display.max_columns", max_cols)
sys.stdout = open('step2log', 'w')


def csvtoframe(sourcefile):
    # Read the csv file
    finished = pd.read_csv(sourcefile, names = ['datetime','ip'], parse_dates= True, infer_datetime_format= True)
    return(finished)

# Get Stats from the Dataset

bandict = csvtoframe('/Users/calbigham/Documents/MonmouthCollege/Year2/Semester 2/COMP240/COMP240Project3/stage1_output.csv')
print(bandict)
print('\n')
print('Number of Attempts by IP:')
valuecount = bandict['ip'].value_counts()
print(valuecount)

print('\n')
print('Number of Total IPs and entries')
numunique = (len(pd.unique(bandict['ip'])))
totalnumber = bandict.shape[0]
print('Total Unique IPs: ' + str(numunique))
print('Total Entries: ' + str(totalnumber))

## Open the log file for bells and whistles
log = '/Users/calbigham/Documents/MonmouthCollege/Year2/Semester 2/COMP240/COMP240Project3/stage2_testdata/step2log'
textviewerpath = '/System/Applications/TextEdit.app/Contents/MacOS/TextEdit'
subprocess.Popen([textviewerpath,log])