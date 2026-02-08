import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="pythonDatabase"
)

mycursor = mydb.cursor()

# INNER JOIN 

# sql = "SELECT \
#     Users.name As User, \
#     products.name AS favorite \
#     From Users \
#     INNER JOIN products ON Users.fav = products.id"
    
# LEFT JOIN 

# sql = "SELECT\
#     Users.name AS user,\
#     products.name AS favorite\
#     FROM Users\
#     LEFT JOIN products ON Users.fav = products.id"
    
    
# RIGHT JOIN 

sql = "SELECT\
    Users.name AS user,\
    products.name AS favorite\
    FROM Users\
    RIGHT JOIN products ON Users.fav = products.id"

    
mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)