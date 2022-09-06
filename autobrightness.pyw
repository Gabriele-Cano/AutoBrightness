from monitorcontrol import *
import darkdetect
import serial
import pystray
from PIL import Image
import time
import sys

COM_PORT = "COM5"

def getSign(number):
	if number >= 0:
		return 1
	else:
		return -1

def command(icon, item):
	name = str(item)
	if name == "Exit":
		icon.stop()
		sys.exit()

def mainLoop(icon):
	icon.visible = True
	serialPort = serial.Serial(port = COM_PORT, baudrate=2000000)

	while True:
		time.sleep(0.05)
		if serialPort.in_waiting > 0:
			luminance = int(serialPort.readline().decode())
			print(luminance)
			for monitor in get_monitors():
				with monitor:
					prevLuminance = monitor.get_luminance()
					deltaL = luminance - prevLuminance
					for i in range(abs(deltaL)):
						monitor.set_luminance(prevLuminance + getSign(deltaL))
						prevLuminance = monitor.get_luminance()

if __name__ == "__main__":
	if darkdetect.isDark():
		image = Image.open("icon_dark.png")
	else:
		image = Image.open("icon.png")
	
	icon = pystray.Icon("AutoBrightness", image, menu=pystray.Menu(
		pystray.MenuItem("Exit", command)
	))

	icon.run(mainLoop)
