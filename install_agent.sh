sudo echo "ubuntu:ubuntu" | chpasswd
sudo echo "root:root" | chpasswd
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install zabbix-agent
sudo apt-get -y install apache2


sudo sed -i "2s/.*/`ifconfig eth0 | grep "inet addr:"| cut -d: -f2 | awk "{ print $1 }"`/g" "/etc/hosts"
sudo sed -i "s/Bcast/`cat /etc/hostname`/g" "/etc/hosts"
sudo sed -i "3s/.*/192.168.11.217\	monitor/g" "/etc/hosts"
sudo /etc/init.d/networking restart
sudo echo "zabbix ALL=NOPASSWD: ALL" >> /etc/sudoers


sudo sed -i "s/# EnableRemoteCommands=0/EnableRemoteCommands=1/" "/etc/zabbix/zabbix_agentd.conf"
sudo sed -i "s/Server=127.0.0.1/Server=192.168.11.61/" "/etc/zabbix/zabbix_agentd.conf"
sudo sed -i "s/ServerActive=127.0.0.1/ServerActive=192.168.11.61:80/" "/etc/zabbix/zabbix_agentd.conf"
sudo sed -i "s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/" "/etc/zabbix/zabbix_agentd.conf"


sudo service apache2 restart
sudo service zabbix-agent restart
