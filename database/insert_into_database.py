import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='eschool'    
)

mycursor = mydb.cursor()

sql = "Insert into customser values (%s, %s)"
val = ('Dagmawi','Adiss Abab')
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
mycursor.execute("SELECT * FROM customser")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)