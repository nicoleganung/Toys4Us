# CSCI320 - Toys4Us
# Authors:
# Nicole Ganung
# Chris Renninger
# Wegmans UI Database

import psycopg2 

conn = psycopg2.connect(host="reddwarf.cs.rit.edu", user="p32002h", password="eigo0oapooj8ENgeGhue", dbname="p32002h")
cursor = conn.cursor();

def shoppersClubCustomer():
    shoppersClubId = input("Please enter your shoppersClubId")
    shoppersClubPurchase(shoppersClubId)


def shoppersClubPurchase(shoppersClubName):
    numItems = input("How many different items are you buying today?")


def itemPurchase():
    numItems = input("How many different items are you buying today?")

def employee():
    employeeId = int(input("Please enter your ID Number: "))
    # search for ID number
    employeeExists = False
    cursor.execute('SELECT employee_id FROM employee WHERE employee_id = %s', (employeeId,))
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
            for data in result:
                print(data[6] + ": " + str(data[3]) + " units")

            print("Coke: 345 units")
            print("Bread: 479 units")
        elif choice == 2:
            itemName = input("Enter the name of the item you would like to order: ")
            itemAmount = int(input("Please enter the number of this item you would like to order: "))
            # database operations
            cursor.execute("Select upc from product where name = '"+itemName+"'")
            result = cursor.fetchall()
            if len(result) == 0:
                print("Not a valid product. Please try again")
                break
            itemUPC = result[0]
            cursor.execute("Select * from inventory_item where upc = "+ str(itemUPC) +" and inventory_id in (select inventory_id from vendor where vendor_id = %s)", (vendorId,))
            result = cursor.fetchall()
            if len(result) == 0:
                print("Item not in inventory. Please try again")
                break
            cursor.execute("update inventory_item set amount = "+ str(int(result[3]) + itemAmount) + " where upc = " + str(itemUPC))
            print(str(itemAmount) + " units of " + itemName + " ordered")
            cursor.execute("Select * from inventory_item where upc = " + str(
            itemUPC) + " and inventory_id in (select inventory_id from vendor where vendor_id = %s)", (vendorId,))
            result = cursor.fetchone()
        else:
            print("Incorrect choice. Please try again")

def customer():
    id = int(input("Please enter your ID Number: "))
    # database operation
    # verify ID exists
    while True:
        print("Thank you for logging into the system. Here is what you can do:")
        print("0. Exit")
        print("1. Make a purchase")
        print("2. Get store info")
        choice = int(input("Please enter the number of the action you'd like to take:"))
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
            print("Our store hours are:")
            print("MWF 11-5pm")
            print("Address: 1 Lomb Memorial Dr.")
        else:
            print("Incorrect choice. Please try again")


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