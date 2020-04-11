# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:36:37 2020

@author: Shaurya Prakash
"""
import numpy as np
import math
import scipy.stats as st
smple_size=100
sigma=5.1 
mean = 21.6
alpha=.95

print(st.norm.interval(.975,loc=21.6,scale=5.1/np.sqrt(100)))

"""(20.45688460892148, 22.743115391078526)"""