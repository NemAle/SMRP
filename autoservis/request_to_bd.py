import sqlite3

con=sqlite3.connect("./AutoServis.db")
cur=con.cursor()

auto_id = 2
query1=cur.execute(f"""SELECT * FROM Auto WHERE number_auto = {auto_id}""")
result1 = query1.fetchone()
print(result1)




con.close()
