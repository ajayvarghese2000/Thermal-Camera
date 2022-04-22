<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/VwT4NrJ.png" width=650></a>
	<p align="center"> This repository is part of  a collection for the 21WSD001 Team Project. 
	All other repositories can be access below using the buttons</p>
</p>

<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/CCC-ProjectDocs"><img src="https://i.imgur.com/rBaZyub.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Dashboard"><img src="https://i.imgur.com/fz7rgd9.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Cloud-Server"><img src="https://i.imgur.com/bsimXcV.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Drone-Firmware"><img src="https://i.imgur.com/yKFokIL.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Simulated-Drone"><img src="https://i.imgur.com/WMOZbrf.png" alt="drawing" height = 33/></a>
</p>

<p align="center">
	Below you can find buttons that link you to the repositories that host the code for the module itself. These can also be found linked in the collection repository: <a href="https://github.com/lboroWMEME-TeamProject/Drone-Firmware">Drone Firmware</a>. 
</p>


<p align="center">
	<a href="https://github.com/lboroWMEME-TeamProject/Main-Pi"><img src="https://i.imgur.com/4knNDhv.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/EnviroSensor"><img src="https://i.imgur.com/lcYUZBw.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Geiger-Counter"><img src="https://i.imgur.com/ecniGik.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/Thermal-Camera"><img src="https://i.imgur.com/kuoiBTc.png" alt="drawing" height = 33/></a> 
	<a href="https://github.com/lboroWMEME-TeamProject/ai-cam"><img src="https://i.imgur.com/30bEKvR.png" alt="drawing" height = 33/></a>
</p>

------------

# Thermal-Camera

This repository contains code to initialise the thermal camera and have it output frames to the Main Pi.

------------

## Table of Contents

- [Subsystem Overview](#Subsystem-Overview)
    - [Wiring Diagram](Wiring-Diagram)
- [Code Overview](#Code-Overview)
- [Test Plan](#Test-Plan)
- [Installation](#Installation)
- [Deployment](#Deployment)

------------

## Subsystem Overview

The thermal camera is directly connected to the Main Pi system, as it already uses I2C communication and the data is in a ready to use format there is not need to add a micro processor in front of it.     

**Subsystem Diagram :**

<p align="center">
	<img src="https://i.imgur.com/azpRjR6.jpg" alt="High Level Diagram"/>
</p>



### Wiring Diagram
<p align="center">
	<img src="https://i.imgur.com/fRkNJH9.jpg" alt="drawing"/>
</p>

------------

## Code Overview

The MLX90640 is a complete package that can output the temperature at each pixel of the sensor. However, to convert this to an image a gradient map must be applied to the data and plotted to effectively get an image. This raw image is then put through a Bilinear interpolation algorithm to smooth out the rough square pixels into something that reflects the actual image. After that it is converted from an array of values to an image and sent off.

### Flowchart


<p align="center">
	<img src="https://i.imgur.com/Dyt0v2a.png" width="250px"alt="drawing"/>
</p>


------------

## Test Plan

<div align="center">

|Objective|Testing Strategy|Expected Output|Current Output|Pass/Fail|
|--|--|--|--|:--:|
|Functionality of thermal camera|Connect camera to raspberry Pi. Upload test code written in chosen software to the Pi. Test code displays temperatures read by the camera|Temperature should be displayed|Temperature is displayed as expected|:heavy_check_mark:|
|Display Image data|Connect camera to raspberry Pi. Upload code written in chosen software to the Pi. Point camera at different objects of different temperatures|Thermal image of object should be displayed for each object|Testing to be implemented|N/A|

</div>

------------

## Installation

*How to download and setup the code on the Pi Pico/Pi*

------------

## Deployment

*How to get it running and outputting data*

------------
