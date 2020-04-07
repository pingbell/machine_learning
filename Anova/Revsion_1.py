# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:04:09 2020

@author: shaurya prakash
"""

import numpy as np
import pandas as pd
import scipy.stats as stats

"""
E = 0.05
Z=1.645
calculate the sample size?
"""
interval = np.abs(stats.norm.interval(.90)[0])
sample_size = (interval**2 )*(.5*.5)/(0.05)**2

"""
E =0.03
P =.40
alpha = .02
"""
interval1 = (np.abs(stats.norm.interval(.98)[0])**2)*(.4*.6)/(0.03)**2