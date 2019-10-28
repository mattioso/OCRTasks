
import pygame, sys
#Pyaame locals for the keyclicks
from pygame.locals import *

#The main class of the object
class Aid(object):

	#Constructor to pass the variables to create the screen
	def __init__(self, width, height, backcolour=(70, 70, 70)):

		#Set the size of the screen
		self.size = self.width, self.height = width, height
		#Set the pygame clock up to limit fps
		self.clock = pygame.time.Clock()

		#Initialize the pygame module
		pygame.init()
		#Set the screen to a pygame display with the size given
		self.screen = pygame.display.set_mode(self.size)

		#Create an array to hold the names of the rectangles added
		self.images = []

		#Set the colour to the given colour
		self.colour = backcolour

	#Define a function to add new rects to the instance
	def addRect(self, name, imgLoc="", width="", height="", colour=(255, 0, 0), layer=0):

		#Check to make sure at least one set of parameters needed for the creation of the rectangle is provided
		if imgLoc == "" and width == "" and height == "":
			raise Exception("Either a location or dimensions should be specified")

		#Start a try except
		try:
			
			#Check if the given value is a list
			imgLoc[0]

			#Create a temporary empty list 
			self.tempImages = []

			#Iterate through the values given
			for loc in imgLoc:
				#Add the pygame image to the temp images list
				self.tempImages.append(pygame.image.load(loc))

			#Set a variable to the name given
			setattr(self, name, Rectangle(image=self.tempImages))

			#Delete the temp image list
			del self.tempImages

		except:
			#If the width and the height have been given
			if not width == "" and not height == "":
				setattr(self, name, Rectangle(width=width, height=height, colour=colour))
			
			#If the image location has been given
			else:
				setattr(self, name, Rectangle(image=pygame.image.load(imgLoc)))

		self.addImage(name, layer)

	#Create a function to create text on the screen easily
	def addText(self, name, text, size, layer, font="monospace", colour=(255, 255, 255)):

		#Set a varible to the given name
		setattr(self, name, Text(text, size, font, colour))

		#Add the image to the images list
		self.addImage(name, layer)

	#Create a function to add buttons to the text easily
	def addButton(self, name, layer, imgLoc="", width="", height="", size=20, text="", font="monospace", colour=(255, 0, 0), txtColour=(255, 255, 255)):

		#Similar code to the rectangle function
		if imgLoc == "" and width == "" and height == "":
			raise Exception("Either a location or dimensions should be specified")
		#If an image is passed
		if not imgLoc == "":
			#Start a try except
			try:
			
				#Check if the given value is a list
				imgLoc[0]

				#Create a temporary empty list 
				self.tempImages = []

				#Iterate through the values given
				for loc in imgLoc:
					#Add the pygame image to the temp images list
					self.tempImages.append(pygame.image.load(loc))
				
				#Set a button class to the given name
				setattr(self, name, Button(img=self.tempImages, text=text, size=size, font=font, txtColour=txtColour))

				#Delete the tempary images list
				del self.tempImages

			#If it is not a list of values
			except:
				#Set the name to the Button value
				setattr(self, name, Button(img=pygame.image.load(imgLoc), text=text, size=size, font=font, txtColour=txtColour))

		#If an image ins't passed
		else:
			#Set the variable name to a button with width and height
			setattr(self, name, Button(width=width, height=height, text=text, size=size, font=font, colour=colour, txtColour=txtColour))

		#Add the image
		self.addImage(name, layer)
	
	#Define a function to add images to the images list
	def addImage(self, name, layer):
		try:
			self.images[layer].append(name)
		#If that list doesn't exist
		except:
			#Start a while loop
			while 1:
				#Try to add the layer in again
				try:
					self.images[layer].append(name)
					#If the name is added, break out of the loop
					break
				except:
					#If the layer list is not present, add another list to images
					self.images.append([])

	#Define a function to run the commands the need running last in a game loop
	def closingCommands(self):

		#If the x is pressed
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		#Use the pygame clock function to limit the to 60 fps
		self.clock.tick(60)
		#Update the display
		pygame.display.update()

	def draw(self):

		#Fill the screen with colour
		self.screen.fill(self.colour)

		#For every rectangle in rectangles array
		for rects in self.images:
			#Iterate through the layers, so the game is drawn in the desired order
			for layers in rects:
				#Check if the rectangle wants to be drawn
				if eval("self.{}".format(layers)).drawing:
					#If the rectangle has an image to draw, or is a button
					if eval("self.{}".format(layers)).type == 0 or eval("self.{}".format(layers)).type == 2 or eval("self.{}".format(layers)).type == 4:
						#Draw the image
						self.screen.blit(eval("self.{}".format(layers)).image, eval("self.{}".format(layers)).rect)
					#If the rectangle has no image
					if eval("self.{}".format(layers)).type == 1:
						#Draw a block coloured rectangle
						pygame.draw.rect(self.screen, eval("self.{}".format(layers)).colour, eval("self.{}".format(layers)).rect)

					#If the eval is text
					if eval("self.{}".format(layers)).type == 3:
						self.screen.blit(eval("self.{}".format(layers)).renderedText, (eval("self.{}".format(layers)).x, eval("self.{}".format(layers)).y))

					#If the eval is a button
					if eval("self.{}".format(layers)).type == 5:
						#Draw the rectangle
						pygame.draw.rect(self.screen, eval("self.{}".format(layers)).colour, eval("self.{}".format(layers)).rect)
						#Draw the text
						self.screen.blit(eval("self.{}".format(layers)).text.renderedText, (eval("self.{}".format(layers)).text.x, eval("self.{}".format(layers)).text.y))

	#Define an update function
	def update(self):

		#Iterate through the rectangles in the rectangle array
		for rects in self.images:
			#Go through the layers
			for layers in rects:
				#Update every rectangle given
				if not eval("self.{}".format(layers)).type == 3:
					eval("self.{}".format(layers)).update()

		#Run the draw function
		self.draw()
		#Run the closing commands function
		self.closingCommands()

	#Return the pressed keys
	def getKeys(self):
		return pygame.key.get_pressed()

	#Return the mouse pos
	def getMousePos(self):
		return pygame.mouse.get_pos()

	#Return the pressed mouse keys
	def getMouseButtons(self):
		return pygame.mouse.get_pressed()

