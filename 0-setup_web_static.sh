#!/usr/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html
echo "I HAVE ARRIVED" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="location /hbnb_static/ {\n    alias /data/web_static/current/;\n    index index.html;\n}\n"

sudo sed -i "/server_name _;/a $nginx_config" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
