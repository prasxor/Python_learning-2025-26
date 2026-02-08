import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = 'CREATE TABLE Users(id INT(5) PRIMARY KEY, name VARCHAR(15), fav int(4))'

mycursor.execute(sql)
