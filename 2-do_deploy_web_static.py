#!/usr/bin/python3
"""
a Module that contains a do_deploy function.
"""

from fabric.api import env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['54.237.218.141', '34.232.53.132']


def do_deploy(archive_path):
    """
    A Fabric script that distributes an archive to your web servers
    """

    # Check if the archive file exists
    if not exists(archive_path):
        return False

    try:
        # Get the archive file name without extension
        archive_name = archive_path.split('/')[-1].split('.')[0]

        # Upload the archive to the /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Uncompress the archive to the folder
        # /data/web_static/releases/<archive_name>
        run(f"mkdir -p /data/web_static/releases/{archive_name}")
        run(f"tar -xzf /tmp/{archive_path.split('/')[-1]} "
            f"-C /data/web_static/releases/{archive_name}")

        # Delete the archive from the web server
        run(f"rm /tmp/{archive_path.split('/')[-1]}")

        # Delete the symbolic link /data/web_static/current
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        run(f"ln -s /data/web_static/releases/{archive_name} "
            f"/data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
