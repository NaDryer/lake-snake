from gpiozero import *
from time import sleep

NetInput = 0
buttonleft = Button(13)
buttonright = Button(19)
servo = Servo(24)
def ButtonLeftPress():
    print("ButtonLeft")
    servo.mid()
    servo.value=1

def ButtonRightPress():
    print("ButtonRight")
    servo.value=0
while True:
    buttonleft.when_pressed = ButtonLeftPress
    buttonright.when_pressed = ButtonRightPress




