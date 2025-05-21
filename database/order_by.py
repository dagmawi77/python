import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customser  order by name desc"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)