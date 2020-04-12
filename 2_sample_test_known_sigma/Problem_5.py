# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 14:01:23 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
import scipy.stats as st

 

"""
with AC     n = 40 , mean1 = 1647 , var1 = 27**2 
without AC  n = 40 , mean2 = 1638 , var2 = 31**2
alpha=0.05
Ho : mean1 - mean2 <= 0
H1 : mean1 - mean2 > 0
"""""
n1 = 40.0 
mean1 = 1647.0 
var1 = 27.0**2 
n2 = 40.0 
mean2 = 1638.0 
var2 = 31.0**2

std_error = np.sqrt(var1/n1+var2/n2)
bias = mean1-mean2

z =bias/std_error

p_value=st.norm.cdf(-z)

zcritical = st.norm.ppf(.95)

CI = st.norm.interval(.95,loc=9,scale=std_error)
""" accept null """