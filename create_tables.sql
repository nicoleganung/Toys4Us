CREATE TABLE Product(
	UPC int,
	packaging_type varchar(20),
	brand_ID int,
	name varchar(40),
	primary key(UPC)
);

CREATE TABLE Product_Type(
	type varchar(20),
	size numeric(4,2),
	primary key(type,size)
);

CREATE TABLE Brand(
	brand_ID int,
	UPC int,
	brand_name varchar(40),
	primary key(brand_ID,UPC)
);

CREATE TABLE Vendor(
	vendor_ID int,
	inventory_ID int,
	primary key(vendor_ID)
);

CREATE TABLE Store_buys_from_vendor(
	store_number int,
	vendor_ID int,
	primary key(store_number,vendor_ID)
);

CREATE TABLE Inventory_item(
	inventory_ID int,
	store_ID int,
	UPC int,
	price int,
	amount int,
	primary key(inventory_ID)
);

CREATE TABLE Inventory_contains(
	UPC int,
	inventory_ID int,
	primary key(UPC,inventory_ID)
);

CREATE TABLE Employee(
	employee_ID int,
	shopper_club_ID int,
	primary key(employee_ID, shopper_club_ID)
);

CREATE TABLE Store(
	store_number int,
	open int,
	close int,
	phone_number int,
	inventory_ID int,
	employee_ID int,
	primary key(store_number)
);

CREATE TABLE Receipt(
	receipt_ID int,
	UPC int,
	shopper_club_ID int,
	price_paid numeric(6,2),
	total_price numeric(6,2),
	date timestamp not null,
	primary key(receipt_ID,UPC)
);

CREATE TABLE Receipt_contains(
	UPC int,
	receipt_ID int,
	primary key(UPC,receipt_ID)
);

CREATE TABLE Address(
	address_ID int,
	zip int,
	state varchar(2),
	city varchar(20),
	apt_number int,
	street_name varchar(20),
	house_number int,
	primary key(address_ID)
);

CREATE TABLE Customer(
	shopper_club_ID int,
	firstname varchar(20),
	lastname varchar(20),
	phone_number int,
	primary key(shopper_club_ID)
);
