import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pythondb",
  passwd="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 