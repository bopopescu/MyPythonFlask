import db

mydb = db.connect()

mycursor = mydb.cursor()

result = mycursor.callproc("my_procedure", ['test', 0])

print(result[1])

mycursor.close()
mydb.close()