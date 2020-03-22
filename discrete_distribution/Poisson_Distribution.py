# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 14:08:40 2020

@author: Shaurya Prakash
"""
from scipy.stats import poisson

mu = 4 #accidents/year
x = 4 

probablity = poisson.pmf(x,mu)

probablity_less_than_4_accidents = poisson.cdf(3,mu)


 

