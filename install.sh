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

echo "Installing Python and venv..."
sudo apt update
sudo apt install -y python3 python3-venv

echo "Creating virtual environment..."
python3 -m venv venv
source venv/bin/activate

echo "Installing Python modules..."
pip install psutil requests

echo "Creating logs folder..."
mkdir -p logs
touch logs/agent.log

echo "Installing systemd service..."
sudo cp iwebit_network_monitoring.service /etc/systemd/system/

sudo systemctl daemon-reload
sudo systemctl enable iwebit_network_monitoring
sudo systemctl restart iwebit_network_monitoring

echo "======================================"
echo " Installation completed"
echo "======================================"
