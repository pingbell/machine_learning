# -*- coding: utf-8 -*-
import numpy as np 
import matplotlib.pyplot as plt
import math
from scipy import stats
 
"""
A machine fills milk bottles, the mean amount of milk in each bottle is supposed to
be 32 Oz with a standard deviation of 0.06 Oz. Suppose the mean amount of milk is
approximately normally distributed. To check if the machine is operating properly, 36
filled bottles will be chosen at random and the mean amount will be determined.


(c). Find the probability of a type II error when the true mean is 32.03.

"""
mu=32
n=36
sigma =0.06
alpha=0.05

"""
(a). If an α = .05 test is used to decide whether the machine is working properly, what
should the rejection criterion be?
"""     
def confidence_interval(aplha) :
    zscore = stats.norm.ppf(0.05) 
    confidence_interval=(mu-zscore*((sigma/np.sqrt(n))),mu+zscore*((sigma/np.sqrt(n))))
    return confidence_interval 
print("anything is not in normal distribution is rejected within confidence interval={}".format(confidence_interval(0.05)))


"""
(b). Find the power of the test if the true mean takes on the following values: 31.97,
31.99, 32, 32.01, 32.03. Draw the power curve.
 """
 