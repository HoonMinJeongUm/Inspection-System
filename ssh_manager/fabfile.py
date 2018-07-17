from fabric.api import run,env,execute,task,parallel,put
def result_parser():
    pass

def get_hostlist(hosts):
    tmphost = hosts.replace('\'', '').replace('[', '').replace(']', '').strip()
    return tmphost.replace(' ','').split('?')

def get_authlist(auth):
    tmpauth = auth.replace('\'','').replace('[','').replace(']','').strip().strip()
    return tmpauth.replace(' ','').split('?')

def env_setting(hosts,auth):

    tmpauth = get_authlist(auth)
    env.user = tmpauth[0]

    if '/' in tmpauth[1]:
        env.key_filename.append = tmpauth[1]
        print(env.key_filename)
    else :
        env.password = tmpauth[1]

    env.hosts = get_hostlist(hosts)

def run_ssh(command):
    run(command)

def run_script(local_path, remote_path,file_name):
    execute(run_ssh, 'mkdir -p ' + remote_path)
    put(local_path+'/'+file_name,remote_path+'/'+file_name)
    execute(run_ssh,'. '+remote_path+'/'+file_name)

@task
def start_ssh(*args):
    execute(env_setting,args[1],args[2])
    execute(run_ssh,args[0])

@task
def start_script(hosts,auth,local_path,remote_path,file_name):
    execute(env_setting, hosts,auth)
    execute(run_script, local_path,remote_path,file_name)
