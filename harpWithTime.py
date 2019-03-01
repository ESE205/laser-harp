#!/usr/bin/python

import spidev
import time
import os
import pygame
import numpy
import RPi.GPIO as GPIO
from time import sleep
pygame.init()
startTime = time.clock()

times = []
states = []

firstSound = pygame.mixer.Sound('/home/pi/laserharp-sounds/samples/ambi_dark.wav')
secondSound = pygame.mixer.Sound('/home/pi/laserharp-sounds/samples/ambi_choir.wav')

led = 8
laser1 = 40
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser1, GPIO.OUT, initial=GPIO.LOW)

# Open SPI bus
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

# Function to read SPI data from MCP3008 chip
# Channel must be an integer 0-7
def ReadChannel(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

# Function to convert data to voltage level,
# rounded to specified number of decimal places.
def ConvertVolts(data,places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

# Function to calculate temperature from
# TMP36 data, rounded to specified
# number of decimal places.
def ConvertTemp(data, places):
    # ADC Value
    # (approx)  Temp  Volts
    #    0      -50    0.00
    #   78      -25    0.25
    #  155        0    0.50
    #  233       25    0.75
    #  310       50    1.00
    #  465      100    1.50
    #  775      200    2.50
    # 1023      280    3.30
    temp = ((data * 330)/float(1023))-50
    temp = round(temp, places)
    return temp

# Define sensor channels
light_channel = 0
light_channel2 = 1

# Define delay between readings
delay = .05
try:
    while True:
        GPIO.output(laser1, GPIO.HIGH)
        # Read the light sensor data
        light_level = ReadChannel(light_channel)
        light_volts = ConvertVolts(light_level, 2)
        light_level2 = ReadChannel(light_channel2)
        light_volts2 = ConvertVolts(light_level2, 2)
        if (light_level >300) or (light_level <120):
            GPIO.output(led, GPIO.HIGH)
            firstSound.play()
            #print('playing first sound')
            #print(time.clock()-startTime)
            times.append(time.clock()-startTime)
            states.append("sound 1")
        elif (light_level2 > 300) or (light_level2 < 95):
            GPIO.output(led, GPIO.HIGH)
            secondSound.play()
            #print('playing second sound')
            times.append(time.clock()-startTime)
            states.append("sound 2")
        else:
            GPIO.output(led, GPIO.LOW)
            times.append(time.clock()-startTime)
            states.append("no sound")

            # Read the temperature sensor data
            ##  temp_level = ReadChannel(temp_channel)
            ##  temp_volts = ConvertVolts(temp_level,2)
            ##  temp       = ConvertTemp(temp_level,2)

            # Print out results
            print("--------------------------------------------")
            print("Light: {} ({}V)".format(light_level, light_volts))
            print("Light2 : {} ({}V)".format(light_level2, light_volts2))

            # Wait before repeating loop
            time.sleep(delay)
except KeyboardInterrupt:
    print("keyboard interrupt, gpio cleanup")
    A = [[times], [states]]
    print(A[0])
    print(A[1])

    # print(times)
    # print(states)
    GPIO.output(laser1, GPIO.LOW)
    GPIO.cleanup()
