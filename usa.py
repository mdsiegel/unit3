#Matthew Siegel
#10/12/17
#usa.py - making a usa flag

from ggame import *

red  = Color(0xFF0000,1)
blue = Color(0x0000FF,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) #pixels,color


star = PolygonAsset([(60,0), (120,30), (100,60),(20,60),(0,30)], blackOutline, red)




Sprite(star)


App().run()



