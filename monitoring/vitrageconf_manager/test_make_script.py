import subprocess

install_agent = "/opt/stack/Inspection-System/install_agent.sh"                    #use for appending texts to script (real path in which script is locate )
path = "/opt/stack/Inspection-System"                                           #path of script
interface_vnf = "enx88366cf34c52"                                                          #replace here with Interface name in VNF
host_ip = "x.x.x.x"                                                             #replace here with Zabbix host IP address
server_ip = "y.y.y.y"                                                           #replace here with Zabbix server IP address
server_port="22"                                                                #replace here with Zabbix server port


# interface_vnf, host_ip, server_ip, server_port have to be input argument
def make_script() :


    subprocess.call("echo 'sudo sed -i \"2s/.*/`ifconfig '%s' | grep \"inet addr:\"| cut -d: -f2 | awk \"{ print $1 }\"`/g\" \"/opt/stack/Inspection-System/testhosts\"' >> '%s'" %(interface_vnf, install_agent), shell=True)
    subprocess.call("echo 'sudo sed -i \"s/Bcast/`cat /etc/hostname`/g\" \"/opt/stack/Inspection-System/testhosts\"' >> '%s'" %install_agent, shell=True)
    subprocess.call("echo 'sudo sed -i \"3s/.*/'%s'\\\tmonitor/g\" \"/opt/stack/Inspection-System/testhosts\"' >> '%s'" %(host_ip ,install_agent), shell=True)
    #subprocess.call("echo 'sudo /etc/init.d/networking restart' >> '%s'" %install_agent, shell=True)
    #subprocess.call("echo 'sudo echo \"zabbix ALL=NOPASSWD: ALL\" >> /etc/sudoers' >> '%s'" %install_agent, shell=True)
    #subprocess.call("echo '\n' >> '%s'" %install_agent, shell=True)

make_script()