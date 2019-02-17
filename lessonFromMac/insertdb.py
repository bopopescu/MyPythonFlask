import db

mydb = db.connect()

mycursor = mydb.cursor()

sql = "INSERT INTO users (username, address) VALUES (%s, %s)"
val = ("wildananugrah05", "Tanah Kusir")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.", "and last id:", mycursor.lastrowid) 