# CSCI320 - Toys4Us
# Authors:
# Nicole Ganung
# Chris Renninger
# Wegmans UI Database

def shoppersClubCustomer():
	shoppersClubId = input("Please enter your shoppersClubId")
	shoppersClubPurchase(shoppersClubId)


def shoppersClubPurchase(shoppersClubName):
	numItems = input("How many different items are you buying today?")


def itemPurchase():
	numItems = input("How many different items are you buying today?")

def employee():
	id = int(input("Please enter your ID Number: "))
	while True:
		print("Thank you for logging into the system. Here is what you can do.")
		print("0. Exit")
		print("1. Look at 20 most recent items purchased")
		print("2. Look at items with low inventory")
		print("3. Order inventory")
		choice = int(input("Please enter the number of the action you'd like to take:"))
		if choice == 0:
			print("Logging out...")
			break
		elif choice == 1:
			#database operations
			print("x units of y purchased for $z on [Date]")
			print("x units of y purchased for $z on [Date]")
			print("x units of y purchased for $z on [Date]")
			print(".....")
		elif choice == 2:
			#database operations
			print("Items with low inventory are: ")
			print("Coke: 25 units")
			print("Bread: 10 units")
		elif choice == 3:
			itemName = input("Enter the name of the item you would like to order: ")
			itemAmount = int(input("Please enter the number of this item you would like to order: "))
			#database operations
			print(str(itemAmount) + " units of " + itemName + " ordered")
		else:
			print("Incorrect choice. Please try again")

def vendor():
	id = int(input("Please enter your ID Number: "))
	while True:
		print("Thank you for logging into the system. Here is what you can do:")
		print("0. Exit")
		print("1. Check inventory")
		print("2. Add to inventory")
		choice = int(input("Please enter the number of the action you'd like to take:"))
		if choice == 0:
			print("Logging out...")
			break
		elif choice == 1:
			#database operations
			print("Coke: 345 units")
			print("Bread: 479 units")
		elif choice == 2:
			itemName = input("Enter the name of the item you would like to order: ")
			itemAmount = int(input("Please enter the number of this item you would like to order: "))
			# database operations
			print(str(itemAmount) + " units of " + itemName + " ordered")
		else:
			print("Incorrect choice. Please try again")

def customer():
	id = int(input("Please enter your ID Number: "))
	while True:
		print("Thank you for logging into the system. Here is what you can do:")


def main():
	empOrCust = input('Please enter if you are an employee, vendor, or customer: ')
	if empOrCust.lower() == "employee":
		employee()
	elif empOrCust.lower() == "customer":
		customer()
	elif empOrCust.lower() == "vendor":
		vendor()

if __name__ == '__main__':
    main()
