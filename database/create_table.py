import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password='',
    database='newdagi'
)

mycursor = mydb.cursor()
mycursor.execute("create table user" \
"(id int auto_increment primary key, " \
"username varchar(255) not null, " \
"password varchar(255) not null, " \
"email varchar(255) not null, " \
"phone varchar(255) not null, " \
"address varchar(255) not null, " \
"city varchar(255) not null, " \
"state varchar(255) not null, " \
"country varchar(255) not null, " \
"zipcode varchar(255) not null, " \
"created_at datetime default current_timestamp, " \
"updated_at datetime default current_timestamp on update current_timestamp, " \
"last_login datetime default current_timestamp, " \
"status enum('active', 'inactive') default 'active', " \
"role enum('admin', 'user') default 'user' )") 

mycursor.execute("insert into user (username, password, email, phone, address, city, state, country, zipcode) " \
"values (%s, %s, %s, %s, %s, %s, %s, %s, %s)", ("admin", "admin", "abcd@gmail.com","0922334455", "address", "city", "state", "country", "zipcode"))

mycursor.execute("select * from user")
mycursor.fetchall()
for x in mycursor:
    print(x)