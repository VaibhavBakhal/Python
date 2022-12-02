import mysql.connector
db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="root"    
    )
print(db.connection_id)
cur= db.cursor()
c=cur.execute("show databases")
for i in c:
    print(i)