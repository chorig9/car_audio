ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -R 10088:localhost:6680 -o ServerAliveInterval=60 -o ExitOnForwardFailure=yes -NT

