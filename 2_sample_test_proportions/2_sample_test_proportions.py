# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:38:10 2020

@author: Shaurya Prakash
"""
import numpy as np
import pandas as pd
from scipy import stats

"""
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

"""
p1 = 27/100
p2 = 19/100 
alpha =0.05
n1=100
n2=100
pooled_prop =  ((p1*n1 + p2*n2)/(n1+n2))
s=np.sqrt(pooled_prop*(1-pooled_prop)*((1/100+1/100)))

def accept_or_reject(alpha,zscore) :
    alpha =alpha/2
    if ((stats.norm.ppf(alpha)>zscore) | (stats.norm.ppf((1-alpha))<zscore)):
       return "reject Ho"
    else :
       return "Accept Ho"

def pvalue(zscore) :
    if ( zscore>0 ):
       return (1-stats.norm.cdf(zscore))*2
    else :
       return (stats.norm.cdf((zscore)))*2
   
def proportion_test(p1,p2) :
    z_score = (p1-p2)/s
    return z_score

z_score = proportion_test(p1,p2)
pvalue  = pvalue(z_score) 
print("pooled prop = {}".format (pooled_prop))
print("pooled variance = {}".format(s))
print("z_score = {}".format(z_score))
print("pvalue = {}".format(pvalue))


