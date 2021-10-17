import time
import subprocess

from spotify_controller.controller import *

spotify = None

while spotify is None:
	time.sleep(10)
	try:
		spotify = SpotifyController()
		spotify.play()
	except Error as e:
		print(e)

while True:
	try:
		spotify.cur_playing()
	except Exception as e:
		subprocess.run(["systemctl", "restart", "raspotify.service"])
		time.sleep(2)
		spotify.play()
		time.sleep(2)
