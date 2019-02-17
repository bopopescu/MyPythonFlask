import db

def doLogin(email. password):
	mydb = db.connect()
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM users WHERE email='" email "' AND password='" password "'")
	