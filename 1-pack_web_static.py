#!/usr/bin/python3
"""
This module provides a function to create a .tgz archive from web_static folder
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if successful, None otherwise.
    """
    # Create the versions folder if it doesn't exist
    local('mkdir -p versions')

    # Format the current timestamp for the archive name
    timestamp = datetime.utcnow().strftime('%Y%m%d%H%M%S')

    # Create the archive file name
    archive_name = 'web_static_{}.tgz'.format(timestamp)

    # Compress the web_static folder into the archive
    result = local('tar -cvzf versions/{} web_static'.format(archive_name))

    # Check if the compression was successful
    if result.failed:
        return None
    else:
        return os.path.abspath('versions/{}'.format(archive_name))
