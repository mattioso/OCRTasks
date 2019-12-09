
from random import randint, shuffle

global alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
global alphabetCaps
alphabetCaps = []
for char in alphabet:
	alphabetCaps.append(char.upper())

global specialChars
specialChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '=', '[', ']', ':', ';', '"', "'"]
global nums
nums = []
for x in range(0, 10):
	nums.append(str(x))

def genPassword():
	global alphabet
	global alphabetCaps
	global specialChars
	global nums
	password = []
	numLower = randint(1, 2)
	numUpper = randint(1, 2)
	numNum = randint(1, 2)
	numSpec = 8 - numLower - numUpper - numNum

	for x in range(numLower):
		password.append(alphabet[randint(0, len(alphabet) - 1)])

	for x in range(numUpper):
		password.append(alphabetCaps[randint(0, len(alphabetCaps) - 1)])

	for x in range(numNum):
		password.append(nums[randint(0, len(nums) - 1)])

	for x in range(numSpec):
		password.append(specialChars[randint(0, len(specialChars) - 1)])

	shuffle(password)

	tempPassword = ""
	for char in password:
		tempPassword = tempPassword + char

	return tempPassword

def checkPassword(password):
	global alphabet
	global alphabetCaps
	global specialChars
	global nums

	score = [0, 0, 0, 0]

	if not len(password) >= 8:
		return False

	for char in password:
		if char in alphabet:
			score[0] += 1
		elif char in alphabetCaps:
			score[1] += 1
		elif char in specialChars:
			score[2] += 1
		elif char in nums:
			score[3] += 1

	if 0 in score:
		return False

	return True

while 1:
	createFile = input("Create file? y/n: ")
	if createFile == 'y' or createFile == 'n':
		break

if createFile == 'y':

	fileName = input("File Name: ")
	userName = input("User Name: ")

	print("A good password would be: {}".format(genPassword()))

	while 1:
		password = input("Password: ")
		if checkPassword(password):
			break

		else:
			print("Too weak a password. A password needs a lowercase letter, an upper case letter, a number and a special charicter")

	text = input("What would you like the file to say: ")

	file = open(fileName, 'w')
	file.write("{}\n{}\n{}".format(userName, password, text))
	file.close()

elif createFile == 'n':
	while 1:
		openFile = input("Open file? y/n: ")
		if openFile == 'y' or openFile == 'n':
			break

	if openFile == 'y':

		fileName = input("File Name: ")
		userName = input("User Name: ")
		password = input("Password: ")

		file = open(fileName, 'r')
		data = file.readlines()
		file.close()

		for x in range(len(data)):
			data[x] = data[x].strip()

		if data[0] == userName and data[1] == password:
			del data[0]
			del data[0]
			for line in data:
				print(line)