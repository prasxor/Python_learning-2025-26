import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = 'INSERT INTO Users (id,name,fav) VALUES (%s,%s,%s)'
val = [
(1, 'John', 154),
(2, 'Peter', 154),
(3, 'Amy', 155),
(4, 'Hannah', None),
(5, 'Michael', None)
]

mycursor.executemany(sql,val)

mydb.commit()