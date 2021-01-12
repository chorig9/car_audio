import RPi.GPIO as GPIO
import time
import subprocess

def loading_event(channel):
	time.sleep(2)

	if GPIO.input(channel):
		print("not loading")
		subprocess.run(["ifconfig", "eth0", "down"])
	else:
		print("loading")
		subprocess.run(["ifconfig", "eth0", "up"])
		time.sleep(5)
		subprocess.run(["systemctl", "restart", "raspotify.service"])

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.BOTH, callback=loading_event)

while True:
	time.sleep(10)


