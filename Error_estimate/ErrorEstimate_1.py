# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 14:40:17 2020

@author: Shaurya Prakash


=============================PONT ESTIMATOR=================================

point estimator : from given data we evaluate the error term.

z-alpha_by_2= (X-bar-mu)/(sigma/np.sqrt(n)) known variance

t-alpha_by_2= (X-bar-mu)/(sigma/np.sqrt(n)) with n-1 degree of freedom

Xbar is point estimator.
mu is parameter.
error (bias) = difference between parameter and point estimator.

xbar is unbiased estimator of mu.
sample variance is unbiased estimator of population variance.
sample std is not unbiased estimator of population std.
"""
import pandas as pd
import numpy as np
import math
data=[2.4,2.9,2.7,2.6,2.9,2.0,2.8,2.2,2.4,2.4,2.0,2.5]
sample_mean = round(np.mean(data) ,2)

S_square = np.var(data)*(len(data))/(len(data)-1)
S_std = np.std(data)*(len(data))/(len(data)-1)

error_estimate = 2.201*S_std/(np.sqrt(12))
 