#Define a class to handle rectangles
class Rectangle(object):

	#Define the constructor
	def __init__(self, width="", height="", image=None, colour=(255, 0, 0)):

		#Start a try except
		try:
			
			#Make sure the image given is a list
			image[0]

			#Set a list to the list of images given
			self.images = image
			#Set an empty list to hold the rectangles of the different objects
			self.rects = []

			#Iterate through the images and add the rects of those images to the rects list
			for img in image:
				self.rects.append(img.get_rect())

			#Set the current image and rectangle to the first image and rectangle in the list
			self.image = self.images[0]
			self.rect = self.rects[0]

			#Set the width and height to the values
			self.width = self.rect.width
			self.height = self.rect.height

			#Set the type to 2
			self.type = 2

		except:
			#if an image has been passed
			if width == "" and height == "":
				#Set the image to the image given
				self.image = image
				#Get a rectangle of the image
				self.rect = self.image.get_rect()
				#Set the width and height variables to the width and height of the rectangle
				self.width = self.rect.width
				self.height = self.rect.height
				#Set the type to 0
				self.type = 0

			#If a set of value have been given
			else:
				#Set up the rectangle manually
				self.rect = Rect(0, 0, width, height)
				#Set the width and height variables to the values given
				self.width = width
				self.height = height
				#Set the type to 1
				self.type = 1
				#Set the colour to the given colour
				self.colour = colour

		#Set up speed variables
		self.speed = [0, 0]
		#Set x and y to 0
		self.x = 0
		self.y = 0
		#Set a variable that can be turned off to make the rectangle not draw
		self.drawing = True

	#Update the rect
	def update(self):

		#Add the speed variables to the x and y
		self.x += self.speed[0]
		self.y += self.speed[1]

		#Update the rect positions 
		self.rect.x = self.x
		self.rect.y = self.y

	#Create a collide function
	def collide(self, Rectangle):

		return self.rect.colliderect(Rectangle.rect)

	#Create a function to set the image to the given value when animation is possible
	def setImage(self, num):

		#Raise an error if the rectangle cant be animated
		if not self.type == 2 and not self.type == 4:
			raise Exception("Only animatable images can use this function")

		if self.type == 4:
			try:
				self.images[0]
			except:
				raise Exception("Only animatable images can use this function")

		#Raise an error if the given number is bigger than the size of the list
		if num > len(self.images) - 1:
			raise Exception("Given number exceeds the list size")

		#Set the current image and rectangle to the given number
		self.image = self.images[num]
		self.rect = self.rects[num]

		#Set the width and the height to the different values
		self.width = self.rect.width
		self.height = self.rect.height

	#Check if the rectangle is being pressed
	def pressed(self, mousePos, mouseButtons):
		return mouseButtons[0] == 1 and self.inBox(mousePos)

	#Check if the mouse is over the rectangles
	def inBox(self, mousePos):
		return self.x < mousePos[0] < self.x + self.width and self.y < mousePos[1] < self.y + self.height

#Create a class to handle text displays
class Text(object):

	#Run the constructor
	def __init__(self, text, size, font, colour):

		#Save the text and colour
		self.text = text
		self.colour = colour

		#Try to access a sys font 
		try:
			self.font = pygame.font.SysFont(font, size)
		#If not, import from a font file
		except:
			self.font = pygame.font.Font(font, size)

		#Render the text
		self.renderedText = self.font.render(self.text, 1, self.colour)

		#Set the x and y to 0 
		self.x = 0
		self.y = 0
		#Get the width and height
		self.width = self.renderedText.get_width()
		self.height = self.renderedText.get_height()
		
		#Set the drawing and type variables
		self.drawing = True
		self.type = 3

	#A function to change the displayed text
	def setText(self, text):
		#Save the new text value
		self.text = text
		#Re-render the text
		self.renderedText = self.font.render(self.text, 1, self.colour)
		self.width = self.renderedText.get_width()
		self.height = self.renderedText.get_height()

#Define a class to create buttons
class Button(Rectangle):

	def __init__(self, img="", width="", height="", text="", size="", font="", colour="", txtColour=""):

		#Super the rectangle class
		#This allows for the use of lists of images as well
		super().__init__(image=img, width=width, height=height, colour=colour)
		
		#If an image is given, set the type to 4
		if not img == "":
			self.type = 4

		#If no image is given
		else:
			#Set the type to 5
			self.type = 5
			#Create a text object
			self.text = Text(text, size, font, txtColour)

		#Set active to false
		self.active = False

	#Create an update function
	def update(self):
		#Super the higher fuction
		super().update()
		#If text is drawn seperatly
		if self.type == 5:
			#Set the x and the y of the text to the middle of the rectangle
			self.text.x = self.x + self.width / 2 - self.text.width / 2
			self.text.y = self.y + self.height / 2 - self.text.height / 2