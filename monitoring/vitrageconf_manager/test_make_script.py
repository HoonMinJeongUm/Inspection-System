import a

class Vitrageconf_manager(object):

    def __init__(self):
        self.monitoring_tool = "Zabbix"
        self.server_ip = "192.168.11.61"
        self.server_port = "22"
        self.server_pass = "Zabbix"
        self.server_user = "admin"
        self.host_name = "192.168.11.61"
        self.host_type = "nova.host"
        self.vm_ip =  ["x.x.x.x","y.y.y.y"]
        self.vm_id = "192.168.11.61"
        self.vm_interface= ["eno1", "eno2"]

        self.script = "/opt/stack/Inspection-System/install_agent.sh"                 # use for appending texts to script (real path in which script is locate )
        self.path_script = "/opt/stack/Inspection-System"                            # path of script

        self.path_vitrage = "/etc/vitrage"                           # replace here with /etc/vitrage
        self.vitrage_conf = "/etc/vitrage/vitrage.conf"  # replace here with /etc/vitrage/vitrage.conf
        self.zabbix_conf = "/etc/vitrage/zabbix_conf.yaml"      # replace here with




    def make_script(self):
        open("%s/install_agent.sh" % self.path_script, 'w').close()  # make <install_agent> script

        a.call("echo 'sudo apt-get -y update' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo apt-get -y upgrade' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo apt-get -y install zabbix-agent' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo apt-get -y install apache2' >> '%s'" % self.script, shell=True)
        a.call("echo '\n' >> '%s'" % self.script, shell=True)

        a.call("echo 'sudo sed -i \"2s/.*/`ifconfig '%s' | grep \"inet addr:\"| cut -d: -f2 | awk \"{ print $1 }\"`/g\" \"/opt/stack/Inspection-System/testhosts\"' >> '%s'" % (self.vm_interface, self.script), shell=True)  # replace testhosts to /etc/hosts
        a.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/opt/stack/Inspection-System/testhosts\"' >> '%s'" % self.script, shell=True)  # replace testhosts to /etc/hosts
        a.call("echo 'sudo sed -i \"3s/.*/'%s'\\\tmonitor/g\" \"/opt/stack/Inspection-System/testhosts\"' >> '%s'" % (self.vm_ip, self.script), shell=True)  # replace testhosts to /etc/hosts
        a.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo echo \"zabbix ALL=NOPASSWD: ALL\" >> /etc/sudoers' >> '%s'" % self.script, shell=True)
        a.call("echo '\n' >> '%s'" % self.script, shell=True)

        a.call("echo 'sudo sed -i \"s/# EnableRemoteCommands=0/EnableRemoteCommands=1/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo sed -i \"s/Server=127.0.0.1/Server='%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.script), shell=True)
        a.call("echo 'sudo sed -i \"s/ServerActive=127.0.0.1/ServerActive='%s':'%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % (self.server_ip, self.server_port, self.script), shell=True)
        a.call("echo 'sudo sed -i \"s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" % self.script, shell=True)
        a.call("echo '\n' >> '%s'" % self.script, shell=True)

        a.call("echo 'sudo service apache2 restart' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo service zabbix-agent restart' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo echo \"ubuntu:ubuntu\" | chpasswd' >> '%s'" % self.script, shell=True)
        a.call("echo 'sudo echo \"root:root\" | chpasswd' >> '%s'" % self.script, shell=True)
