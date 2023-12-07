#!/usr/bin/env bash

# Set directory structures
data_dir="/data"
web_static_dir="$data_dir/web_static"
releases_dir="$web_static_dir/releases"
shared_dir="$web_static_dir/shared"
test_dir="$releases_dir/test"

# Install Nginx
if ! command -v nginx &> /dev/null; then
  echo "Installing Nginx..."
  sudo apt-get update
  sudo apt-get install -y nginx
fi

# Create necessary directories
mkdir -p "$data_dir" "$web_static_dir" "$releases_dir" "$shared_dir"
mkdir -p "$test_dir"

# Create test HTML file
echo "<html>
<head>
</head>
<body>
  Holberton School
</body>
</html>" > "$test_dir/index.html"

# Create/recreate symbolic link
rm -f "$web_static_dir/current" || true
ln -sf "$test_dir" "$web_static_dir/current"

# Set ownership
sudo chown -R ubuntu:ubuntu "$data_dir"

# Update Nginx configuration
sed -i "26i \\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

echo "Web server setup complete!"

