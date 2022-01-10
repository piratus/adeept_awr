#!/usr/bin/python3
import os

curpath = os.path.realpath(__file__)
this_path = "/" + os.path.dirname(curpath)


def replace_num(file, initial, new_num):
    newline = ""
    str_num = str(new_num)
    with open(file, "r") as f:
        for line in f.readlines():
            if line.find(initial) == 0:
                line = (str_num+'\n')
            newline += line
    with open(file, "w") as f:
        f.writelines(newline)


for x in range(1, 4):
    if os.system("sudo apt-get update") == 0:
        break

os.system("sudo apt-get purge -y wolfram-engine libreoffice*")
os.system("sudo apt-get -y clean")
os.system("sudo apt-get -y autoremove")

# for x in range(1, 4):
#     if os.system("sudo pip3 install -U pip") == 0:
#         break

for x in range(1, 4):
    if os.system("sudo apt-get install -y python-dev python3-pip libfreetype6-dev libjpeg-dev build-essential") == 0:
        break

for x in range(1, 4):
    if os.system("sudo -H pip3 install --upgrade luma.oled") == 0:
        break

for x in range(1, 4):
    if os.system("sudo apt-get install -y i2c-tools") == 0:
        break

for x in range(1, 4):
    if os.system("sudo pip3 install adafruit-pca9685 rpi_ws281x") == 0:
        break

for x in range(1, 4):
    if os.system("sudo apt-get install -y python3-smbus") == 0:
        break

for x in range(1, 4):
    if os.system("sudo pip3 install mpu6050-raspberrypi") == 0:
        break

for x in range(1, 4):
    if os.system("sudo pip3 install flask flask_cors websockets numpy") == 0:
        break

for x in range(1, 4):
    if os.system("sudo pip3 install opencv-contrib-python==3.4.3.18") == 0:
        break

for x in range(1, 4):
    if os.system("sudo apt-get -y install libqtgui4 libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqt4-test") == 0:
        break

for x in range(1, 4):
    if os.system("sudo pip3 install imutils zmq pybase64 psutil") == 0:
        break

for x in range(1, 4):
    if os.system("sudo git clone https://github.com/oblique/create_ap") == 0:
        break

try:
    os.system(f"cd {this_path}/create_ap && sudo make install")
except:
    pass

try:
    os.system("cd //home/pi/create_ap && sudo make install")
except:
    pass

for x in range(1, 4):
    if os.system("sudo apt-get install -y util-linux procps hostapd iproute2 iw haveged dnsmasq") == 0:
        break

try:
    os.system('sudo touch //home/pi/startup.sh')
    with open("//home/pi/startup.sh",'w') as file_to_write:
        file_to_write.write(f"#!/bin/sh\nsudo python3 {this_path}/server/webServer.py")
except:
    pass

try:
    replace_num("/boot/config.txt", '#dtparam=i2c_arm=on', 'dtparam=i2c_arm=on\nstart_x=1\n')
except:
    print('try again')

os.system('sudo chmod 777 //home/pi/startup.sh')

replace_num('/etc/rc.local', 'fi', 'fi\n//home/pi/startup.sh start')

# fix conflict with onboard Raspberry Pi audio
try:
    os.system('sudo touch /etc/modprobe.d/snd-blacklist.conf')
    with open("/etc/modprobe.d/snd-blacklist.conf", 'w') as file_to_write:
        file_to_write.write("blacklist snd_bcm2835")
except:
    pass

print(
    'The program in Raspberry Pi has been installed.\n\n'
    'After turning on again, the Raspberry Pi will automatically run the '
    'program to set the servos port signal to turn the servos to the middle '
    'position, which is convenient for mechanical assembly.'
)

print('Restarting...')
os.system("sudo reboot")
