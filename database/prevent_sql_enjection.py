import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customser WHERE name = %s"
adr = ("Dagmawi", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)