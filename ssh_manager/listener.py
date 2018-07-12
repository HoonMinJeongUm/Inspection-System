import fabfile
import os
import sys
import subprocess


def selectCase():
    pass
def start():
    # os.system('fab -H 192.168.11.3 -p stack run_ssh')
    print("############################################")
    output = subprocess.Popen(['fab','-H', '192.168.11.3', '-p', 'stack','run_ssh'],stdout=subprocess.PIPE).stdout
    result = output.read().strip()
    output.close()
    print("result  : : : ",result)
    print("############################################")


start()