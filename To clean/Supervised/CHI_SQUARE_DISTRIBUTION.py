#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:15:02 2021

@author: FouadZ
""" # Marketting and Service Industry use these a lot. Use Excel to


#CHI SQUARE DISTRIBUTION
#1. Goodness of fit test (one variable)
#2. Degree of association test (two variables)

# GOODNESS OF FIT TEST (1-variable)
# Brands of cars and market share - 4 | A,B,C,D | A- 60%, B-20%, C-15%, D-5%
# Counts obtained from a sample --->    A- 140, B-47, C- 28, D-20 (Total 235)
# Are these counts in same ration as 60%, 20%, 15% and 5%?
actual_counts = [140,47,28,20]
total = sum(actual_counts)
expected_counts = []
share = [0.6, 0.2, 0.15, 0.05]
for ctr in range(len(share)): # how many times will the loop run?
    expected_counts.append(share[ctr]*total) # fill the empty list, what calculation?
    # each value of share mutiplied by total
    # Global Null Hypothesis: Counts follow the pattern claimed

import scipy
from scipy import stats
from scipy.stats import chisquare
scipy.stats.chisquare(actual_counts, expected_counts)
# 0.06 > 0.05 therefore the differences are statistically not significant and can be ignore
#break up the test statistic Contribution = ((Expected - Observed)^2)/Expected
#-----------------------------------------#

# DEGREE OF ASSOCIATION (2-variables)
# Factor = Variable
# Level = Possible values of the variable
# Gender - male/female OR Vaccine - Pfizer/Moderna/JJ
# Does the gender influence the type of vaccine chosen?
# Global Null Hypothesis: V1 has no effect on V2
obs_table = np.array([[130,70,35],[180,145,50]])
from scipy.stats import chi2_contingency
scipy.stats.chi2_contingency(obs_table)
# (test statistic, p-value, dof for the table, array[expected value for true H0] )
# DOF for table = (no of rows-1) X (no of cols-1) #Degree of Freedom
# Test Statistic = Sum of all expected values 