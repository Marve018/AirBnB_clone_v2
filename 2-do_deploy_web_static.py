#!/usr/bin/python3
"""
Fabric script to distribute an archive to web servers using do_deploy function.
"""

from fabric.api import run, put, sudo, env
import os

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
    try:
        # Check if the archive file exists
        if not os.path.exists(archive_path):
            raise FileNotFoundError("Error: Archive not found at {}".format(archive_path))

        # Extract necessary information from the archive path
        archive_filename = os.path.basename(archive_path)
        tmp_archive_path = "/tmp/{}".format(archive_filename)
        folder = archive_filename.split('.')[0]
        release_folder = "/data/web_static/releases/{}/".format(folder)

        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, tmp_archive_path)

        # Create the release folder if it doesn't exist
        run("sudo mkdir -p {}".format(release_folder))

        # Extract the archive to the release folder
        run("sudo tar -xzf {} -C {}".format(tmp_archive_path, release_folder))

        # Remove the temporary archive file
        run("sudo rm {}".format(tmp_archive_path))

        # Move the contents to the release folder and clean up
        run("sudo mv -f {}web_static/* {}".format(release_folder, release_folder))
        run("sudo rm -rf {}web_static".format(release_folder))

        # Remove the old /data/web_static/current symbolic link
        run("sudo rm -rf /data/web_static/current")

        # Create a new symbolic link pointing to the new release
        run("sudo ln -s {} /data/web_static/current".format(release_folder))

        print("Deployment successful!")
        return True

    except Exception as e:
        print("Error during deployment: {}".format(str(e)))
        return False
