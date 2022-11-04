#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:09:06 2021

@author: FouadZ
"""
# POISSON REGRESSION: When response variable is a count - Discrete Data

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
import statsmodels
import statsmodels.formula.api as smf
from statsmodels.discrete.discrete_model import Poisson as psn


df = pd.read_csv('counts.csv')

x_train, x_test, y_train, y_test = train_test_split(df.drop('num_awards',axis=1), df['num_awards'], test_size=0.25)

df_train = pd.concat([x_train, y_train], axis=1)
mod1 = psn.from_formula('num_awards~prog+math', data=df_train).fit()


y_pred = mod1.predict(x_test)
y_pred = round(y_pred)

# Try this: 
# y_pred = print(round(mod1.predict(x_test)))

