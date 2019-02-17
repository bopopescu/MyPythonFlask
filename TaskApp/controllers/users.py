import sys
sys.path.append("..")
from configs import db

def doLogin(flask):
	content = flask.request.json

	mydb = db.connect()
	mycursor = mydb.cursor()
	queryString = "SELECT id FROM users WHERE email=%s AND password=%s"
	queryResult = mycursor.execute(queryString, (content['email'], content['password']))
	myresult = mycursor.fetchone()

	myResponse = []

	if myresult:
		myResponse = {
			"rc":"00",
			"data": {
				"userId":myresult[0]
			}
		}
	else:
		myResponse = {
			"rc":"01", 
			"message":"email or password is invalid"
		}

	return flask.jsonify(myResponse)