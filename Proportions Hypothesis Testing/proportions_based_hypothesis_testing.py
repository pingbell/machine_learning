# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:39:24 2020

@author: Shaurya Prakash
"""

import numpy as np
from statsmodels.stats.proportion import proportions_ztest
count = np.array([5, 12])
nobs = np.array([83, 99])
stat, pval = proportions_ztest(count, nobs)
print('{0:0.3f}'.format(pval))
