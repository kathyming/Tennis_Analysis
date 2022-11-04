#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 17:33:45 2021

@author: FouadZ
"""
##                     BINARY LOGISTIC REGRESSION
# Response = Attribute Data and Only Binary Data - Yes or No

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import linear_model
from sklearn.linear_model import LogisticRegression

# Open file to read
df = pd.read_csv('diabetes.csv')

# Split the file
x_train, x_test, y_train, y_test = train_test_split(df.drop('Outcome',axis=1), df['Outcome'], test_size=0.25)
# X is predictors Y is response

# Create Model
bin_regr = LogisticRegression()
bin_regr.fit(x_train, y_train)

# Make Prediction
y_pred = bin_regr.predict(x_test)

# Confusion Matrix && Classification Report
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

# [107  15]
# [ 32  38]]

# first row - actual value = 0
# second row - actual value = 1
#
# first column predicted value = 0
# second column predicted value = 1
# Correct predications = 107+38 = 145
# False predictions = 15 +32 = 47
# Total predictions = 145 + 47 = 192
# % accuracy = 0.755

# Precision and Recall
# TN - 107  FP - 15  FN - 32  TP - 38
# PRECISION = TP/(TP+FP)
# RECALL = TP/(TP+FN)
