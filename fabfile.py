from fabric import cd
from fabric import env
from fabric import run
from fabric import task

env.forward_agent = True
env.user = 'root'
env.hosts = ['your production host']

project_dst = 'project-name'

compose_cmd = [
    'docker-compose',
    '-f', 'docker-compose.yml',
    '-f',
]

renv = 'dev'  # dev by default


def get_compose_cmd():
    if renv is None:
        raise Exception('env was unset')

    return compose_cmd + ['docker-compose-%s.yml' % renv]


@task(alias='env')
def set_renv(local_renv):
    "Sets docker-compose environment"
    global renv
    assert local_renv in ('dev', 'prd')
    renv = local_renv


@task(alias='up')
def compose_up(name=None):
    opt = []
    with cd(project_dst):
        opt += ['-d'] if renv == 'prd' else []
        local_cmd = get_compose_cmd() + ['up']
        local_cmd += opt
        local_cmd += [name] if name else []
        run(' '.join(local_cmd))


@task(alias='build')
def compose_build(name=None):
    with cd(project_dst):
        local_cmd = get_compose_cmd() + ['build']
        local_cmd += [name] if name else []

        run(' '.join(local_cmd))
