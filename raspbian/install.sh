cp 70-usb-modeswitch.rules /etc/udev/rules.d/

cp network-wait-online.service /lib/systemd/system/
cp client_init.service /etc/systemd/system/
cp ssh_tunnel.service /etc/systemd/system/
cp http_tunnel.service /etc/systemd/system/

systemctl daemon-reload
systemctl enable network-wait-online.service
systemctl enable client_init.service
systemctl enable ssh_tunnel.service
systemctl enable http_tunnel.service

