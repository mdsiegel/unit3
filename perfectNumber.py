#Matthew Siegel
#9/29/17
#perfectNumber.py - weird number game

num = int(input('Enter a perfect number: '))
total = 0
i = 1
while i<num:
    if num%i == 0:
        total +=i
        print(i)
    i+=1

print(total)
if total == num:
    print('Perfect Number!')
else:
    print('Not perfect')
