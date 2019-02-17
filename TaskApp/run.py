import flask
import sys

# CONTROLLERS
from controllers import users

## API SERVICES CONFIG
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/users/login', methods=['POST'])
def login():
	return users.doLogin(flask)

app.run(port=8080)
