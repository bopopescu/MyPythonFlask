import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/api/v1/resource/books',methods=['POST'])
def api_post():
	
	
app.run(port='8000',host='10.70.132.173')