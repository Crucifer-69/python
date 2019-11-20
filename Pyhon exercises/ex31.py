door = input("You enter a dark room with two doors. Do you go through door #1 or door #2\n> ")

if door == "1":
	print("There's a giant bear here eating cheese cake. Waht do you do")
	bear = input("1. Take the cake \n2. Scream at the bear\n> ")

	if bear == "1":
		print("The bear eats your face off. Good job")
	elif bear == "2":
		print("The bear eats your legs off. Good job")
	else:
		print("Well, doing {} is probably better. Bear runs away.".format(bear))

elif door == "2":
	print("You stare into the endless abyss at Cthulu's retana.")
	insanity = input("1. Blueberries\n2. Yellow jacket clothspins\n3. Understanding revolvers yelling melodies.\n> ")

	if insanity == "1" or insanity == "2":
		print("your body survives powered by a mind of jello. Good job!")
	else:
		print("The insanity rots your eyes into a pool of muck. Good job!")

else:
	print("You stumble around and fall on a knife and die. Good job!")