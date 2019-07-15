from gpiozero import LED
from time import sleep

red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
    red.on()
    sleep(5)
    red.off()
    
    yellow.on()
    sleep(4)
    yellow.off()
    
    green.on()
    sleep(3)
    green.off()
  
    