class Character():
    
    def __init__(self, char_name, char_description):
        """Create a character"""
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.items = []

    def __del__(self):
        """Destroy a character"""
        print ("destructor")
    
    def describe(self):
        """Describe this character"""
        print( self.name + " is here!" )
        print( self.description )

    def set_conversation(self, conversation):
        """Set what this character will say when talked to"""
        self.conversation = conversation

    def talk(self):
        """Talk to this character"""
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """Fight with this character"""
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
	def __init__(self, char_name, char_description):
		"""Create an enemy"""
		super().__init__(char_name, char_description)
		self.weakness = None
		
	def fight(self, combat_item):
		""" Figth using an item against an enemy"""
		if combat_item == self.weakness:
			print("Has vencido a " + self.name + " con " + combat_item)
			return True
		else:
			print(self.name + " te ha dado una paliza")
			return False
	
	def set_weakness(self, weakness):
		"""Define what defeats this enemy"""
		self.weakness = weakness
    
	def get_weakness(self):
		"""Reveal what defeats this enemy"""
		return self.weakness
	
	def set_items(self,lista_items):
		"""Define the items this enemy owns"""
		self.items = lista_items
	
	def get_items(self):
		"""Get the list of items the enemy owns"""
		return self.items
	
	def roba_item(self, item_name):
		"""Steal an item from the enemy"""
		if item_name in self.items:
			self.items.remove(item_name)
			print("Le has robado " + item_name + " a " + self.name)
		else:
			print(self.name + " no tiene ese objeto")

class Friend(Character):

	def __init__(self, char_name, char_description):
		"""Create a friend"""
		super().__init__(char_name, char_description)
		self.felling = None
		
	def hug(self):
		"""Get a hug"""
		print(self.name + " te abraza también")
