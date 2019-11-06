
#Start the while loop
while 1:

	#Ask the user for input
	print("What task would you like to perform")
	task = input("0 to quit, 1 for entering data, 2 to retrieve all data, 3 for searching for specific users: ")

	#If the user wants to quit, quit
	if task == "0":
		break

	#ELse if the user wants to add data 
	elif task == "1":

		#Start a new while loop so if the data is incorrectly entered the user can renter it
		while 1:
			#Ask for the relevent data
			name = input("Name: ")
			dob = input("Date of birth: ")
			postcode = input("Postcode: ")

			#Ask for confirmation
			confirm = input("To confirm press 1, to reneter press 2:\nYour name is: {}\nYour date of birth is: {}\nAnd your postcode is: {}\n".format(name, dob, postcode))

			#If the data is confirmed, append it to the txt file and break from the loop
			if confirm == "1":
				file = open("data.txt", "a")
				file.write("{}-{}-{}\n".format(name, dob, postcode))
				file.close()
				break

	#Both task 2 and task 3 need the data formated
	elif task == "2" or task == "3":

		#Open the file and retrive the data 
		file = open("data.txt", "r")
		fileData = file.readlines()
		file.close()

		#Iterate through the list of data from the file
		for x in range(len(fileData)):
			#Remove all \n's and set the element of the list to the data split at the -'s
			fileData[x] = fileData[x].strip().split("-")

		#If it is the second task
		if task == "2":

			#Iterate through the list
			for lst in fileData:
				#Print the relevent data
				print("\nName: {}\nDate Of birth: {}\nPostcode: {}\n".format(lst[0], lst[1], lst[2]))

		#If it is the third
		elif task == "3":

			#Ask what type of search is needed, only for the inputs
			searchType = input("1 to search for names, 2 to search for date of birth, 3 to search for postcode: ")

			#Get an input from the user
			if searchType == "1":
				search = input("What name are you looking for: ")
			elif searchType == "2":
				search = input("What date of birth are you looking for: ")
			elif searchType == "3":
				search = input("What postcode are you looking for: ")
			
			#Iterate through the list
			for lst in fileData:
				#Check of the element is in the list
				if search in lst:
					#If it is, print the entire list
					print("\nName: {}\nDate Of birth: {}\nPostcode: {}\n".format(lst[0], lst[1], lst[2]))
