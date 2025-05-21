import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)

mycursor = mydb.cursor()
mycursor.execute( "select * from customser limit 10 offset 5")
myresult=mycursor.fetchall()
for x in myresult:
    print(x)