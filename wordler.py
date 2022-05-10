"""

Author: Arnav Priyadarshi
A Functional programming approach to solving wordle.
Take all possible english words, take all the 5 letter ones, then for every
guess and its information, filter the list more and more until we're left with less than 10 final solutions.
This is a hinter primarily, so it's meant to be fed some information if you've been strugggling, and suggest
an answer that is quite close to being correct, it can and will just get the correct answer if you feed enough different
guesses or a guess that is close to the answer.
"""

# with open("words.txt", encoding="utf-8") as dictionary:
# 	with open("wordles.txt", "w", encoding="utf-8") as tofill:
# 		for line in dictionary:
# 			if len(line) == 6:
# 				tofill.write(line)
# To get the 5 letter words from our words file

import random

def doesNotContainLetter(word, letter):
	# Use for blacks in wordle
	for char in word:	# Don't check if the type is an int, because then it means it was a green or orange
		if(char==letter):
			return False
	return True # true if letter is not in word

def correctGreenLetter(word, letter, index):
	if(type(word[index]) == int):
		return chr(word[index]) == letter
	if(word[index] == letter):
		word[index] = ord(word[index])	# We do this to deal with special cases where the correct word has 2 of the same letter
		return True

def containsOrangeLetter(word, letter, index):
	if word[index] == letter:
			return False
	flag = False
	for charc in range(len(word)):
		if word[charc] == letter:
			# word[charc] = ord(word[charc])
			flag = True
	return flag

###### DRIVER #######

possibles = []
with open("wordles.txt", "r", encoding="utf-8") as guesses:
	for line in guesses:
		possibles.append([char for char in line][:-1])

# print(possibles[:10])
# possibles = list(filter(lambda word: containsOrangeLetter(word, 'e', 1), possibles))
# print("here")
# print(possibles)

option = input("Do you want to start a hint session for Wordle? [y/n]").strip().lower()

def prettyPrintGuesses():
	if(len(possibles)<10):
		for i in range(len(possibles)):
			for char in possibles[i]:
				if(type(char) == int):
					print(chr(char), end='')
				else:
					print(char, end='')
			print()
		return
	print("Here are my first 10 guesses:")
	randomten = random.sample(possibles, 10)

	for i in range(10):
		for char in randomten[i]:
			if(type(char) == int):
				print(chr(char), end='')
			else:
				print(char, end='')
		print()
		print("*****")
		print()

while(option != 'n'):
	print(f"There are {len(possibles)} words i'm considering in my database.")
	guess = input("Enter your guess: ").strip().lower() # If your guess was crane and it was black, black, orange, black, green
	guess = [char for char in guess]
	print("Now enter how correct that guess was in order (0 if black, 1 if orange, and 2 if green):") # You would enter 00102
	validity = input()
	validity = [int(char) for char in validity]
	counter = 0
	for letter, valid in zip(guess, validity):
		if(valid == 0):
			possibles = list(filter(lambda word: doesNotContainLetter(word, letter), possibles))
		elif(valid==1):
			possibles = list(filter(lambda word: containsOrangeLetter(word, letter, counter), possibles))
		elif(valid==2):
			possibles = list(filter(lambda word: correctGreenLetter(word, letter, counter), possibles))
		counter +=1
	prettyPrintGuesses()
	option = input("Would you like to continue? [y/n]").strip().lower()
