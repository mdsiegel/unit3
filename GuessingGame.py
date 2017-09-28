#Matthew Siegel
#9/28/17
#GuessingGame.py- Guessing the numbers

from random import randint

num = randint(1,100)
correct = False

while correct == False:
    guess = int(input('Guess a number between 1 and 100: '))
    
    
