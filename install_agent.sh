#!/usr/bin/env bash

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install zabbix-agent
sudo apt-get -y install apache2


sudo sed -i "2s/.*/`ifconfig [eno1, eno2] | grep "inet addr:"| cut -d: -f2 | awk "{ print $1 }"`/g" "/opt/stack/Inspection-System/testhosts"
sudo sed -i "s/Bcast/`cat /etc/hostname`/g" "/opt/stack/Inspection-System/testhosts"
sudo sed -i "3s/.*/[x.x.x.x, y.y.y.y]\	monitor/g" "/opt/stack/Inspection-System/testhosts"
sudo /etc/init.d/networking restart
sudo echo "zabbix ALL=NOPASSWD: ALL" >> /etc/sudoers


sudo sed -i "s/# EnableRemoteCommands=0/EnableRemoteCommands=1/" "/etc/zabbix/zabbix_agentd.conf"
sudo sed -i "s/Server=127.0.0.1/Server=192.168.11.121/" "/etc/zabbix/zabbix_agentd.conf"
sudo sed -i "s/ServerActive=127.0.0.1/ServerActive=192.168.11.121:22/" "/etc/zabbix/zabbix_agentd.conf"
sudo sed -i "s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/" "/etc/zabbix/zabbix_agentd.conf"


sudo service apache2 restart
sudo service zabbix-agent restart
sudo echo "ubuntu:ubuntu" | chpasswd
sudo echo "root:root" | chpasswd



## Testing Component Packages install
sudo apt-get install -y git
git clone https://github.com/KyleOh/HoonMinJeongUm-TestingPluginScript.git

cd HoonMinJeongUm-TestingPluginScript
sudo ./nodejs_install.sh
sudo ./plugin_artillery_install.sh
sudo ./plugin_locustio_install.sh
sudo ./plugin_stressng_install.sh