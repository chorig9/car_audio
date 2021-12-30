import time
import subprocess

from spotify_controller.controller import *

spotify = None
progress = None

def initialize():
	global spotify
	global progress
	while True:
		try:
			subprocess.run(["ifconfig", "eth0", "up"])
			time.sleep(2)
			subprocess.run(["systemctl", "restart", "raspotify.service"])
			time.sleep(2)
			spotify = SpotifyController()
			if spotify == None:
				continue
			progress = spotify.get_progress_ms()
			spotify.play()
			spotify.seek_track(progress)
			return
		except Exception as e:
			print(e)
		time.sleep(5)

def restart():
	global spotify
	numFailed = 0
	while True:
		try:
			if numFailed > 7:
				initialize()
			spotify.play()
			spotify.seek_track(progress)
			return
		except Exception as e:
			numFailed = numFailed + 1
			print(e)
		time.sleep(5)
		
print("start")
initialize()

while True:
	try:
		ret = spotify.cur_playing()
		if ret["is_playing"] == False:
			restart()
		progress = spotify.get_progress_ms()
		time.sleep(10)
	except Exception as e:
		restart()
