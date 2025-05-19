import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='eschool'
)

mycursor = mydb.cursor()
mycursor.execute("select * from customser")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
# print(myresult)