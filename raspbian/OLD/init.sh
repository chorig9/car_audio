#!/bin/sh

# Assumes this repo is cloned to /home/pi/car_audio
cd /home/pi/car_audio
git pull origin

cd raspbian
./startup.sh
