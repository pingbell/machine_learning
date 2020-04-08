# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:55:40 2020

@author: Shaurya Prakash
"""
import pandas as pd 
import numpy as np
import scipy as statistics

data = pd.read_excel("C:\\Users\\HP\\Desktop\\data_analytics_with_python\\Important_Data\\acad.xlsx")
table = pd.pivot_table(data[['sm','g']],index='g',columns='sm',aggfunc=len)
result= statistics.stats.chi2_contingency(table)
chi2,p,dof,tbl=result
