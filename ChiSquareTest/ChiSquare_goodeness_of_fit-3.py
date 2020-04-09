# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:35:36 2020

@author: HP
"""


import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
data = pd.read_csv("E:\\DATASETS\\iriscsv\\Iris.csv")
 
data['SepalWidthCm'] = data['SepalWidthCm'].apply(lambda x: 0 if (x<=3.0) else 1)

table = pd.pivot_table(data[['Species','SepalWidthCm']],index='Species',columns='SepalWidthCm',aggfunc=len)
l1=list(data['SepalWidthCm'])
l2=list(data['Species'])
 
test_Independece =  stats.chi2_contingency(table)

Fcritical = stats.chi2.ppf(.99,1)



"""Reject null hypothesis """