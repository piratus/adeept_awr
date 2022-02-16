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

## libqt4-test libqtgui4

sudo pip3 install --upgrade\
    luma.oled\
    adafruit-pca9685 rpi_ws281x\
    mpu6050-raspberrypi\
    flask flask_cors websockets numpy\
    imutils zmq pybase64 psutil

sudo pip3 install opencv-contrib-python==3.4.3.18

echo "Configuring create_ap"
#sudo git clone https://github.com/oblique/create_ap
#cd //home/pi/create_ap && sudo make install

echo "Installing service..."
#sudo touch //home/pi/startup.sh
#sudo chmod 777 //home/pi/startup.sh
#sudo touch /etc/modprobe.d/snd-blacklist.conf

echo "Restarting..."
#sudo reboot
