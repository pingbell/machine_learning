# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:07:52 2020

@author:Shaurya Prakash

"""
import numpy as np
import math

sigma= 6.2
n=150
alpha=.01

z_alpha_by_2_99 = 2.575

error_estimate = z_alpha_by_2_99*sigma/np.sqrt(n)
"""1.30"""


