import sqlite3
import openpyxl


db = sqlite3.connect('flysheetDb.db')
wb = openpyxl.load_workbook('data.xlsx', data_only=True)
employee = wb['EMPLOYEE']
for idx, row in enumerate(employee.rows):
	if idx != 0:
		per_row = []
		for i, cell in enumerate(row):
			per_row.append(cell.value)
		del per_row[0]
		db.execute('INSERT INTO Employee(fname,lname,title,department,base_region,gender,dob,email,phone,start_date) VALUES (?,?,?,?,?,?,?,?,?,?)', tuple(per_row))   

product = wb['PRODUCT']
for idx, row in enumerate(product.rows):
	if idx != 0:
		per_row = []
		for cell in row:
			per_row.append(cell.value)
		del per_row[0]
		db.execute('INSERT INTO Product(name, subscription_model, type, priceUSD, priceNTD, pub_id) VALUES (?,?,?,?,?,?)', tuple(per_row)) 

invoice = wb['INVOICE']
for idx, row in enumerate(invoice.rows):
	if idx != 0:
		per_row = []
		for cell in row:
			per_row.append(cell.value)
		del per_row[0]
		db.execute('INSERT INTO Invoice(inv_number, cus_id, issued_date, quarter, payment_date, amountUSD, amountNTD) VALUES (?,?,?,?,?,?,?)', tuple(per_row)) 

customer = wb['CUSTOMER']
for idx, row in enumerate(customer.rows):
	if idx != 0:
		per_row = []
		for cell in row:
			per_row.append(cell.value)
		del per_row[0]
		db.execute('INSERT INTO Customer(name, contact_person, email, phone, address, region, sales_person_id) VALUES (?,?,?,?,?,?,?)', tuple(per_row)) 

publisher = wb['PUBLISHER']
for idx, row in enumerate(publisher.rows):
	if idx != 0:
		per_row = []
		for cell in row:
			per_row.append(cell.value)
		del per_row[0]
		db.execute('INSERT INTO Publisher(name, contact_person, country, phone, address, email, prod_specialist_id) VALUES (?,?,?,?,?,?,?)', tuple(per_row)) 

db.commit()