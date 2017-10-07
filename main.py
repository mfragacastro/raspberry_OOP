from room import Room
from character import Enemy, Character, Friend
from item import Item

# Create rooms
kitchen = Room("Cocina")
kitchen.set_description("Una oscura y húmeda habitacion con el zumbido de cientos de moscas.")

dinning_hall = Room("Comedor")
dinning_hall.set_description("Un lugar tenuemente iluminado por candelabros a punto de agotarse.")

ballroom = Room("Ballroom")
ballroom.set_description("La bitación de las bolas")

kitchen.link_room(dinning_hall,"south")

dinning_hall.link_room(kitchen,"north")
dinning_hall.link_room(ballroom,"west")

ballroom.link_room(dinning_hall,"east")

# Create characters and assing them to rooms
# Chicho
chicho = Enemy("Chicho", "Un apestoso zombi")
chicho.set_conversation("Eres lo peor que nos ha pasado nunca")
chicho.set_weakness("Chocos")

dinning_hall.set_character(chicho)

chicho.set_items(["lobos","dragones","mandriles"])

# Catrina
catrina = Friend("Catrina", "Una amistosa esqueleto")
catrina.set_conversation("¿Hay alguien ahí?")
ballroom.set_character(catrina)

# Create items and assign it to rooms
# Chocos
chocos = Item()
chocos.set_name("Chocos")
chocos.set_description("Cefalópodos recién pescados")

ballroom.set_item(chocos)

# Comienza el bucle de la partida

current_room = kitchen
#mochila = []

dead = False

while dead is False:
	print("\n")
	current_room.get_details()
	ocupante = current_room.get_character()
	cosa = current_room.get_item()
	if ocupante is not None:
		ocupante.describe()
	if cosa is not None:
		cosa.describe()
	command = input("> ")
	if command in ["north","south","east","west"]:
		#Acciones de movimiento
		current_room = current_room.move(command)
	elif command == "talk":
		ocupante.talk()
	elif command == "steal":
		if isinstance(ocupante,Enemy):
			print("El enemigo tiene estos artículos: ")
			print(*ocupante.get_items(), sep=",")
			print("¿Qué quieres robar?")
			objeto = input("> ")
			ocupante.roba_item(objeto)
		else:
			print("No se debe de robar a buenas gentes")
	elif command == "fight":
		print("¿Qué arma quieres usar?")
		arma = input("> ")
		for cosa in Item.mochila:
			if arma == cosa.get_name():
				if ocupante.fight(arma) == True:
					current_room.set_character(None)
					del ocupante
				else:
					dead = True
					print("Juego terminado ... has perdido")
			else:
				print("Tu mochila no contiene eso")
				print("Usa el comando list")
	elif command == "abrazar":
		if isinstance(ocupante, Enemy):
			print("Yo no haría eso si fuera tú...")
		else:
			ocupante.hug()
	elif command == "take":
		if cosa is not None:
			Item.mochila.append(cosa)
			current_room.set_item(None)
		else:
			print("No hay objetos en esta habitación")
	elif command == "list":
		if len(Item.mochila) > 0:
			for obj in Item.mochila:
				print(obj.get_name())
		else:
			print("No hay objetos en tu mochila")
			
