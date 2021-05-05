
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "python"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE python")
#mycursor.execute("SHOW DATABASES")
#mycursor.execute("CREATE TABLE customer (Name Varchar(255), City varchar(255))")
#mycursor.execute("SHOW TABLES")
#sql = "INSERT INTO customer (Name, City) VALUES (%s, %s)"
#val  = ('Robert', 'Madurai')
#val1 = ('selva', 'Tuticorin')
#val2 = ('Nimmy', 'Madurai')

#mycursor.execute(sql, val)
#mycursor.execute(sql, val1)
#mycursor.execute(sql, val2)

#mydb.commit()

mycursor.execute(("select * from customer"))
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

#for x in mycursor:
#   print(x)