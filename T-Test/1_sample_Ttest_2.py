# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 22:21:59 2020

@author: Shaurya Prakash

h0 : service time <= 20 min
h1 : service time > 20 minutes
alpha = .10  (two tailed test.)

"""
from scipy import stats
import numpy as np 

ambulance_arrival_time =[27,15,20,32,18,26]
tvalue , pvalue = stats.ttest_1samp(ambulance_arrival_time,20)
t_alpha = stats.t.ppf(.90,5)

def accept_or_reject (t_alpha,tvalue) :
    if (tvalue > t_alpha) :
        return ("reject")
    else :
        return ("accept")
print(accept_or_reject (t_alpha,tvalue))