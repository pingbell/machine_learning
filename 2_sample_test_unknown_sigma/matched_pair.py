# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:33:43 2020

@author: HP
MATCHED PAIR :
    
An article in the Journal of Strain Analysis (1983, Vol. 18, No. 2) compares
several methods for predicting the shear strength for steel plate girders.
• Data for two of these methods, the Karlsruhe and Lehigh procedures,
when applied to nine specific girders, are shown in Table .
• We wish to determine whether there is any difference (on the average)
between the two methods.
Table : Strength Predictions for Nine Steel Plate Girders
(Predicted Load/Observed Load)
Girder Karlsruhe Method Lehigh Method Difference dj
S11 1.186 1.061 0.119
S21 1.151 0.992 0.159
S31 1.322 1.063 0.259
S41 1.339 1.062 0.277
S51 1.200 1.065 0.138
S21 1.402 1.178 0.224
S22 1.365 1.037 0.328
S23 1.537 1.086 0.451
S24 1.559 1.052 0.507

H0 : meand = 0
H1 : meand != 0
"""
import numpy as np
import math
import scipy.stats as st

data1 = [1.186,1.151,1.322,1.399,1.200,1.402,1.365,1.537,1.559]
data2 = [1.061,0.992,1.063,1.062,1.065,1.178,1.037,1.086,1.052]
tcritical_upper = st.t.ppf(.975,16)
tcritical_lower = st.t.ppf(.025,16)

tval = st.ttest_rel(data1,data2)[0]
pval = st.ttest_rel(data1,data2)[1]


"""Reject Null """