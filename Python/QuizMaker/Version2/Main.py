
#Import needed modules
from PygameAid import *
import random

#Cretae a new aid object of size 800x800 and set the variable to be global
global G
G = Aid(800, 800)

#Create a funtion to return a shuffle list of the given list
#Created instead of using the random list suffler as an error occured when trying to set the same variable to the result
def listShffle(givenList):
	#Create an empty array to hold the suffled list
	newList = [] 
	#Iterate through the length of given list
	for x in range(len(givenList)):
		#Create a varibale to hold the chosen element of the list
		choice = random.choice(givenList)
		#Remove the choice from the main list
		givenList.remove(choice)

		#Append the choice to the list
		newList.append(choice)

	#Return the suffled list
	return newList

#Create a function to seperate a list by word so 'This is an example' becomes ['This', 'is', 'an', 'example']
def seperateByWord(text):

	#Create a list to hold the seperated list
	seperatedText = ['']

	#Iterate through every character in the given string
	for char in text:
		#If the char is an empty space
		if char == ' ':
			#Add an empty string to the seperated text list
			seperatedText.append('')
		else:
			#Add the char to the last element of the list
			seperatedText[len(seperatedText) - 1] = seperatedText[len(seperatedText) - 1] + char

	#Return seperated text
	return seperatedText

#Create a function to turn a list of words into a single string eg: ['This', 'is', 'an', 'example'] becomes This is an example'
def listToString(toConvert):

	#Set text to the first element of the list
	text = toConvert[0]

	#Iterate through 1 to the length of the list
	for x in range(1, len(toConvert)):
		#Add the word to the text
		text = "{} {}".format(text, toConvert[x])

	#Return the string
	return text

#Create a function to one line of text onto multiple pygame lines
def relineText(text):
	#Using global G
	global G
	#Set text to the return of seperateByWord from the given string
	text = seperateByWord(text)
	#Set the number of words to 0
	numOfWords = 0

	#Set a y to the first text elemet
	texty = 0
	#Set current line to an empty stirng
	currentLine = ""

	#Create a list to hold the lines
	lines = []

	#While the number of words is less the the len of text
	while numOfWords < len(text):

		#Add the next word the the current line of text
		currentLine = "{} {}".format(currentLine, text[numOfWords])

		#Create a new Aid text element called text
		G.addText("test", currentLine, 40, 2)
		#Set it to not be drawn
		G.test.drawing = False

		#If the width of the entire screen is less than the width of the current line
		if G.width < G.test.width:
			#Seperate current line
			currentLine = seperateByWord(currentLine)
			#Delete the first and last elements
			del currentLine[0]
			del currentLine[len(currentLine) - 1]

			#Turn the list back to a string
			currentLine = listToString(currentLine)
			#Append the string to current line
			lines.append(currentLine)
			#Reset the current line
			currentLine = ""	
			#Minus one to the words
			numOfWords -= 1
		#Add one to numOfWords
		numOfWords += 1

	#Delete the first element of the string
	currentLine = currentLine[1:]
	#Add the last line to lines
	lines.append(currentLine)

	#Iterate through lines
	for x in range(len(lines)):
		#Add the line to G
		G.addText("line{}".format(x), lines[x], 40, 2)
		#Set the y to the texty variable
		eval("G.line{}".format(x)).y = texty
		#Center the text
		eval("G.line{}".format(x)).x = G.width / 2 - eval("G.line{}".format(x)).width / 2
		#Add the height of the text to the texty var
		texty += eval("G.line{}".format(x)).height

	#Return the num of lines
	return len(lines)

#Create a function to create the four answer buttons
def createButtons(questionNum, possibleAnswers, colours):
	
	#Using global G
	global G

	#Iterate through 4 times
	for x in range(4):
		#Add a button to G
		G.addButton("button{}".format(x), 1, width=350, height=175, text=possibleAnswers[questionNum][x], colour=colours[x], txtColour=(0,0,0))

		#If its the first button, position it on the left top
		if x == 0:
			G.button0.x = 25
			G.button0.y = 300
		#Second button goes bottom left
		elif x == 1:
			G.button1.x = 25
			G.button1.y = 325 + G.button1.height
		#Third button goes top right
		elif x == 2:
			G.button2.x = G.width / 2 + 25
			G.button2.y = 300
		#Fourth button goes bottom right
		elif x == 3:
			G.button3.x = G.width / 2 + 25
			G.button3.y = 325 + G.button3.height

#Set up four colours
RED = (255, 0, 0)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

#Add these colours to a list
colours = [RED, BLUE, GREEN, YELLOW]

#Open the questions file
file = open("Questions.txt", "r", encoding="utf8")
#Get a list of all the lines
lines = file.readlines()
#Close the file
file.close()
#Delete the first (blank) element
del lines[0]

#Set up a list to hold the questions
questions = []
#Set up a list to hold the answers
correctAnswers = []
#Set up a list to hold the incorrect answers
wrongAnswers = []
#Set up a list to hold the correct answers to the specific questions
specCorrectAnswers = []

#Start three counts
#Count is for a simple count to 5 again and again
count = 0
#Count2 counts whether the wrong answers should go in a new list
count2 = 0
#Count3 counts what num in the 2d array the new line should go
count3 = 0

