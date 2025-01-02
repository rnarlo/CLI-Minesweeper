import random
import os
import time

#Function to ask user for input
def Input():
	choice = str(input("Input: "))
	return choice

#Function to save progress
def save():
	global flags

	filesave = open("savefiles/DO_NOT_OPEN/savefile1.txt","w")
	filesave2 = open("savefiles/DO_NOT_OPEN/savefile2.txt","w")
	filesave3 = open("savefiles/DO_NOT_OPEN/savefile3.txt","w")
	filesave4 = open("savefiles/DO_NOT_OPEN/savefile4.txt","w")

	filesave.write(str(n)+"\n"+str(amount_of_mines))

	for element in flags:
		filesave2.write(str(element[0])+","+str(element[1])+"\n")

	for x in range(n):
		for y in range(n):
			if apparent_mines[x][y] != " ":
				filesave3.write(str(x)+","+str(y)+"\n")
			filesave4.write(str(real_mines[x][y])+"\n")

	filesave.close()
	filesave2.close()
	filesave3.close()
	filesave4.close()

#Function to load the save file
def load():
	global configuration
	global configuration2
	global configuration3
	global configuration4

	os.system("clear")
	fileopen1 = open("savefiles/DO_NOT_OPEN/savefile1.txt",'r')
	fileopen2 = open("savefiles/DO_NOT_OPEN/savefile2.txt",'r')
	fileopen3 = open("savefiles/DO_NOT_OPEN/savefile3.txt",'r')
	fileopen4 = open("savefiles/DO_NOT_OPEN/savefile4.txt",'r')
	configuration = []
	configuration2 = []
	configuration3 = []
	configuration4 = []

	for config in fileopen1:
		configuration.append(config)
	for lines in fileopen2:
		data = lines.split(',')
		flag_row = int(data[0])
		flag_col = int(data[1])
		configuration2.append([flag_row,flag_col])
	for lines in fileopen3:
		data = lines.split(',')
		flag_row = int(data[0])
		flag_col = int(data[1])
		configuration3.append([flag_row,flag_col])
	for element in fileopen4:
		configuration4.append(element)


	set_flags()

	fileopen1.close()
	fileopen2.close()
	fileopen3.close()
	fileopen4.close()

#Function to print the minefield complete with opened tiles
def printminefield():
	global n
	global apparent_mines

	os.system("clear")
	print()
	numbers = "       "
	for column in range(n):
		if len(str(column)) == 2:
			numbers = numbers + "      " + str(column+1)
		else:
			numbers = numbers + "       " + str(column+1)
	print(numbers)

	for row in range(n):
		numbers = "          "
		if row == 0:
			for columns in range(n):
				numbers = numbers + "________"
			print(numbers+"_")

		numbers = "          "
		for columns in range(n):
			numbers = numbers + "|       "
		print(numbers + "|")

		if row > 8:
			numbers = "     " + str(row+1) + "   "
		else:
			numbers = "      " + str(row+1) + "   "
		for columns in range(n):
			numbers = numbers + "|   " + str(apparent_mines[row][columns]) + "   "
		print(numbers + "|" + "   " + str(row+1))

		numbers = "          "
		for columns in range(n):
			numbers = numbers + "|_______"
		print(numbers + "|")

	print("\n\n")

#YXM

#Function to randomly assign mines to tiles
def mines():
	counter = 0
	while counter < amount_of_mines:
		number = random.randint(0, n*n-1)
		row = number // n                  #if a tile has a value of -1, there is a mine there
		col = number % n
		if real_mines[row][col] != -1:
			real_mines[row][col] = -1
			counter += 1

