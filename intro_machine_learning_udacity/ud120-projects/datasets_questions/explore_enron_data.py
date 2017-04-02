#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

#Length
print "Number of persons: " + str( len(enron_data))

#Entries per person
print "Entries per Person: " + str(len(enron_data["SKILLING JEFFREY K"]))

#Count number of Persons of Interest
PoICount = 0
for key in enron_data:
	if enron_data[key]["poi"]:
		PoICount += 1

print "#PoI: " + str(PoICount)

#Handmade #PoIs
poi_txt = open('../final_project/poi_names.txt').readlines()
pois = [txt.strip() for txt in poi_txt]
print "Handmade #PoIs: " + str(len(pois) - 2)

#JAmes Prentice stock holdings
print "Stock Value: " + str(enron_data["PRENTICE JAMES"]["total_stock_value"])

#Wesley Colwell mails to PoIs
print "Mail to PoI: " + str(enron_data["COLWELL WESLEY"]["from_this_person_to_poi"])

#Options  Jeffrey K Skilling
print "Exerciced stock options: " + str(enron_data[ "SKILLING JEFFREY K"]["exercised_stock_options"])

#Largest payments
largest_payment = 0
largest_crook = "Me"
for key in ["SKILLING JEFFREY K", "LAY KENNETH L", "FASTOW ANDREW S"]:

	if enron_data[key]["total_payments"] > largest_payment:
		largest_payment = enron_data[key]["total_payments"]
		largest_crook = key

print "Largest Crook is " + largest_crook + " who earned: " + str(largest_payment)

#Have a quantified salary
salaryCount = 0
mailCount = 0
for key in enron_data:
	if enron_data[key]["salary"] != "NaN":
		salaryCount += 1
	if enron_data[key]["email_address"] != "NaN":
		mailCount += 1

print "#People with quantified salary " + str(salaryCount)
print "#People with mail address " + str(mailCount)

#People missing total payments
totalPayCount = 0
PoIHasPayCount = 0
for key in enron_data:
	if enron_data[key]["total_payments"] != "NaN":
		totalPayCount += 1
		if enron_data[key]["poi"] == True:
			PoIHasPayCount += 1

print "People missing total payments " + str(totalPayCount) + ", this is ", (1 - (float(totalPayCount)/len(enron_data))) * 100
print("PoIs having total payments %d, this is %.1f " % (PoIHasPayCount,  (float(PoIHasPayCount)/PoICount) * 100))

#Adding 10 persons
totalPeople = len(enron_data) + 10
newMissTotPay = totalPeople - totalPayCount
print("Total New Number of People: %d" % totalPeople)
print("New number of NaNs: %d" % newMissTotPay)

#New PoIs
newPoICount = PoICount + 10
newPoIMissPayCount = newPoICount - 10
print("New PoIs %d" % newPoICount)
print("New PoIs Missing payments: %d" % (newPoICount - newPoIMissPayCount ))
