#Matthew Siegel
#9/28/17
#gauss.py- gaus loop that adds up all numbers

sum = 0
for i in range(1,101):
    sum+=i
print(sum)

topNum = int(input('Enter a top range: '))
botNum = int(input('Enter a bottum range: '))
sum = 0
for i in range(botNum,topNum+1):
    sum+=i
print(sum)


Dif = int(input('Enter a difference: '))
sum = 0
for i in range(1,101,Dif):
    sum+=i
print(sum)
