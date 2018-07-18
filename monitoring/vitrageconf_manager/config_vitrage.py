import subprocess

vitrage_conf = "/opt/stack/Inspection-System/test.conf"  # replace here with /etc/vitrage/vitrage.conf
ip = "192.168.11.121"                                    # replace here with zabbix agent ip
password = "zabbix"
path = "/opt/stack/Inspection-System"                    # replace here with /etc/vitrage/
zabbix_conf = "/opt/stack/Inspection-System/zabbix_conf.yaml"

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
subprocess.call("echo '- zabbix_host: Zabbix server' >> '%s'" %zabbix_conf, shell=True)
subprocess.call("echo '  type: nova.host' >> '%s'" %zabbix_conf, shell=True)
subprocess.call("echo '  name: Zabbix server' >> '%s'" %zabbix_conf, shell=True)
