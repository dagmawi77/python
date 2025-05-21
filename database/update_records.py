import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)

mycursor = mydb.cursor()
sql = "update customser set name = %s, address = %s where name = %s"
val = ("John", "Highway 21", "Michael")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")