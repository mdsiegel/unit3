#Matthew Siegel
#9/29/17
#fri13 - finding the friday the 13ths

from calendar import weekday
from datetime import date
todayDay = date.today().day
todayMonth = date.today().month
todayYear = date.today().year

print(date.today().month,date.today().day, date.today().year)
print(weekday(date.today().year,date.today().month,date.today().day))

friday13 = 0


runningMonth = todayMonth
runningYear = todayYear
if todayDay > 13:
    if runningMonth!=12:
        runingMonth +=1
    else:
        runningMonth == 1
        runningYear+=1

print('final month is',runningMonth)
while friday13<=10:
    if weekday(runningYear,runningMonth,13) == 5:
        print(13,'/',runningMonth,'/',runningYear)
        friday13+=1
    if runningMonth == 12:
        runningMonth = 1
        runningYear+=1
    else:
        runningMonth+=1
    
    
     
        