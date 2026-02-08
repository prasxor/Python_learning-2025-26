import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

sql = 'INSERT INTO products (id,name) VALUES (%s,%s)'
val = [
( 154, 'Chocolate Heaven' ),
( 155, 'Tasty Lemons' ),
( 156, 'Vanilla Dreams' )
]

mycursor.executemany(sql,val)

mydb.commit()