#Function to give values to tiles that don't contain mines
def fieldnumbers():
	for row in range(n):
		for col in range(n):

			if real_mines[row][col] == -1:
				continue
			if row > 0 and real_mines[row-1][col] == -1: #[CHECK TOP NEIGHBOUR TILE] the first row shouldn't be checked if there are mines there hence row > 0
				real_mines[row][col] += 1
			if row > 0 and col > 0 and real_mines[row-1][col-1] == -1: #[CHECK TOP LEFT NEIGHBOUR TILE] the first row and column shouldn't be checked hence row > 0 & col > 0
				real_mines[row][col] += 1
			if row > 0 and col < n-1 and real_mines[row-1][col+1] == -1: #[CHECK TOP RIGHT NEIGHBOUR TILE] the first row and last column shouldn't be checked hence row > 0 and col < n-1
				real_mines[row][col] += 1
			if col > 0 and real_mines[row][col-1] == -1: #[CHECK LEFT NEIGHBOUR TILE] the first column shouldn't be checked hence col > 0
				real_mines[row][col] += 1
			if col < n-1 and real_mines[row][col+1] == -1: #[CHECK RIGHT NEIGHBOUR TILE] the last column shouldn't be checked hence col < n-1
				real_mines[row][col] += 1
			if row < n-1 and real_mines[row+1][col] == -1: #[CHECK BOTTOM NEIGHBOUR TILE] the last row shouldn't be checked hence row < n-1
				real_mines[row][col] += 1
			if row < n-1 and col > 0 and real_mines[row+1][col-1] == -1: #[CHECK BOTTOM LEFT NEIGHBOUR TILE] the last row and first column shouldn't be checked hence row < n-1 and col > 0
				real_mines[row][col] += 1
			if row < n-1 and col < n-1 and real_mines[row+1][col+1] == -1: #[CHECK BOTTOM RIGHT NEIGHBOUR TILE] the last row and column shouldn't be checked hence row < n-1 and col < n-1
				real_mines[row][col] += 1

#Function to select the row
def select_row():
	x = int(input("            Row: "))
	if x > n or x == 0:
		return None
	if x == 1:
		return 0
	else:
		return x-1

#Function to select the column
def select_column():
	x = int(input("            Column: "))
	if x > n or x == 0:
		return None
	if x == 1:
		return 0
	else:
		return x-1

#Function to open the tile
def open_tile():
	os.system("clear")
	print("            If you want to cancel, just input an already open tile.")
	printminefield()
	row = select_row()
	col = select_column()
	if row == None or col == None:
		print("            Wrong input!")
		time.sleep(1.5)
	else:
		apparent_mines[row][col] = real_mines[row][col]
		if apparent_mines[row][col] == -1:
			apparent_mines[row][col] = "M"
			for x in range(n):
				for y in range(n):
					if real_mines[x][y] == -1:
						apparent_mines[x][y] = "M"
			printminefield()
			print("            BOOOOOM! You lose! Thanks for playing!\n\n")
			exit()

		if apparent_mines[row][col] == 0:
			if row > 0 and real_mines[row-1][col] == 0:
				apparent_mines[row-1][col] = real_mines[row-1][col]

			if row > 0 and col > 0 and real_mines[row-1][col-1] == 0:
				apparent_mines[row-1][col-1] = real_mines[row-1][col-1]

			if row > 0 and col < n-1 and real_mines[row-1][col+1] == 0:
				apparent_mines[row-1][col+1] = real_mines[row-1][col+1]

			if col > 0 and real_mines[row][col-1] == 0:
				apparent_mines[row][col-1] = real_mines[row][col-1]
																				#this block of code searches for neighbouring 0 tiles and opens them
			if col < n-1 and real_mines[row][col+1] == 0:
				apparent_mines[row][col+1] = real_mines[row][col+1]

			if row < n-1 and real_mines[row+1][col] == 0:
				apparent_mines[row+1][col] = real_mines[row+1][col]

			if row < n-1 and col > 0 and real_mines[row+1][col-1] == 0:
				apparent_mines[row+1][col-1] = real_mines[row+1][col-1]

			if row < n-1 and col < n-1 and real_mines[row+1][col+1] == 0:
				apparent_mines[row+1][col+1] = real_mines[row+1][col+1]

#Function for adding and removing flags
def flag():
	os.system("clear")
	printminefield()
	row = select_row()
	col = select_column()
	if row == None or col == None:
		print("\n            Wrong input!")
		time.sleep(1.5)
	else:
		if apparent_mines[row][col] != " " and apparent_mines[row][col] != "F":
			printminefield()
			print("\n            There's already a number there!")
			time.sleep(1.5)
		elif [row,col] in flags:
			flags.remove([row,col])
			apparent_mines[row][col] = ' '
		else:
			flags.append([row,col])

