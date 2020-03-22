#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 16:26:50 2020

@author: dell
"""

import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import pandas as pd

 

df1 = pd.read_csv('MCC.tsv', sep = "\t")
df1 = df1.sort_values(by=['MCC'])
x = df1['F1'].to_numpy()

# create data
#x = np.random.rand(40)
y = df1['Sero'].to_numpy()

z = df1['PFGEs'].to_numpy()
k = df1['samples'].to_numpy()
 
# use the scatter function

fig = plt.figure(figsize = (10,12))
"""
plt.scatter(x, y, s=z*10,c = z ,alpha=0.5)

plt.show()
"""

sns.set_style("white")
cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)

ax = sns.scatterplot(x=x, y=y, hue=k, size=z,sizes = (20,600), palette = cmap,data=df1, legend = None)
ax.set_title("F-1 scores sized by number of PFGE classes and coloured by number of samples")
ax.set(xlabel='F-1', ylabel='Serogroup')













