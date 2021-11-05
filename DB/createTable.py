# DB connector to python
import mysql.connector

tableName = "logint"

mydb = mysql.connector.connect(host='localhost', user='root', passwd='0987654321', database='nesma')
print(mydb)

try:
    #create cursor
    mycursor = mydb.cursor()

    #create logint table inside nesma database
    sql ="""CREATE TABLE """+tableName+"""(login VARCHAR (255), password VARCHAR (255))"""
    mycursor.execute(sql)

    #show table
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    for tables in mycursor:
        print(tables)
    print("\n[+] Table Create OK")
except:
    print("\n[!] Table Create ERROR")

#close the connection
mydb.close()
