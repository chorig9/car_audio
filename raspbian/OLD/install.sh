cp 70-usb-modeswitch.rules /etc/udev/rules.d/

cp last.target /etc/systemd/system/last.target
mkdir /etc/systemd/system/last.target.wants

cp client_init.service /etc/systemd/system/
cp ssh_tunnel.service /etc/systemd/system/
cp http_tunnel.service /etc/systemd/system/

ln -s /etc/systemd/system/ssh_runnel.service /etc/systemd/system/last.target.wants/ssh_tunnel.service
ln -s /etc/systemd/system/http_runnel.service /etc/systemd/system/last.target.wants/http_tunnel.service

systemctl daemon-reload

systemctl set-default last.target
systemctl isolate last.target

systemctl enable client_init.service
systemctl enable ssh_tunnel.service
systemctl enable http_tunnel.service

