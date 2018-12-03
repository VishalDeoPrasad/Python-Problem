import random
print "Welcome to Hangman Game :"

words=("apple","ball","cat","dog","elephant","fish","girl","hen","ice-cream","jun","kite","lion","mango","night","orange")
comp_gues=random.choice(words)

len=str(len(comp_gues))
print "Your have only 5 chance:"
user_gues = raw_input("Guess a %s latter word: " %len)

atmpt=0
while atmpt<=5:
	if comp_gues==user_gues:
		print "good job! your are Amazon."
		break
	else:
		user_gues = raw_input ("Try Again!: ")

	atmpt+=1

else:
	print "Game Over!"