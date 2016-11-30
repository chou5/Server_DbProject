import sqlite3
import openpyxl

db = sqlite3.connect('flysheetDb.db')
wb = openpyxl.load_workbook('data.xlsx')
employee = wb['EMPLOYEE']
for idx, row in enumerate(employee.rows):
	if idx != 0:
		per_row = []
		for i, cell in enumerate(row):
			per_row.append(cell.value)
		del per_row[0]
		db.execute('INSERT INTO Employee(fname,lname,title,department,base_region,gender,dob,email,phone,start_date) VALUES (?,?,?,?,?,?,?,?,?,?)', tuple(per_row))   




db.commit()