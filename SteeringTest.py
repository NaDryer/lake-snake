from smbus import SMBus
import time
#import RPi.GPIO as GPIO
bus = SMBus(1)

def ANALOG_READ(Adc):
    bus.write_byte(0x48, 0x40+Adc)
    return bus.read_byte(0x48)

while True:
    val_x = ANALOG_READ(1
                        )
    print(val_x)
    time.sleep(0.05)
    

