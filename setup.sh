#!/usr/bin/env bash

sudo apt-get update
#sudo apt-get purge -y libreoffice*
#sudo apt-get -y clean
#sudo apt-get -y autoremove

sudo apt-get install -y\
    build-essential python3-dev python3-pip libfreetype6-dev libjpeg-dev\
    i2c-tools\
    python3-smbus\
    libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev\
    util-linux procps hostapd iproute2 iw haveged dnsmasq

sudo pip3 install -Ur requirements.txt

echo "Configuring create_ap"
#sudo git clone https://github.com/oblique/create_ap
#cd //home/pi/create_ap && sudo make install

echo "Installing service..."
sudo make install

echo "Restarting..."
#sudo reboot
