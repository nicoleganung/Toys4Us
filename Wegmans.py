# CSCI320 - Toys4Us
# Authors:
# Nicole Ganung
# Wegmans UI Database

def shoppersClubCustomer():
	shoppersClubId = raw_input("Please enter your shoppersClubId")
	shoppersClubPurchase(shoppersClubId)

def shoppersClubPurchase(shoppersClubName):
	numItems = raw_input("How many different items are you buying today?")

def itemPurchase():
	numItems = raw_input("How many different items are you buying today?")

empOrCust = input('Are you an employee or customer?\n')
if empOrCust.lower() == "employee":
        print("hello employee")
if empOrCust.lower() == "customer":
        shoppersClub = raw_input("Are you a shoppers club member?")
        if (shoppersClub.lower() == "yes") | (shoppersClub.lower() == "y"):
        	shoppersClubCustomer()
        elif (shoppersClub.lower() == "no") | (shoppersClub.lower() == "n"):
        	itemPurchase()
        	# Do you want to sign up for a shoppers club card today?
