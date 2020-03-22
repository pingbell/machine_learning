# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 15:49:24 2020

@author: Shaurya Prakash
"""
from scipy.stats import hypergeom 
import numpy as np

"""

Different computers are checked from 10 in the department. 4 of the 10
computers have illegal software loaded.

What is the probability that 2 of the 3 selected computers have illegal
software loaded?

"""
x_defective = 2

M_total_defective =4

n_sample_size =3

N_Total_size =10

"""
rv = hypergeom(Total_objects,Total_One_type,Sample_Size)
pmf =rv.pmf([list of integers])
pmf=[list of corresponding probablilities]
"""
rv = hypergeom(N_Total_size,M_total_defective,n_sample_size)
probablity = rv.pmf(np.arange(1,4))

