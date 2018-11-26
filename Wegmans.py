# CSCI320 - Toys4Us
# Authors:
# Nicole Ganung
# Chris Renninger
# Wegmans UI Database

import psycopg2 
import datetime

conn = psycopg2.connect(host="reddwarf.cs.rit.edu", user="p32002h", password="eigo0oapooj8ENgeGhue", dbname="p32002h")
cursor = conn.cursor();

def shoppersClubCustomer():
	shoppersClubId = input("Please enter your shoppersClubId")
	shoppersClubPurchase(shoppersClubId)


def shoppersClubPurchase(shoppersClubName):
	numItems = input("How many different items are you buying today?")


def itemPurchase():
	numItems = input("How many different items are you buying today?")

def employee(storeNumber):
	employeeId = int(input("Please enter your ID Number: "))
	# search for ID number
	employeeExists = False
	cursor.execute('SELECT employee_id FROM employee WHERE employee_id = %s', (employeeId,))
	# fetchall() gives back a array of inputs 
	# fetchone() gives back one element 
	myresult = cursor.fetchall()
	for data in myresult:
		if data[0] == employeeId:
			employeeExists = True

	while not employeeExists:
		print("You are not an employee in our system, please try again")
		employeeId = int(input("Please enter your ID Number: "))
		cursor.execute('SELECT employee_id FROM employee WHERE employee_id = %s', (employeeId,))
		myresult = cursor.fetchall();
		for data in myresult:
			if data[0] == employeeId:
				employeeExists = True
			break

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
			print
			#database operations
			cursor.execute('SELECT DISTINCT p.name, date, r.price_paid FROM receipt AS r, product AS p WHERE r.upc = p.upc GROUP BY p.upc, r.upc, r.date, r.price_paid ORDER BY date DESC LIMIT 20')
			receiptResult = cursor.fetchall()
			for data in receiptResult:
				timestamp = data[1]
				date = str(timestamp.month) + '/' + str(timestamp.day) + '/' + str(timestamp.year)
				price = float(data[2])
				print(str(data[0]) + ' purchased for $' + str(price) + ' on ' + str(date))
			print
		elif choice == 2:
			print
			#database operations
			cursor.execute('SELECT * FROM inventory_item WHERE inventory_id IN (SELECT inventory_id FROM store WHERE store_number = 0) AND amount < 30')
			print("Items with low inventory are: ")
			print("Coke: 25 units")
			print("Bread: 10 units")

		elif choice == 3:
			itemName = input("Enter the name of the item you would like to order: ")
			itemAmount = int(input("Please enter the number of this item you would like to order: "))
			#database operations
			#cursor.execute('SELECT * FROM inventory')
			print(str(itemAmount) + " units of " + itemName + " ordered")
		else:
			print("Incorrect choice. Please try again")

def vendor(storeNumber):
	id = int(input("Please enter your ID Number: "))
	# If it doesn't exist:
	# Would you like to create a account?
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

def customer(storeNumber):
	customerID = int(input("Please enter your Shoppers Club ID Number: "))
	# search for ID number
	customerExists = False
	cursor.execute('SELECT shopper_club_id FROM customer WHERE shopper_club_id = %s', (customerID,))
	myresult = cursor.fetchall()
	for data in myresult:
		if data[0] == customerID:
			customerExists = True

	while not customerExists:
		print("Your ID number was not recognized, for the store's card enter 0")
		customerID = int(input("Please enter your ID Number: "))
		cursor.execute('SELECT shopper_club_id FROM customer WHERE shopper_club_id = %s', (customerID,))
		myresult = cursor.fetchall();
		for data in myresult:
			if data[0] == customerID:
				customerExists = True
			break

	print("Thank you for logging into the system.")
	while True:
		print("Here's a list of the action you can do")
		print("0. Exit")
		print("1. Make a purchase")
		print("2. Get store info")
		print("3. Get product info")
		print("4. View receipts")
		choice = int(input("Please enter the number of the action you'd like to take: "))
		if choice == 0:
			print("Logging out...")
			break
		elif choice == 1:
			while True:
				itemName = input("Enter the name of the item you would like to purchase or type exit: ")
				if itemName.lower() == "exit":
					#database operations
					print("Your total is")
					break
				itemAmount = int(input("Please enter the number of this item you would like to purchase: "))

		elif choice == 2:
			#database operations
			cursor.execute('SELECT open_hour, close_hour, address_id FROM store WHERE store_number = %s', (storeNumber))
			myresult = cursor.fetchone();
			print()
			print("Store opens:", myresult[0])
			print("Store closes:", myresult[1])
			cursor.execute('SELECT house_number, street_name, city, state, zip from address where address.address_id = %s', (storeNumber,))
			myresult = cursor.fetchone();
			print("Store Address:", myresult[0], myresult[1], myresult[2], ",", myresult[3], myresult[4])
			print()

		elif choice == 3:
			# get product info
			product = input("Please enter the product you are looking for: ")
			#cursor.execute('SELECT upc from product where name = %s',(product,))
			break
		elif choice == 4:
			cursor.execute('SELECT * FROM receipt full outer join product on receipt.upc = product.upc WHERE receipt.shopper_club_id = %s order by date desc', (customerID,))
			myresult = cursor.fetchall();
			# view receipts
			for data in myresult:
				print("Receipt ID:", data[0], "Date Purchased:", data[3], "Product:", data[9], "Price:", data[2])
			print()
		else:
			print("Incorrect choice. Please try again")


def main():
	storeNumber = input("What store is this? ")
	empOrCust = input('Please enter if you are an employee, vendor, or customer: ')
	if empOrCust.lower() == "employee":
		employee(storeNumber)
	elif empOrCust.lower() == "customer":
		customer(storeNumber)
	elif empOrCust.lower() == "vendor":
		vendor(storeNumber)

if __name__ == '__main__':
    main()
