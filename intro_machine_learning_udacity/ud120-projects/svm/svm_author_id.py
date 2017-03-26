#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

import matplotlib.pyplot as plt
import pylab as pl
import numpy as np

classifier = SVC(kernel = "rbf", C = 10000)

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

t0 = time()
classifier.fit(features_train, labels_train)
print("Time to classify: %.1f" % (time() - t0))

t0 = time()
pred = classifier.predict(features_test)
print("Time to predict: %.1f" % (time() - t0))

acc = accuracy_score(pred, labels_test)

print("Accuracy is %.3f" % acc)

# print pred[10]
# print pred[26]
# print pred[50]

counter = 0
for ii in range(0, len(pred)):
	if pred[ii] == 1:
		counter +=1

print counter



#########################################################
