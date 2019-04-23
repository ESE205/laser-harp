import RPi.GPIO as GPIO
import subprocess
import time
from bottle import route, run, request, template, static_file
import os
from os import walk
from gpiozero import Button

# recordButton = 7  # number?
# offButton = 11  # number?

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(recordButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(offButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
recordButton = Button(4)
offButton = Button(17)

state = 0

while True:
    # recordState = GPIO.input(recordButton)
    # offState = GPIO.input(offButton)
    if(offButton.is_pressed):
        print("off button")
        p1 = subprocess.Popen("sudo halt", stdout=subprocess.PIPE, shell = True)
    if(state == 0):
        if(recordButton.is_pressed):
            # start recording
            # subprocess.run("parecord", "--channels=1", "-d", "STREAM_NAME", "recording.wav")  # insert pulse audio command
            print("start recording")
            p = subprocess.Popen("parecord --channels=1 -d alsa_output.platform-soc_audio.analog-stereo.monitor recording.wav", stdout=subprocess.PIPE, shell=True)
            state = 1
            time.sleep(.5)

    if(state == 1):
        if(recordButton.is_pressed):
            # stop recording
            # terminate process
            print("stop recording")
            p.terminate()

            @route('/upload/<recording>', method='POST')
            def upload(recording):
                print(request.POST)
                file = request.files[recording]
                name, ext = os.path.splitext(recording)
                if ext not in('.wav'):
                    return "File extension not allowed."

                save_path = "./experiment"

                file_path = "{path}/{file}".format(path=save_path, file=filename)
                file.save(file_path)
                return "File successfully saved to '{0}'.".format(save_path)

            @route('/<filename>')
            def download(filename):
                return static_file(filename, root='./experiment')

            @route('/')
            def index():
                files = []
                for(dirpath, dirnames, filenames) in walk('./experiment'):
                    files.extend(filenames)
                return template('home', files=files)

            if __name__ == '__main__':
                run(host='localhost', port=3000, debug=True)
            # upload recording.wav
            state = 0
            time.sleep(.5)
