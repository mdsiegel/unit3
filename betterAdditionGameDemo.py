#Matthew Siegel
#10/4/17
#betterAdditiongameDemo.py - ask addition problems until user gets 5

from random import randint

numCorrect = 0
while numCorrect < 5:
    num1 = randint(-10,10)
    num2 = randint(-10,10)
    question = 'What is ' + str(num1) + ' + ' +  str(num2) + '?'
    answer = int(input(question))
    if answer == num1 + num2:
        print('correct!')
        numCorrect +=1
print('Congrats! You are smarter than Gary!')
