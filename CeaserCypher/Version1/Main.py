
global alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#This is the size of the shift that will take place
shiftSize = 10

#A function to change a string into the numerical position of it in the alphabet
def convertToNums(text):

	#Have a list to hold the text
	toReturn = [[]]
	#All the words need to be lowercase
	text = text.lower()
	#Create a var to hold what word num the program is on to track what list the char should be put in
	wordNum = 0
	global alphabet

	#Iterate through every char in the string
	for char in text:

		#If the char is a letter
		if char in alphabet:
			#Add it to the word in the toReturn list
			toReturn[wordNum].append(alphabet.index(char))

		else:
			#If the char is a space, add a new word to the toReturn list and add one to word num
			if char == " ":
				toReturn.append([])
				wordNum += 1
			else:
				#Otherwise add the char to the list as is, in case of punctuation
				toReturn[wordNum].append(alphabet.index(char))

	#return the list
	return toReturn

#Create a function to shift the list and return the cyphered text
def shift(shiftSize, text):

	#Run the convert to nums function
	text = convertToNums(text)

	#Use global alphabet
	global alphabet
	#Have a string to hold the cyhered text
	cypherString= ""

	#Iterate through the lists in text
	for x in range(len(text)):
		#Add a empty space to the cypher string every new list
		cypherString= cypherString+ " "
		#Iterate through the nums in the list inside of text
		for y in range(len(text[x])):
			#If the cypher does not need to go backwards, add it to the string
			try:
				cypherString= cypherString+ alphabet[text[x][y] + shiftSize]
			except:
				#If the cypher does need to go backwards, minus the length of the alphebet and then add shift size
				cypherString= cypherString+ alphabet[text[x][y] - len(alphabet) + shiftSize]

	#Delete the first unnecassery space
	cypherString= cypherString[1:]
	#Return the string
	return cypherString

#Create a string to hold the test
testString = "This is a test"
#Get the returned string
shifted = shift(shiftSize, testString)
#Print the returned string
print(shifted)
