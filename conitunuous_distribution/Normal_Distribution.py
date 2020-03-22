# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:49:26 2020

@author: Shaurya Prakash
"""
from scipy.stats import norm
import numpy as np

"""
     loc   = mean
     scale = standard deviation
     pdf   = norm.pdf(x,loc,scale)
     
     example : mean = 68.22
     standard deviation = (10.8^.5)
     sample size =1000
     how many soldies are over 72 inces tall
"""
loc=68.22
scale = np
probability = norm.cdf(72,68.22,np.sqrt(10.8))
soldiers_above_six=1-probability

"""
soldiers taller than 72 inches = .1250
"""
