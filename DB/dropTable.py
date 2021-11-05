# DB connector to python
import mysql.connector

tableName = "logint"

mydb = mysql.connector.connect(host='localhost', user='root', passwd='0987654321', database='nesma')
print(mydb)

#create cursor
mycursor = mydb.cursor()

try:
    #show table
    sql = "SHOW TABLES"
    mycursor.execute(sql)
    for tables in mycursor:
        print(tables)

    #drop table
    sql = "DROP TABLE IF EXISTS "+tableName
    mycursor.execute(sql)
    print("\n[+] Table Drop OK")
except:
    print("\n[!] Table Drop ERROR")


#close the connection
mydb.close()
