## This code is used to initalise the camera to be used on a raspberry pi
## This code was written on the raspberry pi terminal

sudo pip3 install matplotlib scipy numpy ##allows camera output to be plotted in python

## enables i2c communication
sudo apt-get install -y python-smbus
sudo apt-get install -y i2c-tools

sudo nano /boot/config.txt ## check i2c communication

sudo reboot ##reboot Pi

sudo i2cdetect -y 1 ## check  pi registers the thermal camera

sudo pip3 install RPI.GPI adafruit-blinka
sudo pip3 install adafruit-circuitpython-mlx90640
