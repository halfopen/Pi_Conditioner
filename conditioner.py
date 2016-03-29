#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO
import time

# 定义单个数码管各段led对应的GPIO口
LED_A = 26
LED_B = 19
LED_C = 13
LED_D = 6
LED_E = 5
LED_F = 11
LED_G = 9
LED_DP = 10

# 定义1到4号数码管阳极对应的GPIO口
DIGIT1 = 12
DIGIT2 = 16
DIGIT3 = 20
DIGIT4 = 21

# 定义按钮输入的GPIO口
btn1 = 17
btn2 = 14
btn1_flag=False
btn2_flag=False

temprature = 27.45

RPi.GPIO.setmode(RPi.GPIO.BCM)

RPi.GPIO.setup(LED_A, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_B, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_C, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_D, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_E, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_F, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_G, RPi.GPIO.OUT)
RPi.GPIO.setup(LED_DP, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT1, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT2, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT3, RPi.GPIO.OUT)
RPi.GPIO.setup(DIGIT4, RPi.GPIO.OUT)

RPi.GPIO.output(DIGIT1, True)
RPi.GPIO.output(DIGIT2, True)
RPi.GPIO.output(DIGIT3, True)
RPi.GPIO.output(DIGIT4, True)

RPi.GPIO.setup(btn1, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)
RPi.GPIO.setup(btn2, RPi.GPIO.IN, pull_up_down=RPi.GPIO.PUD_UP)


def get_temperature():
	tfile = open("/sys/bus/w1/devices/28-0216002036ff/w1_slave")
	text = tfile.read()
	tfile.close()

	secondline=text.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:]) /1000
	print temperature," C"
	return temperature



# 指定no(1-4)号数码管显示数字num(0-9)，第三个参数是显示不显示小数点（true/false）
def showDigit(no, num, showDotPoint):
    # 先将正极拉低，关掉显示
	RPi.GPIO.output(DIGIT1, False)
	RPi.GPIO.output(DIGIT2, False)
	RPi.GPIO.output(DIGIT3, False)
	RPi.GPIO.output(DIGIT4, False)
	
	if (num == 0) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, False)
		RPi.GPIO.output(LED_F, False)
		RPi.GPIO.output(LED_G, True)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 1) :
		RPi.GPIO.output(LED_A, True)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, True)
		RPi.GPIO.output(LED_E, True)
		RPi.GPIO.output(LED_F, True)
		RPi.GPIO.output(LED_G, True)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 2) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, True)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, False)
		RPi.GPIO.output(LED_F, True)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 3) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, True)
		RPi.GPIO.output(LED_F, True)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 4) :
		RPi.GPIO.output(LED_A, True)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, True)
		RPi.GPIO.output(LED_E, True)
		RPi.GPIO.output(LED_F, False)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 5) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, True)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, True)
		RPi.GPIO.output(LED_F, False)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 6) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, True)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, False)
		RPi.GPIO.output(LED_F, False)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 7) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, True)
		RPi.GPIO.output(LED_E, True)
		RPi.GPIO.output(LED_F, True)
		RPi.GPIO.output(LED_G, True)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 8) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, False)
		RPi.GPIO.output(LED_F, False)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	elif (num == 9) :
		RPi.GPIO.output(LED_A, False)
		RPi.GPIO.output(LED_B, False)
		RPi.GPIO.output(LED_C, False)
		RPi.GPIO.output(LED_D, False)
		RPi.GPIO.output(LED_E, True)
		RPi.GPIO.output(LED_F, False)
		RPi.GPIO.output(LED_G, False)
		RPi.GPIO.output(LED_DP, not showDotPoint)
	
	if (no == 1) :
		RPi.GPIO.output(DIGIT1, True)
	elif (no == 2) :
		RPi.GPIO.output(DIGIT2, True)
	elif (no == 3) :
		RPi.GPIO.output(DIGIT3, True)
	elif (no == 4) :
		RPi.GPIO.output(DIGIT4, True)

def showTemprature(temprature):
	t=0.005
	time.sleep(t);
	showDigit(1,(int)(temprature/10),False);
	time.sleep(t);
	showDigit(2,(int)(temprature%10),True);
	time.sleep(t);
	showDigit(3,(int)(temprature*10%10),False);
	time.sleep(t);
	showDigit(4,(int)(temprature*100%10),False);

try:

	while True:
		if RPi.GPIO.input(btn1)==0 :
			if btn1_flag==False:
				temprature = temprature+0.5
				btn1_flag=True
				print temprature
		else:
			if btn1_flag==True:
				btn1_flag = False
		
		if RPi.GPIO.input(btn2)==0 :
			if btn2_flag==False:
				temprature = temprature-0.5
				btn2_flag=True
				print temprature
		else:
			if btn2_flag==True:
				btn2_flag = False

		showTemprature(temprature)
		
		
			
except KeyboardInterrupt:
	pass

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）
RPi.GPIO.cleanup()
