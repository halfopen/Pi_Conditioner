#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO
from rpimenu.Adafruit_CharLCD import *


btn_l,btn_r = 20,21


# 从传感器中获取温度
def get_temperature():
	tfile = open("/sys/bus/w1/devices/28-0216002036ff/w1_slave")
	text = tfile.read()
	tfile.close()

	secondline=text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:]) /1000
	print temperature," C"
	return temperature

# 打印开始信息
def print_info():
	print "空调模拟程序--武汉大学计科三班2013301500100秦贤康"

def setup():
	RPi.GPIO.setmode(RPi.GPIO.BCM)
	RPi.GPIO.setup(btn_l, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
	RPi.GPIO.setup(btn_r, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
	
# 主函数
if __name__ == '__main__':
	print_info()
	lcd = Adafruit_CharLCD()
	setup()
	set_temperature = get_temperature()
	w = 'N'
	# 
	try:
		while(True):
			if(RPi.GPIO.input(btn_l) == 0):
				print "左键按下"
				set_temperature = set_temperature+0.5
			if(RPi.GPIO.input(btn_r) == 0):
				print "右键按下"
				set_temperature = set_temperature-0.5
			print "获取温度"
			t = get_temperature()
			if t-set_temperature>1:
				w = 'L'
			elif t-set_temperature<-1:
				w = 'H'
			else:
				w = 'N'
			#sleep(0.8)
			lcd.clear()
			lcd.message("S:"+str(set_temperature)+"    W:"+w+"\nC:"+str(t))
	except KeyboardInterrupt:
		print "程序终止"

	RPi.GPIO.clearnup()
