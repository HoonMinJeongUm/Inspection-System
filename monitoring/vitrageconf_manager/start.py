
import subprocess
# import ssh_manager.listener

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


    def decode(lsself):
         pass

    def config_vitrage(self):

        path = "/opt/stack/Inspection-System"  # replace here with /etc/vitrage/
        vitrage_conf = "/opt/stack/Inspection-System/test.conf"  # replace here with /etc/vitrage/vitrage.conf
        zabbix_conf = "/opt/stack/Inspection-System/zabbix_conf.yaml"

        # add zabbix to list of datasources in /etc/vitrage/vitrage.conf
        subprocess.call(['sed', "-i", "19s/nova.host/zabbix,nova.host/g", vitrage_conf])

        # add texts to vitrage_conf file
        subprocess.call("echo '[zabbix]' >> '%s'" % vitrage_conf, shell=True)
        subprocess.call("echo 'url = http://'%s'/zabbix' >> '%s'" % (self.server_ip, vitrage_conf), shell=True)
        subprocess.call("echo 'password = '%s'' >> '%s'" % (self.server_pass, vitrage_conf), shell=True)
        subprocess.call("echo 'user = '%s'' >> '%s'" % (self.server_user,vitrage_conf), shell=True)
        subprocess.call("echo 'config_file = /etc/vitrage/zabbix_conf.yaml' >> '%s'" % vitrage_conf, shell=True)

        # make zabbix_conf.yaml file and add texts
        open("%s/zabbix_conf.yaml" % path, 'w').close()
        subprocess.call("echo 'zabbix:' >> '%s'" % zabbix_conf, shell=True)
        subprocess.call("echo '- zabbix_host: '%s'' >> '%s'" % (self.host_name, zabbix_conf), shell=True)
        subprocess.call("echo '  type: '%s'' >> '%s'" % (self.host_type, zabbix_conf), shell=True)
        subprocess.call("echo '  name: '%s'' >> '%s'" % (self.vm_id,zabbix_conf), shell=True)


    def make_script(self):

        install_agent = "/opt/stack/Inspection-System/install_agent.sh"  # use for appending texts to script (real path in which script is locate )
        path = "/opt/stack/Inspection-System"  # path of script

        open("%s/install_agent.sh" % path, 'w').close()  # make <install_agent> script

        subprocess.call("echo 'sudo apt-get -y update' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo apt-get -y upgrade' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo apt-get -y install zabbix-agent' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo apt-get -y install apache2' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo '\n' >> '%s'" % install_agent, shell=True)

        subprocess.call("echo 'sudo sed -i \"2s/.*/`ifconfig '%s' | grep \"\"\\\"inet addr:\\\"\"\"| cut -d: -f2 | awk \"\"\\\"{ print $1 }\\\"\"\"`/g\" /etc/hosts' >> '%s'" % (self.vm_interface, install_agent), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/etc/hosts\"' >> '%s'" % install_agent,shell=True)
        subprocess.call("echo 'sudo sed -i \"3s/.*/'%s'\tmonitor/g\" \"/etc/hosts\"' >> '%s'" % (self.vm_ip, install_agent),shell=True)
        subprocess.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo echo \"zabbix ALL=NOPASSWD: ALL\" >> /etc/sudoers' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo '\n' >> '%s'" % install_agent, shell=True)

        subprocess.call( "echo 'sudo sed -i \"s/# EnableRemoteCommands=0/EnableRemoteCommands=1/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % install_agent,shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Server=127.0.0.1/Server='%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, install_agent), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/ServerActive=127.0.0.1/ServerActive='%s':'%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.server_port, install_agent), shell=True)
        subprocess.call("echo 'sudo sed -i \"s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % install_agent,shell=True)
        subprocess.call("echo '\n' >> '%s'" % install_agent, shell=True)

        subprocess.call("echo 'sudo service apache2 restart' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo service zabbix-agent restart' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo echo \"ubuntu:ubuntu\" | chpasswd' >> '%s'" % install_agent, shell=True)
        subprocess.call("echo 'sudo echo \"root:root\" | chpasswd' >> '%s'" % install_agent, shell=True)

        # os.chmod("%s/install_agent" %path,0777)     #make <install_agent> shell script execute
        # ssh_manager.listener.start_script(host_ip, )  # hosts,auth,file_name,local_path,remote_path



if  Vitrageconf_manager.monitoring_tool == "Zabbix" :



