#Matthew Siegel
#9/28/17
#GuessingGame.py- Guessing the numbers

from random import randint

num = randint(1,100)

while 1<2:
    guess = int(input('Guess a number between 1 and 100: '))
    if guess > num:
        print('Too high')
    elif guess < num:
        print('Too low')
    else:
        print("correct")
        break
    
