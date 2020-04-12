# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:35:40 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
import scipy.stats as st

 

"""
with AC     n = 32 , mean1 = .136 , var1 = .004 
without AC  n = 32 , mean2 = .083 , var2 = .005
alpha=0.05
Ho : mean1 - mean2 = 0.050
H1 : mean1 - mean2 > 0.050
"""
n1 = 32 
mean1 = .136 
var1 = .004**2 
n2 = 32 
mean2 = .083 
var2 = .005**2
alpha=0.05
delta =.050

var = np.sqrt([var1,var2]) # 6.324555320336758268e-02 7.071067811865475172e-02 no pooling

s   = np.sqrt(var1/n1 +var2/n2)
z   = (mean1-mean2-0.050)/s
zcritical = st.norm.ppf(.95)

""" Reject null """

