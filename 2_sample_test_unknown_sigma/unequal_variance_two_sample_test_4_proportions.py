# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:56:00 2020

@author: Shaurya Prakash 
Extracts of St. John’s Wort are widely used to treat depression.
• An article in the April 18, 2001 issue of the Journal of the American Medical
Association (“Effectiveness of St. John’s Worton Major Depression: A
Randomized Controlled Trial”) compared the efficacy of a standard extract
of St. John’s Wort with a placebo in 200 outpatients diagnosed with major
depression.
• Patients were randomly assigned to two groups; one group received the St.
John’s Wort, and the other received the placebo.
• After eight weeks, 19 of the placebo-treated patients showed
improvement, whereas 27 of those treated with St. John’s Wort improved.
• Is there any reason to believe that St. John’s Wort is effective in treating
major depression? Use 0.05.

H0 : p1=p2
H1 : p1!=p2
"""
import numpy as np
import scipy.stats as st
#considering p1=p2

p1=.19
p2=.27
alpha=0.05
pooled_p = (p1*100+p2*100)/(200)
pooled_q = 1-pooled_p
standard_error = np.sqrt(pooled_p*pooled_q*(1/100+1/100))
zscore = (p1-p2)/standard_error
zcritical_lower = st.norm.ppf(.025)
zcritical_upper = st.norm.ppf(.975)

""" accept null """
