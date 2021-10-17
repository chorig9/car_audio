import time
import subprocess

from spotify_controller.controller import *

spotify = None

def restart():
	global spotify
	while True:
		time.sleep(10)
		try:
			subprocess.run(["systemctl", "restart", "raspotify.service"])
			time.sleep(2)
			spotify = SpotifyController()
			if spotify == None:
				continue
			spotify.play()
			return
		except Error as e:
			print(e)

restart()

while True:
	try:
		ret = spotify.cur_playing()
		if ret["is_playing"] == False:
			restart()
		time.sleep(10)
	except Exception as e:
		restart()
