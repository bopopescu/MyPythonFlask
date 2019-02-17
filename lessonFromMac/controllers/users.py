import sys
sys.path.insert(0, '../configs')
import db

def doAddUser(flask, mydb):
	content = flask.request.json
	mycursor = mydb.cursor()
	queryString = "INSERT INTO users(username, address) VALUES(%s, %s)"
	queryResult = mycursor.execute(queryString, (content['username'], content['address']))
	mydb.commit()
	print(mycursor.rowcount, "was inserted.", "and last id:", mycursor.lastrowid) 
	mycursor.close()
	mydb.close()

	return flask.jsonify({"result":"OK"})

def doUpdateUser(flask, mydb):
	print "update user"
	content = flask.request.json
	mycursor = mydb.cursor()
	queryString = "UPDATE users SET username=%s, address=%s WHERE id=%s"
	queryResult = mycursor.execute(queryString, (content['username'], content['address'], content['id']))
	mydb.commit()
	print(mycursor.rowcount, "was updated.") 
	mycursor.close()
	mydb.close()

	return flask.jsonify({"result":"OK"})

def doDeleteUser(flask):
	print "delete user"

	# GET USER ID
	userId = flask.request.args.get('id')

	# DATABASE 
	mydb = db.connect()
	mycursor = mydb.cursor()
	queryString = "DELETE FROM users WHERE id="+userId+""
	queryResult = mycursor.execute(queryString)
	mydb.commit()
	print mycursor.rowcount, "was deleted"
	mycursor.close()
	mydb.close()

	return flask.jsonify({"result":"OK"})

