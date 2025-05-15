import mysql.connector

mydb = mysql.connector.connect(

    host='localhost',
    user='root',
    password=''
)

mycursor = mydb.cursor()
mycursor.execute("CREATE database if not exists newdagi")
mycursor.execute("show databases")
for db in mycursor:
    print(db)    