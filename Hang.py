from random import randint
Word = ''
ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
tr = 5
Ran = 0
blank = ''
Choice = ''
guess = []
PreChoice = []
X = ''
def Random():
	global Word,ABC,Ran
	for x in range(randint(3,12)):
		Ran = ABC[(randint(0,25))]
		Word += Ran	
	print (Word)
	Blank()

def Blank():
	global Word,blank
	
	for x in Word:
		blank +='_ '
		
	print(blank)
	PlayerChoices()

def PlayerChoices():
	global Word,blank,tr,Choice
	if tr>0:
		tr=str(tr)
		Choice=input('can you guess the word? have '+ tr  + 'trys left')
		tr=int(tr)
		Check2()

def Check():
	global Word,Choice,guess,PreChoice

	for x in Word:
		if x==Choice or x==PreChoice:
			guess.append(Choice)
		else: 
			guess.append('_ ')
	print(guess)
	guess=[]
	PlayerChoices()

def Check2():
	global Word,Choice,guess,PreChoice
	for x in Word:
		if Choice  in x:
			guess.append(Choice)
			PreChoice.append(Choice)
		else:
			XX=x
			for y in PreChoice:
				if XX in y:
					guess.append(XX)
					
			
		
		else:
			guess.append('_ ')
	PlayerChoice()	


Random
			




Random()
