import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = 'CREATE TABLE products(id INT(3) PRIMARY KEY, name VARCHAR(15))'

mycursor.execute(sql)