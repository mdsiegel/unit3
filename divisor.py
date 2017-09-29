#Matthew Siegel
#9/29/17
#divisor.py - finding all the divisors

num = int(input('Enter a number: '))
stop = False
i = 1
while stop == False:
    i+=1
    if num%i == 0:
        print(num/i)
    
    if i==num:
        break
    
    

