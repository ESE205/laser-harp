import RPi.GPIO as GPIO
import subprocess

button = 37  # number?

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 0

while True:
    if(state == 0):
        if(GPIO.input(button) == GPIO.HIGH):
            # start recording
            # subprocess.run("parecord", "--channels=1", "-d", "STREAM_NAME", "recording.wav")  # insert pulse audio command
            p = subprocess.Popen("parecord --channels=1 -d STREAM_NAME filename.wav", stdout=subprocess.PIPE, shell=True)
            state = 1

    if(state == 1):
        if(GPIO.input(button) == GPIO.HIGH):
            # stop recording
            # terminate process

            p.terminate()

            # upload recording.wav
            state = 0
