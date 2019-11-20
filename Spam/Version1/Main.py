
from random import randint

menu = ['Burger and chips', 'Fish and chips', 'Hotdog', 'Fried Egg', 'Boiled Eggs', 'Sausages and Gravy']

for x in range(len(menu)):
	try:

		if menu[x].split()[1] == 'and':
			choice = randint(0, 1)
			if choice == 1:
				menu[x] = "Spam with {}".format(menu[x])
			else:
				menu[x] = "{}, Spam {} {}".format(menu[x].split()[0], menu[x].split()[1], menu[x].split()[2])


		else:
			menu[x] = "{} with Spam".format(menu[x])
	except:
		menu[x] = "{} with Spam".format(menu[x])

	print(menu[x])
