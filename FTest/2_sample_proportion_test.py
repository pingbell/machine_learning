# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 08:40:56 2020

@author: Shaurya Prakash
"""
import numpy as np
from scipy import stats 
import matplotlib.pyplot as plt 
sample1 = np.arange(1,11,1)
sample2 = np.arange(11,21,1)
sample3 = np.arange(21,31,1)
sample4 = np.arange(31,41,1)

boxplot_data = [sample1,sample2,sample3,sample4]
plt.boxplot(boxplot_data)
plt.show()

anova = stats.f_oneway(sample1,sample2,sample3,sample4)
print(anova)