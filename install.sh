#!/bin/bash

echo "======================================"
echo " iWebIT Network Monitoring Installer"
echo "======================================"

read -p "Enter IDSync: " IDSYNC

INSTALL_DIR="/opt/iWebIT_Network_Monitoring"

echo "Creating directory..."
sudo mkdir -p $INSTALL_DIR

echo "Copying files..."
sudo cp -r * $INSTALL_DIR

cd $INSTALL_DIR

echo "Updating config.json..."
sudo sed -i 's/"IDSync": ""/"IDSync": "'$IDSYNC'"/' config.json

echo "Installing Python dependencies..."
sudo apt update
sudo apt install -y python3 python3-pip
pip3 install psutil requests

echo "Creating logs folder..."
sudo mkdir -p $INSTALL_DIR/logs
sudo touch $INSTALL_DIR/logs/agent.log

echo "Installing systemd service..."
sudo cp iwebit_network_monitoring.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable iwebit_network_monitoring
sudo systemctl start iwebit_network_monitoring

echo "======================================"
echo " Installation completed"
echo " Service started"
echo "======================================"

echo "Check service status with:"
echo "systemctl status iwebit_network_monitoring"
