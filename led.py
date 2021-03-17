#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep
def autode():
    GPIO.output(15,True)
    sleep(3)
    GPIO.output(15,False)
    sleep(0.5)
    GPIO.output(15,True)
    sleep(0.5)
    GPIO.output(15,False)
    sleep(0.5)
    GPIO.output(15,True)
    sleep(0.5)
    GPIO.output(15,False)
    sleep(0.5)
    GPIO.output(12,True)
    sleep(1)
    GPIO.output(12,False)
    sleep(0.5)
    GPIO.output(11,True)
    
def autod2():
    GPIO.output(11,True)
    sleep(0.5)
    GPIO.output(11,False)
    sleep(0.5)
    GPIO.output(12,True)
    sleep(0.5)
    GPIO.output(12,False)
    sleep(0.5)
    GPIO.output(15,True)
    sleep(2)
    
    
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT) # punane auto
GPIO.setup(12,GPIO.OUT) # kollane auto
GPIO.setup(15,GPIO.OUT) # roheline auto
GPIO.setup(31,GPIO.OUT) # punane jalakäija
GPIO.setup(29,GPIO.OUT) # roheline jalakäija
GPIO.setup(36,GPIO.OUT) # kollane nupp
GPIO.setup(40,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


while True:
    GPIO.output(15,True)
    GPIO.output(31,True)
    if GPIO.input(40) == GPIO.HIGH:
        GPIO.output(36, True)
        autode()
        GPIO.output(11,True)
        GPIO.output(31,True)
        sleep(0.5)
        GPIO.output(31,False)
        sleep(1)
        GPIO.output(36,False)
        sleep(0.000001)
        GPIO.output(29,True)
        sleep(3)
        GPIO.output(29,False)
        sleep(0.5)
        GPIO.output(29,True)
        sleep(0.5)
        GPIO.output(29,False)
        sleep(0.5)
        GPIO.output(31,True)
        GPIO.output(11,False)
        autod2()
        continue


GPIO.cleanup()
exit()
