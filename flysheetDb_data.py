import sqlite3
import openpyxl

db = sqlite3.connect('flysheetDb.db')
wb = openpyxl.load_workbook('data.xlsx')
employee = wb['EMPLOYEE']
#employee_list = []
for idx, row in enumerate(employee.rows):
	per_row = []
	if idx != 0:
		for i, cell in enumerate(row):
			if i != 0:
				per_row.append(cell.value)
			#print per_row
			db.execute('INSERT INTO Employee(fname,lname,title,department,base_region,gender,dob,email,phone,start_date) VALUES (?,?,?,?,?,?,?,?,?,?)', tuple(per_row))   
		#employee_list.append(per_row)

#print employee_list


db.commit()