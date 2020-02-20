import glob
import os
import subprocess
from setuptools import setup, find_packages, Extension


def make_rule():
    path = '/etc/udev/rules.d/99-jetbot-rover.rules'
    rule = 'KERNEL=="ttyUSB*", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", MODE="0666", SYMLINK+="ttyUSB_Rover"'

    isRule = False

    if os.path.isfile(path):
        with open(path) as lines:
            for line in lines:
               if line==rule:
                   isRule = True

    if isRule==False:
        f = open(path, 'w')
        f.write(rule)
        f.close()
        subprocess.call(['systemctl', 'restart', 'systemd-udevd'])
        subprocess.call(['usb_modeswitch', '-v', '0x0403', '-p', '0x6015', '--reset-usb'])

def build_libs():
    subprocess.call(['cmake', '.'])
    subprocess.call(['make'])


make_rule()
build_libs()


setup(
    name='jetbot',
    version='0.4.0',
    description='An open-source robot based on NVIDIA Jetson Nano',
    packages=find_packages(),
    install_requires=[
        'Adafruit_MotorHat',
        'Adafruit-SSD1306',
        'pyserial',
    ],
    package_data={'jetbot': ['ssd_tensorrt/*.so']},
)
