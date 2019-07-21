# Python Ball Releasing System Program
# For the prototype we made, this system is manual, we replaced the stepper motor
# with a LED to indicate the exact time to release the ball from the storage system


import RPi.GPIO as GPIO          
from time import sleep

# We use the blue LED to indicate the need of a ball release
LED_Ball = 19

def init ():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_Ball,GPIO.OUT)
    GPIO.setup(LED_Ball,GPIO.LOW)
    
def ball_release(demande):
    init()

    if demande == 1:
        GPIO.output(LED_Ball,GPIO.HIGH)    
        print("Ball demanded")
        
    else:
        print ("No ball demand !")
        
