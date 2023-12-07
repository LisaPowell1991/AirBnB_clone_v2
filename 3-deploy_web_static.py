#!/usr/bin/python3
"""
A Fabric script that creates and distributes an archive to your web servers.
"""

from fabric.api import local, env
from fabric.operations import put
from os.path import exists

env.hosts = ['54.237.218.141', '34.232.53.132']
env.user = 'ubuntu'


def do_pack():
    """
    Generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo.
    """

    try:
        # create versions folder if it doesn't exists
        local("mkdir -p versions")

        # Generate current timestamp for archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Define archive name
        archive_name = f"web_static_{timpestamp}.tgz"

        # Compress content of of web_static folder into archive
        local(f"tar -czvf versions/{archive_name} web_static")

        # If an error occurs
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    A Fabric script that distributes an archive to your web servers
    """

    # Check if archive file exists
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ dir of the web server
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/
        # <archive filename without extension>
        filename = archive_path.split('.')[-1]
        folder_name = f"/data/web_static/releases/{filename.split('.')[0]}"
        run(f"mkdir -p {folder_name}")
        run(f"tar -xzf /tmp/{filename} -C {folder_name}")

        # Delete the archive from the web server
        run(f"rm /tmp/{filename}")

        # Delete the symbolic link /data/web_static/current
        run("rm -f /data/web_static/current")

        # Create a new symbolic link /data/web_static/current
        # linked to the new version
        run(f"ln -s {folder_name} /data/web_static/current")

        return True

    except Exception as e:
        return False


def deploy():
    """
    Create and distribute the archive to your web servers
    """

    archive_path = do_pack()

    if not archive_path:
        return False

    return do_deploy(archive_path)
