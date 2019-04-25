import RPi.GPIO as GPIO
import subprocess
import time
import requests
from bottle import route, run, request, template, static_file
import os
import signal
from os import walk
from gpiozero import Button
import random

# recordButton = 7  # number?
# offButton = 11  # number?

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(recordButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(offButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
recordButton = Button(4)
offButton = Button(17)

state = 0
rand = random.randint(1, 102947298469128649161972364837164)  # random number
counter = rand
# str(counter)
while True:
    # recordState = GPIO.input(recordButton)
    # offState = GPIO.input(offButton)
    if(offButton.is_pressed):
        print("off button")
        p1 = subprocess.Popen("sudo halt", stdout=subprocess.PIPE, shell=True)
    if(state == 0):
        if(recordButton.is_pressed):
            # start recording
            # subprocess.run("parecord", "--channels=1", "-d", "STREAM_NAME", "recording.wav")  # insert pulse audio command
            print("start recording")
            p = subprocess.Popen("parecord --channels=1 -d alsa_output.platform-soc_audio.analog-stereo.monitor " + str(rand) + ".wav", shell=True) # , stdout=subprocess.PIPE
            state = 1
            time.sleep(.5)

    if(state == 1):
        if(recordButton.is_pressed):
            # stop recording
            # terminate process
            print("stop recording")
            # if(os.path.getsize('/home/pi/'+str(counter))!=44):
            #     with open(str(counter)+'.wav', 'rb') as f:
            #         requests.post('http://3.211.80.203:3000/upload/' + str(counter) + '.wav', files={str(counter)+'.wav': f})
            with open(str(rand)+'.wav', 'rb') as f:
                requests.post('http://3.211.80.203:3000/upload/' + str(rand) + '.wav', files={str(rand)+'.wav': f})
            # p.send_signal(signal.SIGINT)
            p2 = subprocess.Popen("sudo reboot", stdout=subprocess.PIPE, shell =True)

            state = 0
            time.sleep(.5)
    # if(state == 2):
    #     # with open('recording.wav', 'rb') as f:
    #     #     requests.post('http://3.211.80.203:3000/upload/recording.wav', files={'recording.wav': f})
    #     state = 0
