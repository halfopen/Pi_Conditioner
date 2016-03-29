from rpimenu.Adafruit_CharLCD import *
from conditioner import *


lcd = Adafruit_CharLCD()

while(True):
	t = get_temperature()
	sleep(0.5)
	lcd.clear()
	lcd.message(str(t))


