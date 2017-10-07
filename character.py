class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.items = []

    def __del__(self):
        print ("destructor")
    
    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):
	def __init__(self, char_name, char_description):
		super().__init__(char_name, char_description)
		self.weakness = None
		
	def fight(self, combat_item):
		if combat_item == self.weakness:
			print("Has vencido a " + self.name + " con " + combat_item)
			return True
		else:
			print(self.name + " te ha dado una paliza")
			return False
	
	def set_weakness(self, weakness):
		self.weakness = weakness
    
	def get_weakness(self):
		return self.weakness
	
	def set_items(self,lista_items):
		self.items = lista_items
	
	def get_items(self):
		return self.items
	
	def roba_item(self, item_name):
		if item_name in self.items:
			self.items.remove(item_name)
			print("Le has robado " + item_name + " a " + self.name)
		else:
			print(self.name + " no tiene ese objeto")

class Friend(Character):
	def __init__(self, char_name, char_description):
		super().__init__(char_name, char_description)
		self.felling = None
		
	def hug(self):
		print(self.name + " te abraza también")
