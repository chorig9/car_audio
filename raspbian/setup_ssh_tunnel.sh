ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -R 10022:localhost:22 -o ServerAliveInterval=60 -NT

