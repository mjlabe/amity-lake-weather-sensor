import os
import time

file1 = open("/boot/config.txt", "a")  # append mode
file1.write("\ndtoverlay=w1-gpio\n")
file1.close()

for i in range(10, -1, -1):
    load = ['|', '/', u'\u2014', '\\', '|', '/', u'\u2014', '\\', ]
    load.reverse()
    j = i // 2
    prog = '-' * j
    print(f'\rRestarting in: {j}s {load[i % 8]} |{prog}|', end='\r')
    time.sleep(0.5)
print(f'\rRestarting now', end='\r')

os.system('sudo reboot')
