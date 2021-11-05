# DB connector to python
import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', passwd='0987654321', database='nesma')
print(mydb)

#create cursor
mycursor = mydb.cursor()

#alter or modify in the table
sql = "ALTER TABLE logint ADD auto_id INT AUTO_INCREMENT PRIMARY KEY"
mycursor.execute(sql)
