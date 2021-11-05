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

    #show table
    sql = "SELECT * FROM logint"
    mycursor.execute(sql)
    for i in mycursor:
        print(i)

    print("\n[+] Table Display OK")
except:
    print("\n[!] Table Display ERROR")
