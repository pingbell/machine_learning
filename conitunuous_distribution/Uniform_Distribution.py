# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:25:39 2020

@author: Shaurya Prakash
"""
from scipy.stats import uniform

"""
loc - initial position.
scale = loc+other extreme value
x= point at which probability has to be evaluated
"""
probability = uniform.pdf(6,loc=0,scale=10)

cumulative_probability = uniform.cdf(6,loc=0,scale=10)