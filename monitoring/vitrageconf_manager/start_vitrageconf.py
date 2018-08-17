
import subprocess
from ssh_manager import listener
import os
import time


class VitrageconfManager(object):

    def __init__(self, request):
        self.monitoring_tool = None
        self.server_ip = None
        self.server_port = None
        self.server_pass = None
        self.server_user = None
        self.host_name = None
        self.host_type = None
        self.vm_ip =  None
        self.vm_id = None
        self.vm_interface= None
	

        self.script = "/opt/stack/Inspection-System/install_agent.sh"                 # use for appending texts to script (real path in which script is locate )
        self.path_script = "/opt/stack/Inspection-System"                            # path of script
        self.data = None

        self.path_vitrage = "/etc/vitrage"                           # replace here with /etc/vitrage
        self.vitrage_conf = "/etc/vitrage/vitrage.conf"  # replace here with /etc/vitrage/vitrage.conf
        self.zabbix_conf = "/etc/vitrage/zabbix_conf.yaml"      # replace here with

        self.request = request


    def decode(self):
        self.data = self.request['vitrage_conf_policy']
        self.monitoring_tool = self.data['monitoring_tool']
        self.server_ip = self.data['server_ip']
        self.server_port = self.data['server_port']
        self.server_pass = self.data['server_pass']
        self.server_user = self.data['server_user']
        self.host_name = self.data['host_name']
        self.host_type = self.data['host_type']
        self.vm_ip = self.data['vm_ip']
        self.vm_id = self.data['vm_id']
        self.vm_interface = self.data['vm_interface']

    def make_script(self):

        open("%s/install_agent.sh" % self.path_script, 'w').close()  # make <install_agent> script

        subprocess.call("echo 'sudo echo \"ubuntu:ubuntu\" | chpasswd' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo echo \"root:root\" | chpasswd' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y update' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y upgrade' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y install zabbix-agent' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y install apache2' >> '%s'" % self.script, shell=True)
        subprocess.call("echo '\n' >> '%s'" % self.script, shell=True)

        subprocess.call("echo 'sudo sed -i \"2s/.*/`ifconfig '%s' | grep \"inet addr:\"| cut -d: -f2 | awk \"{ print $1 }\"`/g\" \"/etc/hosts\"' >> '%s'" % (self.vm_interface, self.script), shell=True)           #replace testhosts to /etc/hosts
        subprocess.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/etc/hosts\"' >> '%s'" % self.script, shell=True)                                 #replace testhosts to /etc/hosts
        subprocess.call("echo 'sudo sed -i \"3s/.*/'%s'\\\tmonitor/g\" \"/etc/hosts\"' >> '%s'" % (self.vm_ip, self.script), shell=True)                        #replace testhosts to /etc/hosts
        subprocess.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo echo \"zabbix ALL=NOPASSWD: ALL\" >> /etc/sudoers' >> '%s'" % self.script, shell=True)
        subprocess.call("echo '\n' >> '%s'" % self.script, shell=True)

        subprocess.call("echo 'sudo sed -i \"s/# EnableRemoteCommands=0/EnableRemoteCommands=1/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Server=127.0.0.1/Server='%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.script), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/ServerActive=127.0.0.1/ServerActive='%s':'%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.server_port, self.script), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % self.script, shell=True)
        subprocess.call("echo '\n' >> '%s'" % self.script, shell=True)

        subprocess.call("echo 'sudo service apache2 restart' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo service zabbix-agent restart' >> '%s'" % self.script, shell=True)

        # os.chmod("%s/install_agent" %path,0777)     #make <install_agent> shell script execute
        #ssh_manager.listener.start_script(self.vm_ip,self. )  # hosts,auth,file_name,local_path,remote_path

    def start_config(self):
        # add zabbix to list of datasources in /etc/vitrage/vitrage.conf
        #subprocess.call(['sed', "-i", "20s/nova.host/zabbix,nova.host/g", self.vitrage_conf])
	subprocess.call(['sed', "-i", "20s/types = nova.host/types = zabbix,nova.host/g", self.vitrage_conf])
        

	# add texts to vitrage_conf file
        #subprocess.call("echo '[zabbix]' >> '%s'" % self.vitrage_conf, shell=True)
        #subprocess.call("echo 'url = http://'%s'/zabbix' >> '%s'" % (self.server_ip, self.vitrage_conf), shell=True)
        #subprocess.call("echo 'password = '%s'' >> '%s'" % (self.server_pass, self.vitrage_conf), shell=True)
        #subprocess.call("echo 'user = '%s'' >> '%s'" % (self.server_user, self.vitrage_conf), shell=True)
        #subprocess.call("echo 'config_file = /etc/vitrage/zabbix_conf.yaml' >> '%s'" % self.vitrage_conf, shell=True)
	subprocess.call(['sed', "-i", "35s/.*/[zabbix]/g", self.vitrage_conf])
	subprocess.call(['sed', "-i", "36s/.*/url = http:\/\/%s\/zabbix/g" %self.server_ip, self.vitrage_conf])
	subprocess.call(['sed', "-i", "37s/.*/password = %s/g" % self.server_pass, self.vitrage_conf])
	subprocess.call(['sed', "-i", "38s/.*/user = %s/g" % self.server_user, self.vitrage_conf])
	subprocess.call(['sed', "-i", "39s/.*/config_file = \/etc\/vitrage\/zabbix_conf.yaml/g" , self.vitrage_conf])
        # make zabbix_conf.yaml file and add texts

        if os.path.exists("%s" % self.zabbix_conf):
            pass
        else:
            open("%s/zabbix_conf.yaml" % self.path_vitrage, 'w').close()
            subprocess.call("echo 'zabbix:' >> '%s'" % self.zabbix_conf, shell=True)

        subprocess.call("echo '- zabbix_host: '%s'' >> '%s'" % (self.host_name, self.zabbix_conf), shell=True)
        subprocess.call("echo '  type: '%s'' >> '%s'" % (self.host_type, self.zabbix_conf), shell=True)
        subprocess.call("echo '  name: '%s'' >> '%s'" % (self.vm_id, self.zabbix_conf), shell=True)

	print("=================================================================")
	print("            Waiting For Restart Vitrage-Service                  ")
	print("=================================================================")
	time.sleep(60)	
        subprocess.call('sudo systemctl restart devstack@vitrage-*', shell=True)

    def start_script(self):
        self.decode()
        if self.monitoring_tool == "Zabbix":
            self.make_script()
            listener.start_script([self.vm_ip], ['ubuntu','ubuntu'], "install_agent.sh", self.path_script, "/home/ubuntu")


