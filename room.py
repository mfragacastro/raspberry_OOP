class Room:

	def __init__(self, room_name):
		self.name = room_name
		self.description = None
		self.linked_rooms = {}
		self.character = None
		self.item = None
		
	# Character getter and setter
	def set_character(self, character):
		self.character = character
	
	def get_character(self):
		return self.character
		
	# Item getter and setter
	def get_item(self):
		return self.item
	
	def set_item(self,item):
		self.item = item
	
	def set_description(self, room_description):
		self.description = room_description
		
	def get_description(self):
		return self.description
		
	def set_name(self, room_name):
		self.name = room_name
		
	def get_name(self):
		return self.name
	
	def describe(self): 
		print( self.description )
	
	def link_room(self, room_to_link, direction):
		self.linked_rooms[direction] = room_to_link
		#print( self.name + " linked rooms :" + repr(self.linked_rooms) )
	
	def get_details(self):
		print("The " + self.get_name())
		for i in range(10):
			print('-',sep='',end='')
		print("")
		print(self.get_description())
		for direction in self.linked_rooms:
			room = self.linked_rooms[direction]
			print( "The " + room.get_name() + " is " + direction)
		print("")
	
	def move(self, direction):
		if direction in self.linked_rooms:
			return self.linked_rooms[direction]
		else:
			print ("No hay puerta hacia ese lado")
			return self
