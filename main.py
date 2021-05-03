#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:07:45 2021

@author: calbigham
"""
import stage1 as s1
import Part2bantofail as s2
import FixedStage3 as s3
#import stage4 as s4

import pandas as pd
import sys


max_rows = None
max_cols = None
pd.set_option("display.max_rows", max_rows, "display.max_columns", max_cols)
sys.stdout = open('runtimelog', 'w')

# Main Function: Pulling it all together

s1.stage1()
dataframe1 = s2.stage2('stage1_output.csv')
s3.stage3(dataframe1)
#s4.stage4('Stage3.csv')