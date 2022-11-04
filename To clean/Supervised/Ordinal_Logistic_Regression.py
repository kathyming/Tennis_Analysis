#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 18:00:40 2021

@author: FouadZ
"""
# LOGICAL ORDER TO RESPONSE - Ordinal Logistic Regression

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression

import sys
sys.path.append(r 'C:\Users\mord-0.6') # Fix this line
import mord
from mord import LogisticAT

df = pd.read_csv('regr_models.csv')

x_train, x_test, y_train, y_test = train_test_split(df.drop('Survival',axis=1), df['Survival'], test_size=0.25)

ord_regr = LogisticAT().fit(x_train, y_train)

y_pred = ord_regr.predict(x_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

