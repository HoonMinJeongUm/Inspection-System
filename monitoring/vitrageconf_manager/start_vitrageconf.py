
import subprocess
#import ssh_manager.listener

class Vitrageconf_manager(object):

    def __init__(self):
        self.monitoring_tool = "Zabbix"
        self.server_ip = "192.168.11.121"
        self.server_port = "22"
        self.server_pass = "Zabbix"
        self.server_user = "admin"
        self.host_name = ""
        self.host_type = ""
        self.vm_ip =  ["x.x.x.x","y.y.y.y"]
        self.vm_id = ["ddd","fff"]
        self.vm_interface= ["eno1", "eno2"]

        self.script = "/opt/stack/Inspection-System/install_agent.sh"                 # use for appending texts to script (real path in which script is locate )
        self.path_script = "/opt/stack/Inspection-System"                            # path of script

        self.path_vitrage = "/opt/stack/Inspection-System"                           # replace here with /etc/vitrage/
        self.vitrage_conf = "/opt/stack/Inspection-System/test.conf"  # replace here with /etc/vitrage/vitrage.conf
        self.zabbix_conf = "/opt/stack/Inspection-System/zabbix_conf.yaml"

    def decode(self):
         pass

    def config_vitrage(self):


        # add zabbix to list of datasources in /etc/vitrage/vitrage.conf
        subprocess.call(['sed', "-i", "19s/nova.host/zabbix,nova.host/g", self.vitrage_conf])

        # add texts to vitrage_conf file
        subprocess.call("echo '[zabbix]' >> '%s'" % self.vitrage_conf, shell=True)
        subprocess.call("echo 'url = http://'%s'/zabbix' >> '%s'" % (self.server_ip, self.vitrage_conf), shell=True)
        subprocess.call("echo 'password = '%s'' >> '%s'" % (self.server_pass, self.vitrage_conf), shell=True)
        subprocess.call("echo 'user = '%s'' >> '%s'" % (self.server_user,self.vitrage_conf), shell=True)
        subprocess.call("echo 'config_file = /etc/vitrage/zabbix_conf.yaml' >> '%s'" % self.vitrage_conf, shell=True)

        # make zabbix_conf.yaml file and add texts
        open("%s/zabbix_conf.yaml" % self.path_vitrage, 'w').close()
        subprocess.call("echo 'zabbix:' >> '%s'" % self.zabbix_conf, shell=True)
        subprocess.call("echo '- zabbix_host: '%s'' >> '%s'" % (self.host_name, self.zabbix_conf), shell=True)
        subprocess.call("echo '  type: '%s'' >> '%s'" % (self.host_type, self.zabbix_conf), shell=True)
        subprocess.call("echo '  name: '%s'' >> '%s'" % (self.vm_id,self.zabbix_conf), shell=True)


    def make_script(self):

        open("%s/install_agent.sh" % self.path_script, 'w').close()  # make <install_agent> script

        subprocess.call("echo 'sudo apt-get -y update' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y upgrade' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y install zabbix-agent' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo apt-get -y install apache2' >> '%s'" % self.script, shell=True)
        subprocess.call("echo '\n' >> '%s'" % self.script, shell=True)

        subprocess.call("echo 'sudo sed -i \"2s/.*/`ifconfig '%s' | grep \"\"\\\"inet addr:\\\"\"\"| cut -d: -f2 | awk \"\"\\\"{ print $1 }\\\"\"\"`/g\" /etc/hosts' >> '%s'" % (self.vm_interface, self.script), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/etc/hosts\"' >> '%s'" % self.script,shell=True)
        subprocess.call("echo 'sudo sed -i \"3s/.*/'%s'\tmonitor/g\" \"/etc/hosts\"' >> '%s'" % (self.vm_ip, self.script),shell=True)
        subprocess.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo echo \"zabbix ALL=NOPASSWD: ALL\" >> /etc/sudoers' >> '%s'" % self.script, shell=True)
        subprocess.call("echo '\n' >> '%s'" % self.script, shell=True)

        subprocess.call( "echo 'sudo sed -i \"s/# EnableRemoteCommands=0/EnableRemoteCommands=1/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % self.script,shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Server=127.0.0.1/Server='%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.script), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/ServerActive=127.0.0.1/ServerActive='%s':'%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.server_port, self.script), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % self.script, shell=True)
        subprocess.call("echo '\n' >> '%s'" % self.script, shell=True)

        subprocess.call("echo 'sudo service apache2 restart' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo service zabbix-agent restart' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo echo \"ubuntu:ubuntu\" | chpasswd' >> '%s'" % self.script, shell=True)
        subprocess.call("echo 'sudo echo \"root:root\" | chpasswd' >> '%s'" % self.script, shell=True)

        # os.chmod("%s/install_agent" %path,0777)     #make <install_agent> shell script execute
        #ssh_manager.listener.start_script(self.vm_ip,self. )  # hosts,auth,file_name,local_path,remote_path

a= Vitrageconf_manager()


if  a.monitoring_tool == "Zabbix" :

    a.config_vitrage()
    a.make_script()