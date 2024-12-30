import mysql.connector
conn = mysql.connector.connect(host = "localhost", database = "SUPERSTORE",user = "root", password= "Root")
cursor = conn.cursor()
print(conn.is_connected())
mysql = "select * from samplesuperstore"
cursor.execute(mysql)
rows = cursor.fetchall()
print(rows)