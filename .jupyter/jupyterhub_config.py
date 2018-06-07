import os

from jupyterhub.spawner import LocalProcessSpawner

class DefaultUserLocalProcessSpawner(LocalProcessSpawner):

    def user_env(self, env):
        env['USER'] = 'default'
        env['HOME'] = '/opt/app-root/data/%s' % self.user.name
        env['SHELL'] = '/bin/bash'
        return env
    
    def get_env(self):
        env = super().get_env()
        if self.user_options.get('env'):
            env.update(self.user_options['env'])
        env['LD_LIBRARY_PATH'] = os.environ['LD_LIBRARY_PATH']
        env['LD_PRELOAD'] = os.environ['LD_PRELOAD']
        env['NSS_WRAPPER_PASSWD'] = os.environ['NSS_WRAPPER_PASSWD']
        env['NSS_WRAPPER_GROUP'] = os.environ['NSS_WRAPPER_GROUP']
        return env

    def make_preexec_fn(self, name):
        def preexec():
            home = '/opt/app-root/data/%s' % name
            if not os.path.exists(home):
                os.mkdir(home)
            os.chdir(home)
        return preexec

c.JupyterHub.spawner_class = DefaultUserLocalProcessSpawner

idle_timeout = os.environ.get('JUPYTERHUB_IDLE_TIMEOUT')

if idle_timeout and int(idle_timeout):
    c.JupyterHub.services = [
        {
            'name': 'cull-idle',
            'admin': True,
            'command': ['cull-idle-servers', '--timeout=%s' % idle_timeout],
        }
    ]
