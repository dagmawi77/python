import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='messages'
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)