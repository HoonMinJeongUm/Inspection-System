import fabfile
import subprocess

def change_mark(sample):
    return str(sample).replace(',', '?')

def start_command(hosts,auth,command):
    """
    For command, use two authentication methods:
    1. Use the host's common user, pwd
    2. Assume that public and private keys are in VM
    hosts = list
    auth = list
    command = string
    return 'String'

    """

    output = subprocess.Popen(['fab','start_ssh:' +command+","+change_mark(hosts)+","+change_mark(auth)],
                              stdout=subprocess.PIPE).stdout
    result = output.read().strip()
    output.close()
    print("===================================================================")
    print(result.decode(encoding="utf-8"))
    print("===================================================================")
def start_script():
    pass

def result_parser():
    pass

start_command(['192.168.11.3','192.168.11.31'],['stack','stack'],'uname -a')
