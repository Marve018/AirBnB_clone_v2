#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using do_deploy function.
"""

from fabric.api import run, put, sudo, env
from os.path import exists

env.hosts = ['34.207.58.155', '54.160.85.28']
env.user = 'ubuntu'

def do_deploy(archive_path):
    """
    Distribute an archive to web servers.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        bool: True if all operations were successful, False otherwise.
    """
    if not exists(archive_path):
        print("Error: Archive not found at {}".format(archive_path))
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to /data/web_static/releases/
        archive_basename = archive_path.split('/')[-1]
        release_folder = '/data/web_static/releases/{}'.format(archive_basename.split(".")[0])
        sudo('mkdir -p {}'.format(release_folder))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_basename, release_folder))

        # Remove the archive from the web server
        sudo('rm /tmp/{}'.format(archive_basename))

        # Delete the symbolic link /data/web_static/current
        current_link = '/data/web_static/current'
        if exists(current_link):
            sudo('rm {}'.format(current_link))

        # Create a new symbolic link
        sudo('ln -s {} {}'.format(release_folder, current_link))

        print("New version deployed successfully!")
        return True

    except Exception as e:
        print("Error during deployment: {}".format(str(e)))
        return False
