# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 22:40:30 2020

@author: Shaurya Prakash


A product developer is interested in reducing the drying time of a primer paint.
• Two formulations of the paint are tested; formulation 1 is the standard chemistry, and
formulation 2 has a new drying ingredient that should reduce the drying time.
• From experience, it is known that the standard deviation of drying time is 8 minutes, and this
inherent variability should be unaffected by the addition of the new ingredient.
• Ten specimens are painted with formulation 1, and another 10 specimens are painted with
formulation 2; the 20 specimens are painted in random order.
• The two-sample average drying times are 𝑥1 = 121 minutes and 𝑥2 = 112 minutes,
respectively.
• What conclusions can the product developer draw about the effectiveness of the new
ingredient, using alpha = 0.05?
ho; mean1-mean2=0
h1:mean1>mean2

"""
import numpy as np
import math
import scipy.stats as st

sigma=8
n=10
mean1=121
mean2=112
alpha =0.05

standard_error=sigma*np.sqrt(1/10+1/10)

t= (mean1-mean2)/standard_error
 
zcritical = st.norm.ppf(.95)
""" reject null hypothesis """