#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 17:28:35 2021

@author: FouadZ
"""

# Import commands
import numpy as np
import scipy
from scipy import stats
from scipy.stats import f

sampA = [5,6,8,4,5,8,4,9]
sampB = [2,3,4,3,5,4,6,3,7]

# test statistic value
# F- Distribution (F-Test Statistic)
F = np.var(sampA)/np.var(sampB) 

#convert to p-value

p_value = (scipy.stats.f.cdf(F,len(sampA)-1, len(sampB)-1))*2
# Degrees of Freedom = len(sampA)-1
# Since p-value is more than 0.05, Null Hypothesis is not rejected
# The ratio of variances can be considered as 1

# Difference between actual ratio can be ignored
# Variance of sampA and sampB can be considered as equal.

# If the p-value is less than 0.05, Null Hypothesis is rejected..
# Difference between actual ration CANNOT be ignored.