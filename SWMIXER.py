#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 12:39:52 2019

@author: 39387
"""

import spidev
import time
import os
import pygame
import wave
import RPi.GPIO as GPIO
from multiprocessing import Process
from pydub import AudioSegment
from threading import Thread
import swmixer


swmixer.init(samplerate=44100, chunksize=1024, stereo=False)
swmixer.start()


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


# turn on lasers
GPIO.output(laser1, GPIO.HIGH)
GPIO.output(laser2, GPIO.HIGH)
GPIO.output(laser3, GPIO.HIGH)
GPIO.output(laser4, GPIO.HIGH)
GPIO.output(laser5, GPIO.HIGH)
GPIO.output(laser6, GPIO.HIGH)




#py_audio=pyaudio.PyAudio()


startTime = time.clock()

#global comp = pygame.mixer.music.load('/home/pi/laserharp-sounds/off.wav')

def playLaser1(timer1 = []):
	if(lightlevell > 800):
            a = swmixer.Sound('/home/pi/laserharp-sounds/1.wav')
            swmixer.play(-1)
            print ("1")
        #time = time.clock()-startTime
        #timer.append(time)
        #global comp
        #comp = comp +

def playLaser2(timer2 = []):
	if(lightlevel2 > 800):
            b = swmixer.Sound('/home/pi/laserharp-sounds/2.wav')
            swmixer.play(-1)
            print ("2")
        #time = time.clock()-startTime
        #timer2.append(time)

def playLaser3(timer3 = []):
	if(lightlevel3 > 800):
            c = swmixer.Sound('/home/pi/laserharp-sounds/3.wav')
            swmixer.play(-1)
            print ("3")
        #time = time.clock()-startTime
        #timer3.append(time)

def playLaser4(timer4 = []):
	if(lightlevel4 > 800):
            d = swmixer.Sound('/home/pi/laserharp-sounds/4.wav')
            swmixer.play(-1)
            print("4")
        #time = time.clock()-startTime
        #timer4.append(time)

def playLaser5(timer5 = []):
	if(lightlevel5 > 800):
            e = swmixer.Sound('/home/pi/laserharp-sounds/5.wav')
            swmixer.play(-1)
            print("5")
        #time = time.clock()-startTime
        #timer5.append(time)

def playLaser6(timer6 = []):
	if(lightlevel6 > 800):
            f = swmixer.Sound('/home/pi/laserharp-sounds/6.wav')
            swmixer.play(-1)
            print("6")
	#time = time.clock()-startTime
        #timer6.append(time)

#def concat(timer1,timer2,timer3,timer4,timer5,timer6, ):
try:
    while True:
        lightlevell = ReadChannel(light_channel)
        lightlevel2 = ReadChannel(light_channel2)
        lightlevel3 = ReadChannel(light_channel3)
        lightlevel4 = ReadChannel(light_channel4)
        lightlevel5 = ReadChannel(light_channel5)
        lightlevel6 = ReadChannel(light_channel6)
        threads = []
        if __name__=='__main__':
            #print(lightlevell)
        	threads.append(Thread(target = playLaser1))
        	threads.append(Thread(target = playLaser2))
        	threads.append(Thread(target = playLaser3))
        	threads.append(Thread(target = playLaser4))
        	threads.append(Thread(target = playLaser5))
        	threads.append(Thread(target = playLaser6))

        for thread in threads:
        	thread.start()

        for thread in threads:
        	thread.join()
	
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


# processes = []
# if __name__=='__main__':
# 	processes.append(Process(target = playLaser1))
# 	processes.append(Process(target = playLaser2))
# 	processes.append(Process(target = playLaser3))
# 	processes.append(Process(target = playLaser4))
# 	processes.append(Process(target = playLaser5))
# 	processes.append(Process(target = playLaser6))
#
# for process in processes:
# 	process.start()
#
# for process in processes:
# 	process.join()


##GPIO.output(laser1, GPIO.LOW)
##GPIO.output(laser2, GPIO.LOW)
##GPIO.output(laser3, GPIO.LOW)
##GPIO.output(laser4, GPIO.LOW)
##GPIO.output(laser5, GPIO.LOW)
##GPIO.output(laser6, GPIO.LOW)
##
##GPIO.cleanup()