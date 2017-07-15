from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import task
from fabric.context_managers import cd, lcd

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
    return compose_cmd + ['docker-compose-%s.yml' % renv]


def get_fn():
    return run if renv == 'prd' else local


def get_cmd_exists(cmd):
    def tell_on(arg, rs):
        if rs:
            print('"%s" found in path.' % arg)
        else:
            print('"%s" not found in path. Cannot continue.' % arg)
        return rs

    fn = get_fn()
    rs = fn('which %s' % cmd, capture=True)
    return tell_on(cmd, ('not found' not in rs))


@task(alias='setup')
def do_setup():
    """
    Helps you setup your environment. Call it once per project.
    """
    assert get_cmd_exists('vue')
    assert get_cmd_exists('npm')
    assert get_cmd_exists('fab')
    assert get_cmd_exists('docker')
    assert get_cmd_exists('docker-compose')

    print("We'll now setup VueJS (just accept defaults)")
    local('vue init webpack ux')

    print("We'll now setup SemanticUI (just accept defaults)")
    with lcd('styles'):
        local('npm install semantic-ui')

    print('Execute:')
    print('  fab env:dev up  # for development mode')
    print('  fab env:prd up  # for production mode')


@task(alias='env')
def set_renv(local_renv):
    "Sets docker-compose environment"
    global renv
    assert local_renv in ('dev', 'prd')
    renv = local_renv


@task(alias='up')
def compose_up(name=None):
    opt = ['-d'] if renv == 'prd' else []

    with cd(project_dst):
        local_cmd = get_compose_cmd() + ['up']
        local_cmd += opt
        local_cmd += [name] if name else []
        get_fn()(' '.join(local_cmd))


@task(alias='build')
def compose_build(name=None):
    with cd(project_dst):
        local_cmd = get_compose_cmd() + ['build']
        local_cmd += [name] if name else []

        get_fn()(' '.join(local_cmd))
