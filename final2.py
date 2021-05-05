"""Write a Python code to configure the MySQL Connector in your system and Insert data to MySQL
Table after which you Fetch and Display data from Table"""

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "python"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE python")

mycursor.execute("CREATE TABLE customer (Name Varchar(255), City varchar(255))")

sql  = "INSERT INTO customer (Name, City) VALUES (%s, %s)"
val  = ('Robert', 'Madurai')
val1 = ('Selvam', 'Tuticorin')
val2 = ('Nirmal', 'Madurai')

mycursor.execute(sql, val)
mycursor.execute(sql, val1)
mycursor.execute(sql, val2)

mydb.commit()

mycursor.execute(("select * from customer"))
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

