# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 15:29:09 2020

@author: Shaurya Prakash
"""
import numpy as np
import math

import scipy.stats as stat
n=6
std=.14
CI =.98
mean = 232.26

""" if sample mean is used to estimate error """

error = stat.t.ppf(.99,5)

