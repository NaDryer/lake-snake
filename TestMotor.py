from gpiozero import *

pin_a = Button(5,pull_up=True)         # Rotary encoder pin A connected to GPIO2
pin_b = Button(4,pull_up=True)         # Rotary encoder pin B connected to GPIO3
boatmotor = PWMOutputDevice(23)
NetThrottleNO = 0

def pin_a_rising():                    # Pin A event handler
    global NetThrottleNO
    if pin_b.is_pressed: NetThrottleNO += -2   # pin A rising while A is active is a clockwise turn
    print(NetThrottleNO)

def pin_b_rising():                    # Pin B event handler
    global NetThrottleNO
    if pin_a.is_pressed: NetThrottleNO += 3   # pin B rising while A is active is a clockwise turn
boatmotor.active_high
boatmotor.on()

pin_a.when_pressed = pin_a_rising      # Register the event handler for pin A
pin_b.when_pressed = pin_b_rising      # Register the event handler for pin B

input("Turn the knob, press Enter to quit.\n")