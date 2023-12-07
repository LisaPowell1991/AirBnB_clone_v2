#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get install -y nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/{releases/test,shared}

# Create a fake HTML file for testing
echo "<html>
 <head>
 </head>
 <body>
  Holberton School
 </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx config to serve /data/web_static/current at /hbnb_static/
nginx_config="/etc/nginx/sites-available/default"
nginx_config_backup="$nginx_config.bak" # Backup the original config

# Backup the original config if not backed up already
if [ ! -e "$nginx_config_backup" ]; then
    sudo cp "$nginx_config" "$nginx_config_backup"
fi

# Add or update the location block in Nginx config
sudo sed -i "/location \/ {/a \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" "$nginx_config"

# Restart Nginx to apply changes
sudo service nginx restart

