#Matthew Siegel
#9/28/17
#GuessingGame.py- Guessing the numbers

from random import randint

num = randint(1,100)
total = 0
while 1<2:
    total += 1
    guess = int(input('Guess a number between 1 and 100: '))
    if guess > num:
        print('Too high')
    elif guess < num:
        print('Too low')
    else:
        print("correct in",total,"guesses")
        break
    
