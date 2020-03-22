# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 13:46:12 2020

@author:Shaurya Prakash
"""
from scipy.stats import binom 

""" 4 coins weere tossed simultaneouly , what is probablility of getting 2 heas?
"""

n=4
p=0.5
x=2

probablity_of_getting_2_heads =  binom.pmf(x,n,p)
probablity_of_getting_atmost_2_heads = binom.cdf(x,n,p)
mean = binom.mean(n,p)
variance = binom.var(n,p)
