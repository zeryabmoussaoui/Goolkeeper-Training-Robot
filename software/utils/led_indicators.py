# LED indicators
# We installed 4 LEDs on the prototype :
# 1. Blue  : ball releasing demand
# 2. Red   : system off
# 3. White : shooting angle required
# 4. Green : new exercise
# The blue one has its own program that we import here "ball_releasing"


import RPi.GPIO as GPIO          
from time import sleep
from ball_releasing_system import init
from file import ball_release

Red=13
White=6
Green=26

def init ():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(Red,GPIO.HIGH)
    GPIO.setup(White,GPIO.OUT)
    GPIO.setup(Green,GPIO.OUT)

    GPIO.setup(Red,GPIO.LOW)
    GPIO.setup(White,GPIO.LOW)
    GPIO.setup(Green,GPIO.LOW)

def LEDs(exercise, angle):
    init()
    if exercice==1:
        GPIO.setup(Red,GPIO.LOW)
        print("System ON")
        GPIO.setup(Green,GPIO.HIGH)
        print("New exercise")
        
    else:
        GPIO.setup(Green,GPIO.LOW)
        print("No exercise")
        GPIO.setup(Red,GPIO.HIGH)
        print("System OFF")
    ball_release(exercice)

    if angle != 0:
        GPIO.setup(White,GPIO.HIGH)
    else:
        GPIO.setup(White,GPIO.LOW)
    print("Shooting angle : "+ angle)
        

