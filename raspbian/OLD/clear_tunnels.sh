#!/bin/bash
ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'sudo kill -9 $(sudo lsof -t -i:10088)' || true
ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'sudo kill -9 $(sudo lsof -t -i:10022)' || true
ssh -i /home/pi/aws_micro_ubuntu.pem ubuntu@ec2-18-218-34-216.us-east-2.compute.amazonaws.com -t 'sudo systemctl restart ssh'

