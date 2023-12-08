#!/usr/bin/python3
"""
a Module that contains a do_deploy function.
"""

from fabric.api import env, run, put, local
import os
from datetime import datetime

env.hosts = ['54.237.218.141', '34.232.53.132']


def do_deploy(archive_path):
    """
    A Fabric script that distributes an archive to your web servers
    """

    # Check if the archive file exists
    if not os.path.exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, "/tmp/")

        # Extract the archive to
        # /data/web_static/releases/<filename without extension>/
        archive_filename = os.path.basename(archive_path)
        release_folder = (
                f"/data/web_static/releases/{archive_filename.split('.')[0]}"
                )
        run(f"mkdir -p {release_folder}")
        run(f"tar -xzf /tmp/{archive_filename} -C {release_folder}")

        # Remove the archive from the web server
        run(f"rm /tmp/{archive_filename}")

        # Synchronize contents to appropriate location
        run(f"rsync -av {release_folder}/web_static/ {release_folder}")

        # Remove the old symbolic link
        run("rm -rf /data/web_static/current")

        # Update the symbolic link
        run(f"ln -s {release_folder} /data/web_static/current")

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Error: {e}")
        return False
