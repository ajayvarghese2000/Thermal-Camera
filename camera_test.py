import time
import board 
import busio
import adafruit_mlx90640

i2c = busio.I2C(board.SCL, board.SDA, frequency = 800000)  #setup i2c communication
mlx = adafruit_mlx90640.MLX90640(i2c)  ## begin i2c communication on camera
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_2_HZ

frame = [0] * 768 ## array used to store temperatures

while True:
    try:
        mlx.getFrame(frame)
    except ValueError:
        continue
        
for h in range(24):
    for w in range(32):
        t = frame[h * 32 + w]
        print("0.1f, " %t)
