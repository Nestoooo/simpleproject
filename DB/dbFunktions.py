# DB connector to python
import mysql.connector

mydb = mysql.connector.connect(host='localhost', 
                               user='root', 
                               passwd='0987654321',
                               database='nesma')


#create cursor
mycursor = mydb.cursor()


#insert funktion
def insert_rec(**kwargs):
    sql = """INSERT INTO logint 
              (login, password)
              VALUES (%s, %s)"""
    
    values = (kwargs["unameUp"], kwargs["pwordUp"])
    try:        
        mycursor.execute(sql, values)
    except:
        mydb.rollback()
        return 0
    else:
        mydb.commit()
        return 1
    

#is it a user?
def usreOrNot (**kwargs):
    a = kwargs["uname"]
    b= kwargs["pword"]
    sql = "SELECT * FROM logint WHERE login = \"" + a + "\" AND password = \"" + b + "\""
    mycursor.execute(sql)
    foundUser=mycursor.fetchone()

    if foundUser is None:
        return 0
    else:
        return 1

#is this user name already exist?
def userNameExist (**kwargs):
    a = kwargs["unameUp"]

    sql = "SELECT * FROM logint WHERE login = \"" + a + "\" "
    mycursor.execute(sql)
    foundUser=mycursor.fetchone()

    if foundUser is None:
        return 0
    else:
        return 1


