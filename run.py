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

spotify.play()

