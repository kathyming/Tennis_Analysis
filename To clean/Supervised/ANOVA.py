#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 18:00:50 2021

@author: FouadZ
"""

import pandas as pd

df = pd.read_excel('ANOVA.xlsx')

df.head()

Out[3]: 
  SampleID  Value
0        A     12
1        A     15
2        A     13
3        A     11
4        A     12

import statsmodels

from statsmodels import stats

import statsmodels.api as sm

from statsmodels.formula.api import ols
import statsmodels.stats.multicomp

mod1 = ols('Value ~ SampleID', data=df).fit()

tbl = sm.stats.anova_lm(mod1)

print(tbl)

# For more than 2 interactions
# where difference is not zero and significance 
from statsmodels.stats.multicomp import pairwise_tukeyhsd

comp_tbl = pairwise_tukeyhsd(endog=df['Value'], groups=df['SampleID'], alpha=0.05)

print(comp_tbl)

mod1 = ols('Marks ~ City*Gender', data=df).fit()

tbl = sm.stats.anova_lm(mod1)

print(tbl)
