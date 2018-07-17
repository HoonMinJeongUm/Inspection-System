from fabric.api import run,env,execute,task,parallel
def result_parser():
    pass

def get_hostlist(hosts):
    tmphost = hosts.replace('\'', '').replace('[', '').replace(']', '').strip()
    return tmphost.replace(' ','').split('?')

def get_authlist(auth):
    tmpauth = auth.replace('\'','').replace('[','').replace(']','').strip().strip()
    return tmpauth.replace(' ','').split('?')

# @parallel
def env_setting(hosts,auth):

    tmpauth = get_authlist(auth)
    env.user = tmpauth[0]

    if '/' in tmpauth[1]:
        env.key_filename.append = tmpauth[1]
        print(env.key_filename)
    else :
        env.password = tmpauth[1]

    env.hosts = get_hostlist(hosts)

# @parallel
def run_ssh(command):
    run(command)

@task
def start_ssh(*args):
    execute(env_setting,args[1],args[2])
    execute(run_ssh,args[0])


def run_script():
    pass
