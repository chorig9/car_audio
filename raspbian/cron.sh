@reboot sleep 10 && /home/pi/create_tunnel.sh > /home/pi/cron_status.txt 2>&1
* * * * * /home/pi/create_tunnel.sh > /home/pi/every_minute_cron.txt 2>&1
