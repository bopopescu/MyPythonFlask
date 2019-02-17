import mysql.connector

def connect():
	return mysql.connector.connect(
  		host="localhost",
  		user="tasksapp",
  		passwd="password",
  		database="tasksdb"
	)