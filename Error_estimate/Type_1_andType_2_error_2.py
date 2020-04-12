# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:58:44 2020

@author: Shaurya Prakash

mu=12
mu<12
sigma=.10
n=60
evaluate type 2 error for mu=11.99
"""
import scipy.stats as st
import numpy as np
import math
sigma=.10
n=60
Z_alpha = -st.norm.ppf(.05)

max_error =  Z_alpha * sigma/np.sqrt(60)

Xvalue = 12 - max_error

Zvalue = (Xvalue - 11.99)*np.sqrt(60)/sigma

beta  = 1-st.norm.cdf(Zvalue)

