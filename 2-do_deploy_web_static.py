#!/usr/bin/python3
""" deploying archives to multiple server """

from os import path
from fabric.api import env, put, run

env.hosts = ["100.26.166.24", "34.202.233.65"]
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Function that distributes a scropt to my web servers"""
    if path.isfile(archive_path) is False:
        return False
    file = archive_path.split('/')[-1]
    name = file.split('.')[0]

    try:
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}'.format(name))
        run('tar -xzf /tmp/{} -C "/data/web_static/releases/"{}/'.
            format(file, name))
        run('rm /tmp/{}'.format(file))
        run('mv "/data/web_static/releases/"{}\
            /web_static/* "/data/web_static/releases/"{}/'.format(name))
        run('rm -rf "/data/web_static/releases/"{}/web_static'.
            format(name))
        run('rm -rf /data/web_static/current')
        run('ln -s "/data/web_static/releases/"{}/ /data/web_static/current'.
            format(name))
        return True
    except:
        return False
