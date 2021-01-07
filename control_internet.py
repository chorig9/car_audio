import RPi.GPIO as GPIO
import time
import subprocess

def loading_event(channel):
	if GPIO.input(channel):
		print("not loading")
		subprocess.run(["ifconfig", "eth1", "down"])
	else:
		print("loading")
		subprocess.run(["ifconfig", "eth1", "up"])

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.BOTH, callback=loading_event, bouncetime=200)

while True:
	time.sleep(10)


