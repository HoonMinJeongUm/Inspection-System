from fabric.api import run,env,execute,task

env.user = 'stack'
env.password = 'stack'
env.hosts=['192.168.11.3','192.168.11.31']

def run_ssh(command):
    run(command)


def run_script():
    pass