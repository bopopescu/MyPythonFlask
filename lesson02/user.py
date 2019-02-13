class User:
	def __init__(self, username, address):
		self.username = username
		self.address = address
		
	def getUsername(self):
		return self.username
	
	def getAddress(self):
		return self.address
		
	def setUsername(self, username):
		self.username = username