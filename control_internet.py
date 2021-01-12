import RPi.GPIO as GPIO
import time
import subprocess

from spotify_controller.controller import *

spotify = None

while spotify is None:
	time.sleep(10)
	try:
		spotify = SpotifyController()
	except Error as e:
		print(e)


def loading_event(channel):
	time.sleep(2)

	if GPIO.input(channel):
		print("not loading")
		spotify.pause()
		subprocess.run(["ifconfig", "eth0", "down"])
	else:
		print("loading")
		subprocess.run(["ifconfig", "eth0", "up"])
		time.sleep(5)
		subprocess.run(["systemctl", "restart", "raspotify.service"])
		time.sleep(2)
		spotify.play()

spotify.play()

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(26, GPIO.BOTH, callback=loading_event)

while True:
	time.sleep(10)


