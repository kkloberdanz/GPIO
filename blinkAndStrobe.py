import RPi.GPIO as GPIO
import time
import random

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

def strobe(p, num_strobes=100):
    for dc in range(0, num_strobes, 1):
        p.ChangeDutyCycle(dc)
        time.sleep(0.001)
    time.sleep(0.1)
    for dc in range(num_strobes, 0, -1):
        p.ChangeDutyCycle(dc)
        time.sleep(0.002)
    p.ChangeDutyCycle(0)

pin1 = 12
pin2 = 10
pin3 = 8

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(pin1, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.setup(pin3, GPIO.OUT)

p1 = GPIO.PWM(pin1, 50)
p1.start(0)

p2 = GPIO.PWM(pin2, 50)
p2.start(0) 

p3 = GPIO.PWM(pin3, 50)
p3.start(0) 

pins_list = [p1, p2, p3]
num_pins  = len(pins_list)
cleaned_up = False

try:
    for loops in range(50):
        for i in range(100):
            #blink(pin)
            '''
            strobe(p1)
            strobe(p2)
            strobe(p3)
            strobe(p2)
            '''
            strobe(pins_list[random.randint(0,num_pins - 1)], i)

        for i in range(100, 0, -1):
            strobe(pins_list[random.randint(0,num_pins - 1)], i)

except KeyboardInterrupt: 
    print("\nCleaning up ...")
    GPIO.cleanup()
    cleaned_up = True

if not cleaned_up:
    GPIO.cleanup()

print("DONE")
