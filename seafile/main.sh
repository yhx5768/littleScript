#!/usr/bin/env bash

if [[ ! -z $SUDO_USER]]; then
    echo "Don't run this in sudo!!"
    exit 1
fi

# Preparation Phase
mkdir ~/Tools/Seafile
cd ~/Tools/Seafile

wget http://seafile-downloads.oss-cn-shanghai.aliyuncs.com/seafile-server_6.2.2_x86-64.tar.gz

tar -xzf seafile-server_*
mkdir installed
mv seafile-server_* installed

# Prerequisites
sudo apt update
sudo apt install -y python2.7 libpython2.7 python-setuptools python-imaging python-ldap python-urllib3 ffmpeg python-pip python-mysqldb python-memcache
pip install pillow moviepy

# Setup
cd seafile-server-*
./setup-seafile-mysql.sh

sudo cp config/seafile.conf /etc/nginx/site-available/
sudo ln -s /etc/nginx/sites-available/seafile.conf /etc/nginx/sites-enabled/seafile.conf

# SERVICE_URL: http://www.myseafile.com
# FILE_SERVER_ROOT: http://www.myseafile.com/seafhttp

sudo cp config/seafile.service /etc/systemd/system/
sudo cp config/seahub.service /etc/systemd/system/

sudo systemctl enable seafile.service
sudo systemctl enable seahub.service
