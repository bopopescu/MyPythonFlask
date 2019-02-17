import flask
import sys
sys.path.insert(0, './controllers')

# CONTROLLERS
import users

## API SERVICES CONFIG
app = flask.Flask(__name__)
app.config["DEBUG"] = True


## DATABASE CONFIG
import db

mydb = db.connect()

mycursor = mydb.cursor()

## ROUTES

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

'''
@app.route('/login', methods=['POST'])
def login():
	content = flask.request.json

	print "SELECT * FROM users WHERE username='",content['username'],"' AND password ='",content['password'],"'"

	return flask.jsonify({
		"your_username":content['username'],
		"your_password":content['password']
		})
'''

@app.route('/api/v1/login', methods=['POST'])
def login():
	content = flask.request.json

	queryString = "SELECT * FROM users WHERE username=%s AND password=%s"	
	
	print queryString

	queryResult = mycursor.execute(queryString, (content['username'], content['password']))
	myresult = mycursor.fetchall()
	
	if myresult:
		user = myresult[0]
		return flask.jsonify({"result":"OK", "data":{
			"userid":user[0],
			"username":user[1],
			"address":user[3]
			}}) 
	else:
		return flask.jsonify({"result":"Record Not Found"})

@app.route('/api/v1/users', methods=['GET'])
def user_detail():
	userId = flask.request.args.get('id')

	queryString = "SELECT * FROM users WHERE id='"+userId+"'"	
	
	print queryString

	queryResult = mycursor.execute(queryString)
	user = mycursor.fetchone()
	
	if user:
		return flask.jsonify({"result":"OK", "data":{
			"userid":user[0],
			"username":user[1],
			"address":user[3]
			}}) 
	else:
		return flask.jsonify({"result":"Record Not Found"})

@app.route('/api/v1/users/all', methods=['GET'])
def user_all():

	queryString = "SELECT * FROM users ORDER BY id DESC"	
	
	print queryString

	queryResult = mycursor.execute(queryString)
	users = mycursor.fetchall()
	data = []

	if users:
		for user in users:
			data.append({
			"userid":user[0],
			"username":user[1],
			"address":user[3]
			}) 
		return flask.jsonify({"result":"OK", "data":data}) 
	else:
		return flask.jsonify({"result":"Record Not Found"})

@app.route('/api/v1/users/add', methods=['POST'])
def addUser():
	return users.doAddUser(flask, mydb)

@app.route('/api/v1/users', methods=['PUT'])
def updateUser():
	return users.doUpdateUser(flask, mydb)

@app.route('/api/v1/users', methods=['DELETE'])
def deleteUser():
	return users.doDeleteUser(flask)

app.run(port=8080)
