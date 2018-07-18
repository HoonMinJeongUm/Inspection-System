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
    # start_command(['192.168.11.3','192.168.11.31'],['stack','stack'],'uname -a') <= TEST Line

    """
    # YOU NEED STACK USER
    output = subprocess.Popen(['fab','-f','~/Inspection-System/ssh_manager/fabfile.py','start_ssh:' +command+","+change_mark(hosts)+
                               ","+change_mark(auth)],stdout=subprocess.PIPE).stdout
    result = output.read().strip()
    output.close()
    print("===================================================================")
    print(result.decode(encoding="utf-8"))
    print("===================================================================")
    return result.decode(encoding="utf-8")


def start_script(hosts,auth,file_name,local_path,remote_path):

    """
    hosts = list
    auth = list(PWD or Key Path)
    local_path = local script file path
    remote_path = remote script file path
    return 'String'
    # start_script(['192.168.11.3','192.168.11.31'],['stack','stack'],'test.sh','/opt/stack','/opt/stack/test') <= TEST Line

    """

    output = subprocess.Popen(['fab','start_script:'+change_mark(hosts)+","+change_mark(auth)
                               +","+local_path+","+remote_path+","+file_name],
                              stdout=subprocess.PIPE).stdout
    result = output.read().strip()
    output.close()
    print("===================================================================")
    print(result.decode(encoding="utf-8"))
    print(type(result.decode(encoding="utf-8")))
    print("===================================================================")
    return result.decode(encoding="utf-8")