#Function for adding the flags on the field
def set_flags():
	for element in flags:
		row = element[0]
		col = element[1]
		if [row,col] in flags:
			apparent_mines[row][col] = "F"

#Function for save file to add the visible tiles on the field
def set_apparent():
	for element in forApparent:
		row = element[0]
		col = element[1]
		apparent_mines[row][col] = real_mines[row][col]

#Function for save file to give values to the tiles
def set_real():
	counter = 0
	while counter < n:
		for row in range(n):
			for col in range(n):
				real_mines[row][col] = int(forReal[counter])
				counter += 1

#Function to check if the game is over
def submit():
	global n
	global amount_of_mines

	compare = (n * n)
	compare = compare - amount_of_mines
	counter = 0
	for row in range(n):
		for col in range(n):
			if apparent_mines[row][col] != " " and apparent_mines[row][col] != "F":
				counter += 1
	if counter == compare:
		print("\n            WOOOO! Game over! Thank you so much for playing!\n            Thank you, to the professors, for this semester.\n            I hope you had fun! <3\n\n")
		time.sleep(1.5)
		exit()
	else:
		print("\n            Game is still not over.")
		time.sleep(1.5)




#The data needed for the game
n = 0
amount_of_mines = 0
flags = []
forApparent = []
forReal = []

os.system("clear") #this line of code clears the terminal
print("\nWelcome to Minesweeper!\n")
print("***MAKE SURE YOUR TERMINAL IS MAXIMISED***\n")
print("What do you want to do?")
print("1) 8x8   (10 mines)\n2) 10x10 (40 mines)\n3) 16x16 (60 mines)\n4) Load Save File\n")
gridsize = Input()

if gridsize == '1':
	n = n + 8
	amount_of_mines += 10
elif gridsize == '2':  #n is the grid size
	n = n + 10
	amount_of_mines += 40
elif gridsize == '3':
	n = n + 16
	amount_of_mines += 60
elif gridsize == '4':
	load()
	n = int(configuration[0])
	amount_of_mines = int(configuration[1])
	for x in configuration2:
		flags.append(x)
	for x in configuration3:
		forApparent.append(x)
	for x in configuration4:
		forReal.append(int(x))
else:
	print("Invalid input! Reload the program and try again.")
	gameover = True
	exit()


real_mines = [[0 for y in range(n)] for x in range(n)]		 #this list takes care of the tiles' values that are not shown to the player
apparent_mines = [[' ' for y in range(n)] for x in range(n)] #this list takes care of what's shown to the player

if gridsize == '1' or gridsize == '2' or gridsize == '3':
	mines()
	fieldnumbers()
elif gridsize == '4':
	set_real()

set_apparent()
set_flags()

gameover = False

while not gameover:
	printminefield()
	print("            What do you want to do?\n\n            'open' will prompt you to open a tile.\n            'flag' will prompt you to set (or remove) a flag on a tile.\n            'save' will save your game.\n            'exit' will quit your game without saving.\n            'submit' will check if your game is over.")
	tile = input("\n            Input: ").lower()
	if tile == "save":
		os.system("clear")
		printminefield()
		choice = input("            Are you sure you want to overwrite your save file?\n            There's no going back! [Y/N]\n            Choice: ").lower()
		if choice == "y":
			save()
			continue
		elif choice == "n":
			continue
		else:
			print("\n            Invalid input. Defaulting to no.")
			time.sleep(1.5)
			continue
	elif tile == "open":
		open_tile()
	elif tile == "flag":
		flag()
	elif tile == "exit":
		os.system("clear")
		printminefield()
		choice = input("            Are you sure you want to exit? (Make sure you saved) [Y/N]\n            Choice: ").lower()
		if choice == "y":
				print("\n            Thanks for playing!\n")
				exit()
		elif choice == "n":
			continue
		else:
			print("\n            Invalid input. Defaulting to no.")
			time.sleep(1.5)
			continue
	elif tile == "submit":
		submit()
	else:
		print("\n            Wrong input! Try again.")
		time.sleep(1)
		continue
	set_flags()
