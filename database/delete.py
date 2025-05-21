import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)

mycursor = mydb.cursor()

sql = "delete  FROM customser where name ='Sandy' "

mycursor.execute(sql)

mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

