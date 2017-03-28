#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

#General libraries
import sys
from time import time
sys.path.append("../tools/")
from sklearn.naive_bayes import GaussianNB

#Local libraries
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###

def classifyNB(features_train, labels_train):
	"""
		Classifies a dataset along with a training set according to Naive-Bayes
	"""

	classifier 	= GaussianNB()

	startTime 	= time()
	classifier.fit(features_train, labels_train)
 	timeSpent = time() - startTime

	return classifier, timeSpent

def predictNB(classifier, features_test):
	"""
		Predicts a dataset
	"""
	startTime 	= time()
	prediction	= classifier.predict(features_test)
	timeSpent 	= time() - startTime

	return prediction, timeSpent

classifier, timeClass 	= classifyNB(features_train, labels_train)

pred, timePred			= predictNB(classifier, features_test)

##Mystuff
nSamples = len(features_test)
nCorrect = 0

for i in range(nSamples):

    if abs(pred[i] - labels_test[i]) < 0.0001:
        nCorrect += 1

print(nCorrect)

accuracy = float(nCorrect) / nSamples

print("Accuracy = %0.5f" % accuracy)

print("Time spent on classification = %.3f and prediction = %.3f" % (timeClass , timePred) )

#########################################################
