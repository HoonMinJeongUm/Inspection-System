
import subprocess
#import ssh_manager.listener

install_agent = "/opt/stack/Inspection-System/install_agent.sh"                    #use for appending texts to script (real path in which script is locate )
path = "/opt/stack/Inspection-System"                                              #path of script

interface_vnf = ["eno1", "eno2"]                                                          #replace here with Interface name in VNF
vm_ip = ["x.x.x.x","y.y.y.y"]                                                             #replace here with Zabbix host IP address

server_ip = "y.y.y.y"                                                           #replace here with Zabbix server IP address
server_port="22"                                                                #replace here with Zabbix server port







# interface_vnf, host_ip, server_ip, server_port have to be input argument
def make_script() :

    open("%s/install_agent.sh" % path, 'w').close()  # make <install_agent> script

    subprocess.call("echo 'sudo apt-get -y update' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo apt-get -y upgrade' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo apt-get -y install zabbix-agent' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo apt-get -y install apache2' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo '\n' >> '%s'" %install_agent, shell=True)


    subprocess.call("echo 'sudo sed -i \"2s/.*/`ifconfig '%s' | grep \"\"\\\"inet addr:\\\"\"\"| cut -d: -f2 | awk \"\"\\\"{ print $1 }\\\"\"\"`/g\" /etc/hosts' >> '%s'" %(interface_vnf, install_agent), shell=True)
    subprocess.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/etc/hosts\"' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo sed -i \"3s/.*/'%s'\tmonitor/g\" \"/etc/hosts\"' >> '%s'" %(vm_ip ,install_agent), shell=True)
    subprocess.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo echo \"zabbix ALL=NOPASSWD: ALL\" >> /etc/sudoers' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo '\n' >> '%s'" %install_agent, shell=True)


    subprocess.call("echo 'sudo sed -i \"s/# EnableRemoteCommands=0/EnableRemoteCommands=1/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo sed -i \"s/Server=127.0.0.1/Server='%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %(server_ip, install_agent), shell=True)
    subprocess.call("echo 'sudo sed -i \"s/ServerActive=127.0.0.1/ServerActive='%s':'%s'/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %(server_ip, server_port,install_agent), shell=True)
    subprocess.call("echo 'sudo sed -i \"s/Hostname=Zabbix server/Hostname=`cat /etc/hostname`/\" \"/etc/zabbix/zabbix_agentd.conf\"' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo '\n' >> '%s'" %install_agent, shell=True)


    subprocess.call("echo 'sudo service apache2 restart' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo service zabbix-agent restart' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo echo \"ubuntu:ubuntu\" | chpasswd' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo echo \"root:root\" | chpasswd' >> '%s'" %install_agent, shell=True)


    #os.chmod("%s/install_agent" %path,0777)     #make <install_agent> shell script execute

    #ssh_manager.listener.start_script(host_ip, )  # hosts,auth,file_name,local_path,remote_path