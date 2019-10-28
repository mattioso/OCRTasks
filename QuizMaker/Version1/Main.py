
import random

#Open the file containing the questins
file = open("Questions.txt", "r", encoding="utf8",)

#Get a list of all the text in the file
lines = file.readlines()

#Close the file
file.close()

#Delete the first element as it is blank
del lines[0]

#Set up a questions and an answers list
questions = []
answers = []

#Create a variable that can count through wether an element is a question, an answer or a blank space
toList = 0
#Iterate through all elements of the list
for x in range(len(lines)):
	#If the element is a question, append it to the questions list
	if toList == 0:
		questions.append(lines[x].strip())
	#If the element is an answer, append it to the answers list
	elif toList == 1:
		answers.append(lines[x].strip())

	#If toList queals 2 set it 0
	if toList == 2:
		toList = 0
	#else add 1 to toList
	else:
		toList += 1

#Create a list to hold the number of the questions that will be asked
questionNumbers = []

#Iterate through the num of questions to be asked
for x in range(5):

	#Set num to a randint between
	num = random.randint(0, len(questions))

	#If/While num is in questions numbers, num = randint between 0 and the len of questions
	#This is to prevent repeate questions
	while num in questionNumbers:
		num = random.randint(0, len(questions))

	#Append num to questions
	questionNumbers.append(num)

#Set a score to 0
score = 0

#Iterate through the question nums
for x in range(len(questionNumbers)):
	#Print the question
	print(questions[questionNumbers[x]])
	#Request an answer
	answer = input("Answer: ")

	#Make everything lowercase and check if the answer is equal to the questions answer
	if answer.lower() == answers[questionNumbers[x]].lower():
		#If it is, add one to score and print correct
		score += 1
		print("Correct!\n")

	#Else, print false
	else:
		print("False\n")

#Finally, print the score
print("Your score was: {}".format(score))

