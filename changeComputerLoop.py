#Matthew Siegel
#9/29/17
#changeComputerloop.py - finding amount of change

cents = int(input('Enter an amount of cents: '))
quarters = 0


while cents > 0:
    if cents // 25 > 1 :
        quarters +=1
        cents -=25
    if cents //10 > 1:
        