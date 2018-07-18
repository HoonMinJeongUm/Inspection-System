
import subprocess


install_agent = "/opt/stack/Inspection-System/install_agent"
path = "/opt/stack/Inspection-System"

open("%s/install_agent" %path,'w').close()


subprocess.call("echo 'sudo apt-get -y update' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo apt-get -y upgrade' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo apt-get -y install zabbix-agent' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo apt-get -y install apache2' >> '%s'" %install_agent, shell=True)


subprocess.call("echo 'sudo sed -i \"2s/.*/`ifconfig [Interface name in VNF] | grep \"\"\\\"inet addr:\\\"\"\"| cut -d: -f2 | awk \"\"\\\"{ print $1 }\\\"\"\"`/g\" \"/etc/hosts\"' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/etc/hosts\"' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo sed -i \"3s/.*/[Zabbix Host IP Address]\tmonitor/g\" \"/etc/hosts\"' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo echo 'zabbix ALL=NOPASSWD: ALL' >> /etc/sudoers' >> '%s'" %install_agent, shell=True)


subprocess.call("echo 'sudo sed -i \"s/# EnableRemoteCommands=0/EnableRemoteCommands=1/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %install_agent, shell=True)
sub#process.call("echo 'sudo sed -i \"s/Server=127.0.0.1/Server=[Zabbix server's IP Address]/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %install_agent, shell=True)
sub#process.call("echo 'sudo sed -i \"s/ServerActive=127.0.0.1/ServerActive=[Zabbix server's IP Address:Port]/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo sed -i \"s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %install_agent, shell=True)

subprocess.call("echo 'sudo service apache2 restart' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo service zabbix-agent restart' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo echo 'ubuntu:ubuntu' | chpasswd' >> '%s'" %install_agent, shell=True)
subprocess.call("echo 'sudo echo 'root:root' | chpasswd' >> '%s'" %install_agent, shell=True)


#os.chmod("%s/install_agent" %path,0777)     #make <install_agent> shell script execute

