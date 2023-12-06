#!/usr/bin/env bash
# a Bash script that sets up your web servers for the deployment of web_static.

# Install Nginx if it's not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders if they don't exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file for testing
echo "<html><head></head><body>Hello World!!</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link to index.html
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx config
config_content=$(cat <<EOL
server {
    listen 80;
    server_name _;
    location /hbnb_static {
        alias /data/web_static/current/;
    }
    error_page 404 /404.html;
    location = /404.html {
        root /usr/share/nginx/html;
        internal;
    }
}
EOL
)

echo "$config_content" | sudo tee /etc/nginx/sites-available/default

# Restart Nginx to apply changes
sudo service nginx restart
