import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customser where name like'%Dagmawi%'")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)