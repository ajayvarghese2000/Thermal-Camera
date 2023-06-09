This file outputs the thermal image from the camera

import time
import board
import busio
import adafruit_mlx90640
import matplotlib.pyplot as plt ##library used to create plot
import numpy as np  ##library used to manipulate data from camera


i2c = busio.I2C(board.SCL, board.SDA, frequency= 800000) #setup i2c communication
mlx = adafruit_mlx90640.MLX90640(i2c) #setup i2c communication on Pi
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_Hz
mlx_shape = (24,32) ## camera width and length

plt.ion ##enable interactive plotting
fig,ax = plt.subplots(figsize(24,32))
cam1 = ax.imshow(np.zeros(mlx_shape))
cbar = fig.colorbar(therm1)

frame = np.zeros((24*32,))
time_array = []
while True:
      current = time.monotonic()
      try:
         mlx.getFrame(frame)
         cam1.set_data(frame)
      except ValueError:
          continue
