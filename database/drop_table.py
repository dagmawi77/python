import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)
mycursor = mydb.cursor()
sql = "drop table if exists customer"

mycursor.execute(sql)
