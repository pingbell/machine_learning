# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:15:26 2020

@author: Shaurya Prakash
"""
import math
import numpy as np
import scipy.stats as stats
CI=.95
sigma=1.6
E = .50

z_alpha_by_2 = (stats.norm.ppf(.975))
var=2.56
esquare=.25

n = (z_alpha_by_2**2)*var/esquare #~40

