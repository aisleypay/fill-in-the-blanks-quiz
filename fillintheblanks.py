# IPND Stage 2 Final Project

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!


#Passages and Answers

# Level 1
quizes = {'Easy': '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value 
to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be 
more complicated such as objects and lambda functions.''',

#Level 2 Grammar Check
		   'Medium': """Once upon a time there ___1___ (live) a man called Damocles.\n A friend of his eventually ___2___ (become) the ruler of a small city.\n Damocles thought, 'How lucky my friend ___3___ (be). He ___3___ (be) now a ruler.\n He must ___4___ (have) a great time. \
He ___5___ have fine clothes, lots of money and a number of servants.\n I wish I ___6___ (have) his luck.'
He ___7___ (decide) to visit his friend to enjoy his hospitality. When he ___8___ (reach) the palace, the king 
himself ___9___ (receive) him with respect and affection. Damocles then ___10___ (tell) the king that 
he ___11___ (be) indeed a lucky man.\nThe king ___12___ (smile). He ___13___ (invite) his friend to have dinner with him.""",

#Level 3 Marvel Quotes
			'Hard': '''You know, the last time I was in Germany and saw a man ___1___ everybody else, we ended up disagreeing. -- Captain America
You people are so petty... and ___2___. -- Thor
Well, if I put an arrow through ___3___, I'd sleep better, I suppose. -- Hawkeye
Regimes fall every day. I tend not to weep over that, I'm ___4___... or was. -- Black Widow
Dost Mother know you wear-eth her ___5___? -- Tony Stark
That's my secret, Cap: I'm ___6___. -- Bruce Banner
I sort of met you, I mean, I watched you while you were ___7___. -- Phil Coulson'''}

answers = {'Easy':[["function"],["parameters"],["errors"], ["lists"]],
		   'Medium':[["lived"], ["became"], ["is"], ["be having"], ["must have"], ["had"], ["decided"], ["reached"], ["received"], 
					 ["told"], ["was"], ["smiled"], ["invited"]],
		   'Hard':[["standing"], ["tiny"], ["Loki's"], ["Russian"], ["drapes"], ["always angry"], ["sleeping"]]}


#User Difficulty - user will first choose difficulty level of game

print "Welcome to GUESS THAT WORD! A game of knowledge and wit, let's see what you got!"
def user_level():
	global player_level
	player_level = raw_input("Choose your difficulty level: Easy, Medium, or Hard: ")
	dif_level = ["Easy", "Medium", "Hard"]
	while player_level not in dif_level:
		player_level = raw_input("Please choose Easy, Medium, or Hard. Don't forget your CAPITALIZATIONS! ")
	print "You have chosen level "+player_level+"." + "\n"
	if player_level == dif_level[0]:
		print "Nice and easy.."
		print quizes['Easy']
		return game_play()
	elif player_level == dif_level[1]:
		print "This is a grammar challenge. Enter the correct form of the words in parentheses." + "\n"
		print quizes['Medium']
		return game_play()
	elif player_level == dif_level[2]:
		print "Let's test you Avengers knowledge" + "\n"
		print quizes['Hard']
		return game_play()

quiz = 1 #number of questions to be answered/the question currently being answered
p1 = 0 #passage

#main game

def game_play():
	global quiz
	quizloop = len(answers[player_level]) + 1
	while quiz < quizloop:    #loop to stop game when all blanks have been correctly filled per the game level
		questions()
		quiz += 1

#user provides answers to the blanks in passage
def questions():
	blankans = quiz - 1                 #this is the index. this directly refers to the list placement of the specified questions
	print "Question %s" % quiz          #%s is useful for string substitution
	print "What is ___%s___?" % quiz
	trueans = answers[player_level][blankans]   #index of actual answer to questions
	userans = raw_input("Your answer: ")
	while userans not in trueans:
		print "That is not right! Try again :("
		userans = raw_input("New answer: ")
	if userans in trueans:
		print "Correct!"

#fill in the blanks of the original passage and print the newly filled in passage

	global p1, filledin
	if p1 == 0:   						#this is for the first time the game is run, when the filling in process is dragging in the passages locally to this function for the first time
		p1 = quizes[player_level]
		p1 = p1.replace('___%s___' % str(quiz), userans)
		filledin = p1	
	else:
		filledin = filledin.replace('___%s___' % str(quiz), userans)   #post 1 blank being filled correctly
	print filledin


user_level()

print "Thanks for playing! See you next time!"
