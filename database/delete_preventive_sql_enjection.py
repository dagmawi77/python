import mysql.connector

mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="eschool"
)


mycursor = mydb.cursor()

sql = "DELETE FROM customser WHERE name = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)


mydb.commit()

print(mycursor.rowcount, "record(s) deleted")