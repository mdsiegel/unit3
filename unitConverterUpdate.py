#Matthew Siegel
#9/28/17
#unitConverterUpdate.py- Update to the program

quit = False
while quit==False:
    numChose = int(input('1 for Km to miles, 2 for Kg to pounds, 3 for liters to gallons, 4 for celsius to fahrenheit, 5 for quit'))
    
    if numChose/1 ==1:
        Km = float(input('Enter a distance in Km: '))
        print('You have',Km*0.621371, 'miles')
    elif numChose/2 ==1:
        Kg = float(input('Enter Kg: '))
        print('You have',Kg*2.20462, 'pounds')
    elif numChose/3 ==1:
        liters = float(input('Enter lites: '))
        print('You have',liters*0.219969, 'gallons')
    elif numChose/4 ==1:
        celsius = float(input('Enter a temp in celsius: '))
        print('You have',celsius*1.8+32, 'fahrenheit')
    elif numChose/5 == 1:
        break
    else:
        break
