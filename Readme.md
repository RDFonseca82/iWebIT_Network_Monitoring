----------------------------------------------------------------------------

🚀 Passo a passo de instalação


git clone https://github.com/RDFonseca82/iWebIT_Network_Monitoring.git

cd iWebIT_Network_Monitoring

chmod +x install.sh

sudo ./install.sh

sudo systemctl status iwebit_network_monitoring


Durante a instalação será solicitado o IdSync (identificador da empresa ou cliente).


-------------------------------------------------------------------------------------

🚀 Desisntalar iWebItAgent


sudo systemctl stop iwebit_network_monitoring.service 2>/dev/null

sudo systemctl disable iwebit_network_monitoring.service 2>/dev/null

sudo rm -f /etc/systemd/system/iwebit_network_monitoring.service

sudo systemctl daemon-reload

sudo rm -rf /opt/iwebit_network_monitoring

sudo rm -rf /var/log/iwebit_network_monitoring


----------------------------------------------------------------------------------------

#Verificar o status do serviço

sudo systemctl status iwebit_network_monitoring
