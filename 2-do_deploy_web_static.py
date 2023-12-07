#!/usr/bin/python3
"""
a Module that contains a do_deploy function.
"""

from fabric.api import env, run, put
from os.path import exists
from datetime import datetime

env.hosts = ['54.237.218.141', '34.232.53.132']
env.user = 'ubuntu'


def do_deploy(archive_path):
    # Check if the archive file exists
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory on the web servers
        put(archive_path, "/tmp/")

        # Get the archive filename without extension
        archive_filename = archive_path.split("/")[-1]
        archive_name_no_ext = archive_filename.split(".")[0]

        # Uncompress the archive to the releases folder on the web servers
        run(f"mkdir -p /data/web_static/releases/{archive_name_no_ext}")
        run(f"tar -xzf /tmp/{archive_filename} "
            f"-C /data/web_static/releases/{archive_name_no_ext}")

        # Delete the archive from the web servers
        run(f"rm /tmp/{archive_filename}")

        # Delete the existing symbolic link
        run("rm -f /data/web_static/current")

        # Create a new symbolic link to the new version of the code
        run(f"ln -s /data/web_static/releases/{archive_name_no_ext} "
            f"/data/web_static/current")

        return True

    except Exception as e:
        return False
