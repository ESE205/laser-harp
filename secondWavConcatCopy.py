import spidev
import time
import os
import pygame
import numpy
import RPi.GPIO as GPIO
import wave
import contextlib
from time import sleep
from pydub import AudioSegment
from pydub.playback import play
pygame.init()
pygame.mixer.init()

led = 8
laser1 = 29
laser2 = 31
laser3 = 32
laser4 = 33
laser5 = 35
laser6 = 36
count1 = 0

sound2 = AudioSegment.from_wav('/home/pi/laserharp-sounds/samples/harpSound1.wav')
combined_sounds = sound2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser2, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser3, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser4, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser5, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(laser6, GPIO.OUT, initial=GPIO.LOW)

#create sounds
# s = pygame.mixer.music.load('/home/pi/laserharp-sounds/sample/harpSound1Complete.wav')

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
def ConvertVolts(data, places):
    volts = (data * 3.3) / float(1023)
    volts = round(volts, places)
    return volts

# Define sensor channels
light_channel = 0
light_channel2 = 1
light_channel3 = 2
light_channel4 = 3
light_channel5 = 4
light_channel6 = 5

# Define delay between readings
state = 0;
lastState = 0;
delay = .05
state2Time = 0

#turn on lasers
GPIO.output(laser1, GPIO.HIGH)
GPIO.output(laser2, GPIO.HIGH)
GPIO.output(laser3, GPIO.HIGH)
GPIO.output(laser4, GPIO.HIGH)
GPIO.output(laser5, GPIO.HIGH)
GPIO.output(laser6, GPIO.HIGH)


# initialLight1 = ReadChannel(light_channel)
# initialLight2 = ReadChannel(light_channel2)
# initialLight3 = ReadChannel(light_channel3)
# initialLight4 = ReadChannel(light_channel4)
# initialLight5 = ReadChannel(light_channel5)
# initialLight6 = ReadChannel(light_channel6)

startTime = time.clock()
try:
    while True:
        #read light sensors
        light_level = ReadChannel(light_channel)
        light_level2 = ReadChannel(light_channel2)
        light_level3 = ReadChannel(light_channel3)
        light_level4 = ReadChannel(light_channel4)
        light_level5 = ReadChannel(light_channel5)
        light_level6 = ReadChannel(light_channel6)

        if(light_level > 300) or(light_level < 120): #state 1
            #play sound 1
            pygame.mixer.music.stop()
        elif (light_level2 > 300) or (light_level2 <95): #state 2
            #play sound 2
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/samples/testFile.wav')
            pygame.mixer.music.play(-1)
            state2Time = time.clock()-startTime


        else: #state 0
            pygame.mixer.music.stop()
            if(state2Time != 0):
                print(state2Time)
                state2Time = 0
            else:
                startTime  = time.clock()
                time.sleep(.05)
            #no sound
except KeyboardInterrupt:
    print("keyboard interrupt")
    combined_sounds.export("/home/pi/laserharp-sounds/samples/combined_sounds1.wav", format="wav")
    #turn off lasers
    GPIO.output(laser1, GPIO.LOW)
    GPIO.output(laser2, GPIO.LOW)
    GPIO.output(laser3, GPIO.LOW)
    GPIO.output(laser4, GPIO.LOW)
    GPIO.output(laser5, GPIO.LOW)
    GPIO.output(laser6, GPIO.LOW)

    GPIO.cleanup()
