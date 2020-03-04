# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 17:39:24 2020

@author: Shaurya Prakash
"""

import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
population = 1018
porportion_Null_Hypothesis = .52
proportion_Alternative_Hypothesis = .56

z_stat ,p_value=( sm.stats.proportions_ztest(proportion_Alternative_Hypothesis * population , population,porportion_Null_Hypothesis , alternative='larger'))