#!/usr/bin/python3
"""
A module that contains a do_pack function
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the
    web_static folder of your AirBnB Clone repo.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Generate current timestamp for the archive name
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Define the archive name
        archive_name = f"web_static_{timestamp}.tgz"

        # Compress the content of the web_static folder into the archive
        local(f"tar -czvf versions/{archive_name} web_static")

        # Return archive path if successful
        return f"versions/{archive_name}"

    # If error occures
    except Exception as e:
        return None
