#Matthew Siegel
#9/29/17
#changeComputerloop.py - finding amount of change

cents = int(input('Enter an amount of cents: '))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while cents > 0:
    if cents - 25 >= 0 :
        quarters +=1
        cents -=25
    elif cents-10 >= 0:
        dimes += 1
        cents -=10
    elif cents-5 >=0:
        nickels += 1
        cents -=5
    elif cents -1 >=0:
        pennies += 1
        cents -=1
        
        
print('There are',quarters,'quarters',dimes,'dimes',nickels,'nickles', pennies,'pennies')