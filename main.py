import os
import time
import datetime


LEVELS = {
	"Easy" : [7, 3],
	"Normal" : [20, 6],
	"Hard" : [27, 9]
}

FIELD = []
CHOSEN_LEVEL = "none"
FLAGS_USED = 0
FLAGS_CAN_USE = 0
STARTED = False

SQUARE = 0
MINES = 0
GAME_START = 0
ISDEAD = False

clear = lambda: os.system('clear')


def generateField(number):
	# Since it is square, we need the number only once
	# Since it is square, we need the number only once
	# x for rows, y for columns
	FIELD = [[0 for x in range(number)] for y in range(number)]
	
	#for row in range(number):
		#for col in range(number):
			
		#print(" ".join(row[0]))
	#for row in range(number):
		#print("\n_________\n|       |\n|   B   |\n|       |".join(*row))
	#	print(" x ".join(row))
	
	for x in range(number):
		print('____'*number)
		print('   |'*number)
		print(' x |'*number)
		print('   |'*number)
	return ' '




def startGame():
	minutes = 0
	print("---- MINEFINDER GAME by Peter Till ----\n")
	print("""
	LEVELS \n
	[Easy] - 12x12, 3 mines \n
	[Normal] - 20x20 6 mines \n
	[Hard] - 27x27 9 mines \n
	""")
	chosenlvl = input("Please choose a level! \n MINEFINDER>")
	clear()
	GAME_START = time.time()
	while True:
		try:
			CHOSEN_LEVEL = chosenlvl
			SQUARE = LEVELS[str(chosenlvl)][0]
			MINES = LEVELS[str(chosenlvl)][1]
			STARTED = True
			end = time.time()
			print("---- MINEFINDER GAME by Peter Till ----\n")
			gametime = round(end - GAME_START)
			formated = datetime.timedelta(seconds=gametime)
			print(f"Level: {CHOSEN_LEVEL} | Field size: {SQUARE}x{SQUARE} | Mines placed: {MINES} | Time elapsed: {formated}")
			print(generateField(SQUARE))
			step = input("ACTION>")
			clear()
		except(Exception, e):
			print("You have provided wrong details. Please ty again!")
			print(e)
			startGame()
		
	
startGame()
