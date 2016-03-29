tfile = open("/sys/bus/w1/devices/28-0216002036ff/w1_slave")
text = tfile.read()
tfile.close()

secondline=text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:]) /1000
print temperature," C"
