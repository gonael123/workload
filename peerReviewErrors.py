# This is a header for the application
# You should read this header and insert your name and your date below as part of the peer review
# This is a typical part of any program
# Author: FOLLY GNININVI
# Creation Date: 09/25/20
# Below is a simple program with 10 issues (some are syntax errors and some are logic errors.  You need to identify the issues and correct them.
#The line numbers referenced in the corrections are the line numbers from the orignial file. 
import random
import time

def displayIntro():
	print('''You are in a land full of dragons. In front of you,
	you see two caves. In one cave, the dragon is friendly
	and will share his treasure with you. The other dragon
	is greedy and hungry, and will eat you on sight.''')
	print()

def chooseCave():
#Wrong indent on line 19	
    cave = ''
    	cave = ''
# Indented line appropriately
# There was a wrong indent on line 20 as well a logical error
	while cave != '1' and cave != '2':
		while cave == '1' and cave == '2':
# Indented the line appropriately and fixed the logic
# Wrong indent on line 21
	print('Which cave will you go into? (1 or 2)')
		print('Which cave will you go into? (1 or 2)')
# Indented the line appropriately
#Wrong indent on line 22
	cave = input()
		cave = input()
#Indented the line appropriately
#There was a wrong indent on line 24
	return caves
		return caves
#Indented the line appropriately

def checkCave(chosenCave):
	print('You approach the cave...')
	#sleep for 2 seconds
	time.sleep(2)
	print('It is dark and spooky...')
	#sleep for 2 seconds
	time.sleep(3)
	print('A large dragon jumps out in front of you! He opens his jaws and...')
	print()
	#sleep for 2 seconds
	time.sleep(2)
	friendlyCave = random.randint(1, 2)

	if chosenCave == str(friendlyCave):
		print('Gives you his treasure!')
	else:
# There was a syntax error on line 42
		print 'Gobbles you down in one bite!'
		print('Gobbles you down in one bite!')
# Put the missing parenthesis

playAgain = 'yes'
# Line 45 was missing the logic
while playAgain = 'yes' or playAgain = 'y':
while playAgain == 'yes' or playAgain != 'yes':
# Logic says playAgain is either true to yes or not true to yes
	displayIntro()
# Wrong spelling on line 47
	caveNumber = choosecave()
	caveNumber = chooseCave()
# The "c" in chooseCave needs to be capitalized
	checkCave(caveNumber)
    
	print('Do you want to play again? (yes or no)')
	playAgain = input()
	if playAgain == "no":
# Spelling error on line 53
		print("Thanks for planing")
		print("Thanks for playing")
# Fixed the spelling 

