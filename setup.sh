#!/bin/bash
# Setup Script for IKEA SYMFONISK (KDE)

echo ' IKEA SYMFONISK Configurator  '
echo '           .........          '
echo '       ..........:::^::.      '
echo '    .......:::......:^^^^:.   '
echo '   .......:...:.......^^^^~:  '
echo '  .........:::.........^^^^~: '
echo ' ......................:^^^~~ '
echo ' .......................^^^^!:'
echo ' .......................^^^^!:'
echo ' .......................^^^~! '
echo '  .....................^^^~!: '
echo '   ...................^^^~~:  '
echo '     ...............:^^^^^.   '
echo '       ...........::^::..     '
echo '             .......          '

# Remove already existed config
sudo rm config.json

# Install python dependency
pip install paho-mqtt

echo "Broker address (example - 192.168.0.1)"
read broker
echo "Port (example - 1883)"
read port
echo "MQTT topic (example - zigbee2mqtt/symfonisk)"
read topic
echo "Broker username (example - homeassistant)"
read username
echo "Broker password"
read password

# Export data to .json file
echo '{
    "broker":"'$broker'",
    "port":"'$port'",
    "topic":"'$topic'",
    "username":"'$username'",
    "password":"'$password'"
}' >> config.json

# Export service files
sudo mkdir /lib/volumeKnobController
sudo cp volumeControl.py /lib/volumeKnobController
sudo cp config.json /lib/volumeKnobController
sudo cp volumeKnobController.service /etc/systemd/user

# Run service
systemctl --user daemon-reload
systemctl --user start volumeKnobController.service
systemctl --user enable volumeKnobController.service

echo Checking service status

systemctl --user status volumeKnobController.service | awk 'NR==3'
