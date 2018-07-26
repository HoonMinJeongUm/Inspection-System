import subprocess

"""

"""
vitrage_conf = "/opt/stack/Inspection-System/test.conf"  # replace here with /etc/vitrage/vitrage.conf
password = "zabbix"
path = "/opt/stack/Inspection-System"                    # replace here with /etc/vitrage/
zabbix_conf = "/opt/stack/Inspection-System/zabbix_conf.yaml"
ip = "f.f.f.f"                                          # server ip
Zabbix_host = "Zabbix server"
type = "nova.host"


def config_vitrage():


    # add zabbix to list of datasources in /etc/vitrage/vitrage.conf
    subprocess.call(['sed', "-i", "19s/nova.host/zabbix,nova.host/g", vitrage_conf])

    # add texts to vitrage_conf file
    subprocess.call("echo '[zabbix]' >> '%s'" %vitrage_conf, shell=True)
    subprocess.call("echo 'url = http://'%s'/zabbix' >> '%s'" %(ip, vitrage_conf), shell=True)
    subprocess.call("echo 'password = %s' >> '%s'" %(password, vitrage_conf), shell=True)
    subprocess.call("echo 'user = admin' >> '%s'" %vitrage_conf, shell=True)
    subprocess.call("echo 'config_file = /etc/vitrage/zabbix_conf.yaml' >> '%s'" %vitrage_conf, shell=True)

    #make zabbix_conf.yaml file and add texts
    open("%s/zabbix_conf.yaml" %path,'w').close()
    subprocess.call("echo 'zabbix:' >> '%s'" %zabbix_conf, shell=True)
    subprocess.call("echo '- zabbix_host: '%s'' >> '%s'" %(Zabbix_host, zabbix_conf), shell=True)
    subprocess.call("echo '  type: '%s'' >> '%s'" %(zabbix_conf, type), shell=True)
    subprocess.call("echo '  name: Zabbix server' >> '%s'" %zabbix_conf, shell=True)

