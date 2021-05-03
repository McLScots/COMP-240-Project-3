# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 21:26:59 2021

@author: gabba
"""

import matplotlib.pyplot as plt

x= [ 115.9,120.2,-56.2,102.6,102.6,118.8,
    118.8,25.1,25.1,-117.9]
y= [28.7,30.2,-34.9,24.8,24.8,
    32,32,60.4,60.4,34]

plt.hist(x)

plt.xlabel("Longitude")
plt.ylabel('Latitude')
plt.title("Geographic coordinates of Ip Address")

plt.show()