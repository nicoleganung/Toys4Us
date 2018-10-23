# CSCI320 - Toys4Us
# Authors:
# Nicole Ganung 
# Wegmans UI Database

empOrCust = raw_input("Are you an employee or customer?\n")
if empOrCust.lower() == "employee":
	print("hello")
if empOrCust.lower() == "customer":
	shoppersClub = raw_input("Are you a shoppers club member?")
	shoppersClubCustomer(shoppersClub)
	if (shoppersClub.lower() == "yes") | (shoppersClub.lower() == "y"):
		numItems = raw_input("How many different items are you buying today?)
		
def 
