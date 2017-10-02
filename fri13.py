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
while friday13<=10:
    if todayDay > 13:
        if runningMonth!=12:
            runningMonth+=1
            if weekday(13,runningMonth,runningYear) == 5:
                friday13+=1
                print(13,runningMonth,runningYear)
        else:
            runningMonth==1
            runningYear+=1
            if weekday(13,runningMonth,runningYear) == 5:
                friday13+=1
                print(13,runningMonth,runningYear)
    elif todayDay < 13:
        if weekday(13,runningMonth,runningYear) == 5:
                friday13+=1
                print(13,runningMonth,runningYear)
        else:
            print(
    else:
        if weekday(13,runningMonth,runningYear) == 5:
                friday13+=1
                print(13,runningMonth,runningYear)
        else:
            
            

                
        