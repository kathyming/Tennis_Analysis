#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 17:15:55 2021

@author: FouadZ
"""
# Inferential Statistics Tests for Discrete Data

# One Proportion Test - Test proportion of a sample against a Claim Value
# Sample size will always be a whole number
# Example: min 73% people are vaccinated
# Ho vac >= 0.73
# Ha vac < 0.73 , Sample Size is 300. Vacciated people are 200
# Can the difference between 0.73 and 0.66 be ignored or not

import statsmodels
from statsmodels import stats
from statsmodels.stats import proportion
from statsmodels.stats.proportion import proportions_ztest

# Test statistic and p-value calculation
statsmodels.stats.proportion.proportions_ztest(200,300,0.73,alternative='smaller')

# Since 0.009 < 0.05 therefore Ho is rejected. The difference is statistically
# significant


# Two-Proportion Test - Difference of proportions of 2 independant smaples will
# be compared against a claim value

# Example: Claim: Max Difference of proportions of people vaccinated in US & India
# is 12% ---> Ho: vac(US) - vac(India) <= 0.12
#        ---> Ha: vac(US) - vac(india) > 0.12
# US: 180 of 250 vaccinated /// India: 220 of 400 vaccinated
# 0.72 - 0.55 = 0.1699 is greater than 0.12. Lets check can we ignore this difference or not
import numpy as np
counts = np.array([180,220])
size = np.array([250,400])
# Test Stattistic adn p-value calculation
statsmodels.stats.proportion.proportions_ztest(counts,size,0.12,alternative='larger')
# 0.10 > 0.05 therefore Null Hypothesis is accepted

