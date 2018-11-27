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
			# database operations
			# any less than 30
			cursor.execute('SELECT i.amount, p.name FROM inventory_item as i, product as p WHERE inventory_id IN (SELECT inventory_id FROM store WHERE store_number = %s) AND amount < 30 AND i.upc = p.upc;', (storeNumber,))
			myresult = cursor.fetchall()
			print("Items with low inventory are: ")
			for data in myresult:
				print(str(data[1]) + ': ' + str(data[0]) + ' unit(s)')
			print

		elif choice == 3:
			itemName = input("Enter the name of the item you would like to order: ")
			itemAmount = int(input("Please enter the number of this item you would like to order: "))
			#database operations
			cursor.execute("SELECT upc FROM product WHERE name = '"+itemName+"'")
			result = cursor.fetchone()
			if len(result) == 0:
				print("Not a valid product. Please try again")
				break
			itemUPC = result[0]
			cursor.execute("UPDATE inventory_item SET amount = amount+" + str(itemAmount) + " WHERE upc IN (SELECT product.upc FROM product WHERE " + str(itemUPC) + " = product.upc)")
			print
			print(str(itemAmount) + " units of " + itemName + " ordered")
			print
		else:
			print("Incorrect choice. Please try again")

def vendor():
	vendorId = int(input("Please enter your ID Number: "))
	vendorExists = False
	cursor.execute('SELECT vendor_id FROM vendor WHERE vendor_id = %s', (vendorId,))
	myresult = cursor.fetchall()
	for data in myresult:
		if data[0] == vendorId:
			vendorExists = True

	while not vendorExists:
		print("You are not a vendor in our system, please try again")
		vendorId = int(input("Please enter your ID Number: "))
		cursor.execute('SELECT vendor_id FROM vendor WHERE vendor_id = %s', (vendorId,))
		myresult = cursor.fetchall();
		for data in myresult:
			if data[0] == vendorId:
				vendorExists = True
				break

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
			# database operations
			cursor.execute('SELECT * FROM inventory_item as inv natural left outer join product WHERE inv.inventory_id in (select inventory_id from vendor where vendor_id = %s)', (vendorId,))
			result = cursor.fetchall()
			print
			for data in result:
				print(data[6] + ": " + str(data[3]) + " units")
			print
		elif choice == 2:
			itemName = input("Enter the name of the item you would like to order: ")
			itemAmount = int(input("Please enter the number of this item you would like to order: "))
			# database operations
			cursor.execute("Select upc from product where name = '"+itemName+"'")
			result = cursor.fetchone()
			if len(result) == 0:
				print("Not a valid product. Please try again")
				break
			itemUPC = result[0]
			cursor.execute("Select * from inventory_item where upc = "+ str(itemUPC) +" and inventory_id in (select inventory_id from vendor where vendor_id = %s)", (vendorId,))
			result = cursor.fetchone()
			if len(result) == 0:
				print("Item not in inventory. Please try again")
				break
			print
			cursor.execute("update inventory_item set amount = "+ str(int(result[3]) + itemAmount) + " where upc = " + str(itemUPC))
			print(str(itemAmount) + " units of " + itemName + " ordered")
			cursor.execute("Select * from inventory_item where upc = " + str(
			itemUPC) + " and inventory_id in (select inventory_id from vendor where vendor_id = %s)", (vendorId,))
			result = cursor.fetchone()
			print
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
		myresult = cursor.fetchall()
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
		choice = int(input("Please enter the number of the action you'd like to take: "))
		if choice == 0:
			print("Logging out...")
			break
		elif choice == 1:
			numItems = int(input("How many different items do you have?"))
			print("Enter the item followed by the amount")
			total = 0.0
			while numItems != 0:
				itemName = input("")
				itemAmount = input("")
				cursor.execute("SELECT price FROM product, inventory_item WHERE product.upc = inventory_item.upc AND product.name = '"+ itemName + "'")
				myresult = cursor.fetchone()
				total=total+(float(myresult[0])*itemAmount)
				numItems=numItems-1
			print
			print("Your total is $" + str(total))
			print
		elif choice == 2:
			storeNumber = input("Enter the store number you would like information for: ")
			#database operations
			cursor.execute('SELECT open_hour, close_hour FROM store WHERE store_number = %s', (storeNumber,))
			myresult = cursor.fetchone()
			print
			print("Store opens: " + str(myresult[0]))
			print("Store closes: " + str(myresult[1]))
			print
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
		vendor()
	cursor.close()
	conn.commit()
	conn.close()

if __name__ == '__main__':
	main()