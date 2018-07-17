import fabfile
import os
import sys
import subprocess

# from fabric.api import run,env,execute,task

#
#
# env.user = 'root'
# env.password = 'root'
# env.hosts=['192.168.10.101','192.168.10.102','192.168.10.103']



def result_parser():
    pass
def start_command():
    """
    For command, use two authentication methods:
    1. Use the host's common user, pwd
    2. Assume that public and private keys are in VM

    """
    command = 'uname -a'


    # os.system('fab -H 192.168.11.3 -p stack run_ssh')
    print("############################################")
    output = subprocess.Popen(['fab','run_ssh:' + command],stdout=subprocess.PIPE).stdout
    result = output.read().strip()
    output.close()

    print("result  Type : : : ", type(result))
    print("result  : : : ",result.decode(encoding="utf-8"))
    print("############################################")


def start_script():
    pass

start_command()