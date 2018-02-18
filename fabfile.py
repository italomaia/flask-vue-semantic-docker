from fabric.api import env
from fabric.api import local
from fabric.api import run
from fabric.api import task
from fabric.context_managers import cd, lcd

import os
import json

env.forward_agent = True
env.user = 'root'
env.hosts = ['your production host']

project_dst = 'project-name'

compose_cmd = [
    'docker-compose',
    '-f', 'docker-compose.yml',
    '-f',
]

# service to run commands against
service_name = None
renv = 'dev'  # dev by default
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
STYLES_DIR = os.path.join(CURRENT_DIR, 'styles')
UX_DIR = os.path.join(CURRENT_DIR, 'ux')


def get_compose_cmd():
    return compose_cmd + ['docker-compose-%s.yml' % renv]


def get_fn():
    """
    Returns the correct function call for the environment.
    """
    return run if renv == 'prd' else local


def get_cmd_exists(cmd):
    def tell_on(arg, rs):
        if rs:
            print('"%s" found in path.' % arg)
        else:
            print('"%s" not found in path. Please, install it to continue.' % arg)  # noqa
        return rs

    fn = get_fn()
    rs = fn('which %s' % cmd, capture=True)
    return tell_on(cmd, ('not found' not in rs))


def insert_line_after(lines, line, after):
    for i in range(len(lines)):
        if after in lines[i]:
            lines.insert(i+1, line)
            break


def update_webpack_base_conf(conf_path):
    with open(conf_path) as fs:
        lines = fs.readlines()

    line_to_insert = ""\
        "  plugins: [\n"\
        "    new webpack.ProvidePlugin({\n"\
        "    '$': 'jquery',\n"\
        "    'jQuery': 'jquery',\n"\
        "    'window.jQuery': 'jquery'\n"\
        "  })],\n"
    line_condition = 'module.exports = {'
    insert_line_after(lines, line_to_insert, line_condition)

    with open(conf_path, 'w') as fs:
        fs.write(''.join(lines))


def update_webpack_dev_conf(conf_path):
    with open(conf_path) as fs:
        lines = fs.readlines()

    # add disable host check; required for development with webpack
    line_to_insert = '    disableHostCheck: true,\n'
    line_condition = 'devServer: {'
    insert_line_after(lines, line_to_insert, line_condition)

    with open(conf_path, 'w') as fs:
        fs.write(''.join(lines))


def update_ux_main(path):
    with open(path) as fs:
        lines = fs.readlines()

    line_to_insert = "\n"\
        "require('./styles/semantic.min.css')\n"\
        "require('./styles/semantic.min.js')\n"
    line_condition = "productionTip"
    insert_line_after(lines, line_to_insert, line_condition)

    with open(path, 'w') as fs:
        fs.write(''.join(lines))


@task(alias='setup')
def do_setup():
    """
    Helps you setup your environment. Call it once per project.
    """
    msg = "Command not found. Please, install %s"
    assert get_cmd_exists('npm'), msg % "npm"
    assert get_cmd_exists('vue'), msg % "vue-cli"
    assert get_cmd_exists('fab'), msg % "fabric3"
    assert get_cmd_exists('docker'), msg % "docker"
    assert get_cmd_exists('docker-compose'), msg % "docker-compose"

    print("Setting up VueJS (just accept defaults)")
    local('vue init webpack ux', shell='/bin/bash')

    update_webpack_base_conf("ux/build/webpack.base.conf.js")
    update_webpack_dev_conf("ux/build/webpack.dev.conf.js")
    update_ux_main("ux/src/main.js")

    with lcd(UX_DIR):
        local("yarn add jquery")

    print("Setting up SemanticUI (just accept defaults)")
    with lcd(STYLES_DIR):
        local('npm install semantic-ui', shell='/bin/bash')

        semantic_settings = os.path.join(STYLES_DIR, 'semantic.json')
        with open(semantic_settings, 'r') as fs:
            data = json.load(fs)

        data['autoInstall'] = True
        with open(semantic_settings, 'w') as fs:
            json.dump(data, fs)

    print(
        "IMPORTANT: run the following command:\n"
        "sudo echo \"127.0.0.1  dv\" >> /etc/hosts")

    print(
        "IMPORTANT: make sure to update your envfile file with "
        "your project production configuration.")
    print(
        "IMPORTANT: make sure to update your fabfile "
        "hosts with your production host.")
    print("")
    print("Now you're ready to go:")
    print('  fab env:dev up  # for development mode')
    print('  fab env:prd up  # for production mode')
    print('  fab env:tst up  # to simulate production mode')
    print('Locally, your project will be available at http://dv:8080')


@task(alias='env')
def set_renv(local_renv):
    "Sets docker-compose environment"
    global renv
    assert local_renv in ('dev', 'prd')
    renv = local_renv


@task(alias='up')
def compose_up(name=None):
    """
    Calls docker compose up using the correct environment.
    """
    opt = ['-d'] if renv == 'prd' else []

    with cd(project_dst):
        local_cmd = get_compose_cmd() + ['up']
        local_cmd += opt
        local_cmd += [name] if name else []
        get_fn()(' '.join(local_cmd))


@task(alias='build')
def compose_build(name=None):
    """
    Calls docker compose build using the correct environment.
    """
    with cd(project_dst):
        local_cmd = get_compose_cmd() + ['build']
        local_cmd += [name] if name else []

        get_fn()(' '.join(local_cmd))


@task(alias='on')
def on_service(name):
    """
    Define service where command should run
    """
    global service_name
    service_name = name


@task(alias='run')
def compose_run(cmd):
    """
    Calls docker compose run using the correct environment.

    :param cmd: run command, including container name.
    """
    opt = ['--rm']

    if service_name is None:
        print("please, provide service name")
        exit()

    with cd(project_dst):
        local_cmd = get_compose_cmd() + ['run']
        local_cmd += opt
        local_cmd += [service_name]
        local_cmd += cmd.split()
        get_fn()(' '.join(local_cmd))


@task(alias='logs')
def docker_logs(name):
    """
    Get docker container logs.
    """
    get_fn()('docker logs %s' % name)
