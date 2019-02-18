import sys
sys.path.append('../configs')

from configs import db

def get_users():
	conn = db.connect()
	cursor = conn.cursor()
	sql = "SELECT id, username, address FROM users"
	cursor.execute(sql)
	results = cursor.fetchall()
	print(results)
	conn.close()