cp 70-usb-modeswitch.rules /etc/udev/rules.d/

cp network-wait-online.service /lib/systemd/system/
cp tunnel.service /etc/systemd/system/

systemctl daemon-reload
systemctl enable network-wait-online.service
systemctl enable tunnel.service
