
from random import shuffle, randint

class HackProof(object):

	def __init__(self):

		self.alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		self.alphabetCaps = []
		for char in self.alphabet:
			self.alphabetCaps.append(char.upper())

		self.specialChars = ['!', '@', '#', '$', '%', '^', '&', ',', '*', '(', ')', '-', '+', '=', '[', ']', ':', ';', '"', "'", " ", "_", '.']
		self.nums = []
		for x in range(0, 10):
			self.nums.append(str(x))

		self.cypherChars = self.alphabet + self.alphabetCaps + self.specialChars + self.nums

		openFile = self.whileInput("Would you like to convert a file or open an exisiting one? 1 or 2: ", ['1', '2'])

		if openFile == '1':

			fileName = input("File name: ")
			
			fileName = self.formatFileName(fileName)

			self.shiftLength = randint(1, len(self.cypherChars) - 1)

			fileUser = input("What is your userName: ")

			filePass = input("What is your password: ")

			file = open(fileName, 'r')
			data = file.readlines()
			file.close()

			data = self.joinList(["{}_{}\n".format(fileUser, filePass)], data)
			
			data = self.encrypt(data)

			data = self.joinList(["{}\n".format(self.numEncrypt(self.shiftLength))], data)

			file = open(fileName, 'w')
			file.writelines(data)
			file.close()

		else:
			fileName = input("File name: ")
			fileName = self.formatFileName(fileName)

			file = open(fileName, 'r')

			fileUser = input("What is your userName: ")
			filePass = input("What is your password: ")

			data = file.readlines()
			self.shiftLength = self.decryptNum(data[0].strip('\n'))

			passAndUser = self.decrytLine(data[1]).split('_')
			passAndUser[1] = passAndUser[1].strip('\n')

			if fileUser == passAndUser[0] and filePass == passAndUser[1]:
				
				temp = []
				del data[0]
				del data[0]
				for line in data:
					temp.append(self.decrytLine(line))

				file = open(fileName, 'w')
				file.writelines(temp)
				file.close()


	def genPassword(self):

		password = []
		numLower = randint(1, 2)
		numUpper = randint(1, 2)
		numNum = randint(1, 2)
		numSpec = 8 - numLower - numUpper - numNum

		for x in range(numLower):
			password.append(self.alphabet[randint(0, len(self.alphabet) - 1)])

		for x in range(numUpper):
			password.append(self.alphabetCaps[randint(0, len(self.alphabetCaps) - 1)])

		for x in range(numNum):
			password.append(self.nums[randint(0, len(self.nums) - 1)])

		for x in range(numSpec):
			password.append(self.specialChars[randint(0, len(self.specialChars) - 1)])

		tempPassword = ""
		shuffle(password)

		tempPassword = ""
		for char in password:
			tempPassword = tempPassword + char

		return tempPassword


	def whileInput(self, inputText, correctAns):
		while 1:
			temp = input(inputText)
			if temp in correctAns:
				return temp
			print("That is not a vailid input\n")

	def encrypt(self, lst):

		tempLst = ['']

		for line in lst:
			for char in line:
				tempLst[len(tempLst) - 1] = tempLst[len(tempLst) - 1] + self.returnChar(char)

			tempLst.append('')

		del tempLst[len(tempLst) - 1]
		return tempLst

	def returnChar(self, char):
		if not char == '\n':
			pos = self.cypherChars.index(char)

			pos += self.shiftLength
			if pos >= len(self.cypherChars):
				pos = pos - len(self.cypherChars)

			return self.cypherChars[pos]
		return char

	def decryptChar(self, char):
		if not char == '\n':
			pos = self.cypherChars.index(char)

			pos -= self.shiftLength
			if pos < 0:
				pos = int(len(self.cypherChars) + pos)
			return self.cypherChars[int(pos)]
		return char

	def numEncrypt(self, num):
		return int(num) * 5 - 15
	def decryptNum(self, num):
		return (int(num) + 15) / 5

	def joinList(self, ls1, ls2):
		return ls1 + ls2

	def formatFileName(self, fileName):
		fileName = fileName.split('.txt')
		if len(fileName) == 1:
			fileName.append('.txt')
		elif len(fileName) == 2:
			fileName[1] = '.txt'

		return fileName[0] + fileName[1]

	def decrytLine(self, string):

		string2 = ""

		for char in string:
			string2 = string2 + self.decryptChar(char)

		return string2

H = HackProof()