#Iterate through every element in the lines list
for x in range(len(lines)):

	#If the element is a question, append the string to the questions list, minus the \n
	if count == 0:
		questions.append(lines[x].strip())

	#If the element is an answer, append the string to the answers list, minus the \n
	elif count == 1:
		correctAnswers.append(lines[x].strip())

	#If the count is neither 1 or 2
	else:
		#Try to add the count3 list
		try:
			wrongAnswers[count3].append(lines[x].strip())
		#If it is out of range
		except:
			#Append a list with lines[x] to the wrong answers
			wrongAnswers.append([lines[x].strip()])

		#Count to three then back to 0
		if not count2 == 3:
			count2 += 1

		#When count2 has counted that all the wrong answers for a question have been added, it adds a new list
		else:
			count2 = 0
			count3 += 1

	#Have the first count go to 5 then back again
	if not count == 5:
		count += 1

	else:
		count = 0

#Iterate through the wrong answers and delete the unwanted space at the end
for x in range(len(wrongAnswers) - 1):
	del wrongAnswers[x][3]

#Create a list of question numbers
questionNumbers = []
#Create a list to hold the possible answers to the question
possibleAnswers = []

#Iterate through the num of question
for x in range(5):
	#Set num to a randint between 0 and 19
	num = random.randint(0, 19)

	#While that num is already in question num, pick another to prevent repeats
	while num in questionNumbers:
		num = random.randint(0, 19)

	#Add the num to question nums
	questionNumbers.append(num)
	#Add the answer to the specCorrect answers list
	specCorrectAnswers.append(correctAnswers[num])

	#Add the answer to possible answers
	possibleAnswers.append([correctAnswers[num]])
	#Add the possible answers[x] list to the wrong answers[x] list
	possibleAnswers[x] = possibleAnswers[x] + wrongAnswers[num]
	#Shuffle the possible answers list
	possibleAnswers[x] = listShffle(possibleAnswers[x])

#Run the create buttons function
createButtons(0, possibleAnswers, colours)
#Set lineNum to the number of lines for this iteration
lineNum = relineText(questions[questionNumbers[0]])

#Set up three states
states = ["Asking", "Middle", "End"]
#Set up a current state var
state = states[0]
#Set correct to false
correct = False

#Create centered text for both correct and incorrect
G.addText("correctText", "Correct!", 80, 2, colour=GREEN)
G.correctText.drawing = False
G.correctText.x = G.width / 2 - G.correctText.width / 2
G.correctText.y = G.height / 2 - G.correctText.height / 2 

G.addText("incorrectText", "Incorrect!", 80, 2, colour=RED)
G.incorrectText.drawing = False
G.incorrectText.x = G.width / 2 - G.incorrectText.width / 2
G.incorrectText.y = G.height / 2 - G.incorrectText.height / 2

#Set up a score count
score = 0
#Have a count for how long the screens in the middle will last
screenCount = 60
#Set question num to 0
questionNum = 0

#Start our game loop
while 1:

	#Get the mouse pos and the mouse buttons
	mousePos = G.getMousePos()
	mouseButtons = G.getMouseButtons()

	#If the state is Asking
	if state == states[0]:

		#Iterate through the four buttons
		for x in range(4):
			#If the button is being pressed
			if eval("G.button{}".format(x)).pressed(mousePos, mouseButtons):
				#If the buttons text is the same as the correct answer for this question
				if eval("G.button{}".format(x)).text.text == specCorrectAnswers[questionNum]:
					#Add one to the score
					score += 1
					#Set correct to true 
					correct = True
				#If the wrong button is pressed
				else:
					#Set correct to false 
					correct = False
				#Set the state to Middle
				state = states[1]
				#add one to the question num
				questionNum += 1

	#If the state is Middle
	if state == states[1]:
		#If the screen count does not = 0
		if not screenCount == 0: 
			#If the user got the correct answer
			if correct:
				#Draw the correct text
				G.correctText.drawing = True
			#If the user got the wrong answer
			if not correct:
				#Draw the incorrect text
				G.incorrectText.drawing = True

			#Iterate through the four buttons and stop drawing them
			for x in range(4):
				eval("G.button{}".format(x)).drawing = False

			#Iterate through the text lines and draw them
			for x in range(lineNum):
				eval("G.line{}".format(x)).drawing = False

			#Minis one from the screen count
			screenCount -= 1

		#If the time for the Middle screen to be up has elapsed
		if screenCount == 0:

			#If it was the last question, set the state to End
			if questionNum == 5:
				state = states[2]
			#If it was not the last question
			else:
				#Create new buttons
				createButtons(questionNum, possibleAnswers, colours)
				#Re-align the text 
				lineNum = relineText(questions[questionNumbers[questionNum]])
				#Set the state to Asking
				state = states[0]

			#Set the text to not draw
			if correct:
				G.correctText.drawing = False
			if not correct:
				G.incorrectText.drawing = False

			#Set screen count to 60
			screenCount = 60

	#If the state = End
	if state == states[2]:
		#Iterate through the buttons and set them to not draw
		for x in range(4):
			eval("G.button{}".format(x)).drawing = False

			#Iterate through the lines and set them not to draw
			for x in range(lineNum):
				eval("G.line{}".format(x)).drawing = False

		#Add the score text and align it with the center
		G.addText("scoreText", "Score: {}".format(score), 80, 2, colour=(0, 255, 0))
		G.scoreText.x = G.width / 2 - G.scoreText.width / 2
		G.scoreText.y = G.height / 2 - G.scoreText.height / 2

	#Update G
	G.update()