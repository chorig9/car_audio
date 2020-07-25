#!/bin/bash

if ! ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'timeout 5 ssh -p 10022 pi@localhost exit'; then
	ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'sudo kill -9 $(sudo lsof -t -i:10088)' || true
	ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'sudo kill -9 $(sudo lsof -t -i:10022)' || true
	ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'sudo systemctl restart ssh'

	# Wait for ssh server to restart
	sleep 5

	ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -R 10022:localhost:22 -o ServerAliveInterval=60 -f -N
        ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -R 10088:localhost:6680 -o ServerAliveInterval=60 -f -N
fi

