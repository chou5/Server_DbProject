import sqlite3
db = sqlite3.connect('picnic.db')
db.execute("CREATE TABLE picnic (id INTEGER PRIMARY KEY, item CHAR(100) NOT NULL, quant INTEGER NOT NULL)")
db.execute("INSERT INTO picnic (item,quant) VALUES ('bread', 4)")
db.execute("INSERT INTO picnic (item,quant) VALUES ('cheese', 2)")
db.execute("INSERT INTO picnic (item,quant) VALUES ('grapes', 30)")
db.execute("INSERT INTO picnic (item,quant) VALUES ('cake', 1)")
db.execute("INSERT INTO picnic (item,quant) VALUES ('soda', 4)")
db.commit()