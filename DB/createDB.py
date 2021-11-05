# DB connector to python
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='0987654321')
print(mydb)

#create cursor
mycursor = mydb.cursor()


#create database
sql = "CREATE DATABASE nesma"
mycursor.execute(sql)

#show database
sql = "SHOW DATABASES"
mycursor.execute(sql)

for item in mycursor:
    print(item)

#drop database
#sql = "DROP DATABASE nesma"
#mycursor.execute(sql)

#close db
#mydb.close()