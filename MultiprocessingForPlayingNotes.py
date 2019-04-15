Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> import spidev
import time
import os
import pygame
import wave
import pyaudio
import RPi.GPIO as GPIO
from multiprocessing import Process

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


# turn on lasers
GPIO.output(laser1, GPIO.HIGH)
GPIO.output(laser2, GPIO.HIGH)
GPIO.output(laser3, GPIO.HIGH)
GPIO.output(laser4, GPIO.HIGH)
GPIO.output(laser5, GPIO.HIGH)
GPIO.output(laser6, GPIO.HIGH)


lightLevell = ReadChannel(light_channel)
lightLevel2 = ReadChannel(light_channel2)
lightLevel3 = ReadChannel(light_channel3)
lightLevel4 = ReadChannel(light_channel4)
lightLevel5 = ReadChannel(light_channel5)
lightLevel6 = ReadChannel(light_channel6)

py_audio=pyaudio.PyAudio()


startTime = time.clock()

#global comp = pygame.mixer.music.load('/home/pi/laserharp-sounds/off.wav')


def playLaser1(timer1 = []):
	if(light_level1 > 800):
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/1.wav')
            pygame.mixer.music.play(-1)
        #time = time.clock()-startTime
        #timer.append(time)
        #global comp
        #comp = comp + 

def playLaser2(timer2 = []):
	if(light_level2 > 800): 
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/2.wav')
            pygame.mixer.music.play(-1)
        #time = time.clock()-startTime
        #timer2.append(time)
            
def playLaser3(timer3 = []):
	if(light_level3 > 800): 
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/3.wav')
            pygame.mixer.music.play(-1)
        #time = time.clock()-startTime
        #timer3.append(time)
            
def playLaser4(timer4 = []):
	if(light_level4 > 800):
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/4.wav')
            pygame.mixer.music.play(-1)
        #time = time.clock()-startTime
        #timer4.append(time)
            
def playLaser5(timer5 = []):
	if(light_level5 > 800): 
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/5.wav')
            pygame.mixer.music.play(-1)
        #time = time.clock()-startTime
        #timer5.append(time)
            
def playLaser6(timer6 = []):
	if(light_level6 > 800): 
            s = pygame.mixer.music.load('/home/pi/laserharp-sounds/6.wav')
            pygame.mixer.music.play(-1)
	#time = time.clock()-startTime
        #timer6.append(time)

#def concat(timer1,timer2,timer3,timer4,timer5,timer6, ):
	

processes = []

for i in range(os.cpu_count()):
	print('registreing process %d' % i)
	processes.append(Process(target = playLaser1))
	processes.append(Process(target = playLaser2))
	processes.append(Process(target = playLaser3))
	processes.append(Process(target = playLaser4))
	processes.append(Process(target = playLaser5))
	processes.append(Process(target = playLaser6))
			 
for process in processes:
	process.start()

for process in processes:
	process.join()

	
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
