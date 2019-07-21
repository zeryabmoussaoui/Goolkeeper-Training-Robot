# Python Pittching Program
# direction_1 & pwm_1 for the control of direction and speed of the right motor (front view)
# direction_2 & pwm_2 for the control of direction and speed of the left motor (front view)

import RPi.GPIO as GPIO          
from time import sleep


def init():
    
# direction_1 = 22
# direction_2 = 4
# pwm_1 = 17
# pwm_2 = 27

    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)

    p = GPIO.PWM(17, 50)
    p2 = GPIO.PWM(27, 50)

# Set motor rotation direction (fixed)
GPIO.output(4, GPIO.HIGH)
GPIO.output(22, GPIO.HIGH)

def pitch(vitesse,te,angle):
    
    if angle==45:
        print("Pitching with an angle of 45")
        if vitesse == 'l':
            p.ChangeDutyCycle(50)
            p2.ChangeDutyCycle(30)
           
            print("with a low speed ")
            time.sleep(15)

        elif vitesse=='m':
            p.ChangeDutyCycle(70)
            p2.ChangeDutyCycle(50)
            
            print("with a medium speed ")
            time.sleep(15)

        elif vitesse=='h':
            p.ChangeDutyCycle(90)
            p2.ChangeDutyCycle(70)
            
            print("with a high speed ")
            time.sleep(15)

########################################################################
    if angle==90:
        print("Pitching with an angle of 45")
        if vitesse == 'l':
            p.ChangeDutyCycle(30)
            p2.ChangeDutyCycle(30)
            
            print("with a low speed ")
            time.sleep(15)

        elif vitesse=='m':
            p.ChangeDutyCycle(60)
            p2.ChangeDutyCycle(60)
            
            print("with a medium speed ")
            time.sleep(15)

        elif vitesse=='h':
            p.ChangeDutyCycle(80)
            p2.ChangeDutyCycle(80)
            
            print("with a high speed ")
            time.sleep(15)
            
#########################################################################
    if angle==135:
        print("Pitching with an angle of 45")
        if vitesse == 'l':
            p.ChangeDutyCycle(30)
            p2.ChangeDutyCycle(50)
            
            print("with a low speed ")
            time.sleep(15)

        elif vitesse=='m':
            p.ChangeDutyCycle(50)
            p2.ChangeDutyCycle(70)
            
            print("with a medium speed ")
            time.sleep(15)

        elif vitesse=='h':
            p.ChangeDutyCycle(70)
            p2.ChangeDutyCycle(90)
            
            print("with a high speed ")
            time.sleep(15)
            
    elif angle==100:
        GPIO.cleanup()
        print("Pittching done!")
        
    
    
   
