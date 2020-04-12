# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 13:21:04 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
import scipy.stats as st

"""
with AC     n = 45 , mean1 = 204.4 , var1 = 13825.3 
without AC  n = 55 , mean2 = 130.0 , var2 = 8632.0
Ho : mean1=mean2
H1:mean1 != mean2
"""
n1 = 45 
mean1 = 204.4 
var1 = 13825.3 
n2 = 55 
mean2 = 130.0 
var2 = 8632.0

std1= np.sqrt(13825.3)
std2= np.sqrt(8632)
#NO pooling

standard_error = np.sqrt(var1/n1 + var2/n2)
bias = (mean1-mean2) -0 

interval=st.norm.interval(.95,loc=(mean1-mean2),scale =standard_error )

"""
interval does not contains zero , hence reject null hypothesis
(32.17, 116.62)
"""