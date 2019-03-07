import spidev
import time
import os
import pygame
import numpy
import RPi.GPIO as GPIO
from time import sleep
pygame.init()
startTime = time.clock()
times =[]
states = []
A = [[times], [states]]

firstSound = pygame.mixer.Sound('/home/pi/laserharp-sounds/samples/ambi_dark.wav')
secondSound = pygame.mixer.Sound('/home/pi/laserharp-sounds/samples/ambi_choir.wav')

led = 8
laser1 = 40
GPIO.setwarning(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, inital=GPIO.LOW)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

delay = .05
try:
    while True:
        for x in times:
            if(state[x] == "sound 1"):
                firstSound.play()
            elif(state[x] == "sound 2"):
                secondSound.play():
            else:
                print("no sound")
except KeyboardInterrupt:
    print("keyboard interrupt, gpio cleanup")
    A = [[times], [states]]
    print(A[0])
    print(A[1])

    # print(times)
    # print(states)
    GPIO.output(laser1, GPIO.LOW)
    GPIO.cleanup()
