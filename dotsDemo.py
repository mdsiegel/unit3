#Matthew Siegel
#10/5/17
#dotsDemo.py - Making some dots

from ggame import *

red  = Color(0xFF0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(12): #prints the row x times
    for i in range(20): #prints one row of dots
        Sprite(dot,(20+50*i,20+50*j))
App().run()