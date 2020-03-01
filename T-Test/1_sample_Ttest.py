# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:24:32 2020

@author: Shaurya Prakash
"""

from scipy import stats 

# given data 
mean = 12
sample =[10,12,20,21,24,18,8]
std_deviation = "unknown"

#since sample is small n<30 ,degree of freedom = n-1=6
print (stats.ttest_1samp(sample,mean))

statistics,pvalue=(stats.ttest_1samp(sample,mean))

print(pvalue)