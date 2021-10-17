import time
import subprocess

max_tries = 10

while True:
	try:
		ret = subprocess.call(["git", "pull",  "origin"])
		if ret == 0:
			break
	except Exception as e:
		print(e)

	max_tries = max_tries - 1
	if max_tries == 0:
		break


subprocess.call(["python3", "/home/pi/car_audio/run.py"])



