import RPi.GPIO as GPIO
import subprocess
import time
from bottle import route, run, request, template, static_file
import os
from os import walk

recordButton = 37  # number?
offButton = 00 # number?

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(recordButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(offButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

state = 0

while True:
    if(state == 0):
        if(GPIO.input(recordButton) == GPIO.HIGH):
            # start recording
            # subprocess.run("parecord", "--channels=1", "-d", "STREAM_NAME", "recording.wav")  # insert pulse audio command
            p = subprocess.Popen("parecord --channels=1 -d alsa_output.platform-soc_audio.analog-stereo.monitor recording.wav", stdout=subprocess.PIPE, shell=True)
            state = 1
            time.sleep(.5)

    if(state == 1):
        if(GPIO.input(recordButton) == GPIO.HIGH):
            # stop recording
            # terminate process
            p.terminate()

            @route('/upload/<filename>', method='POST')
            def upload(recording):
                print(request.POST)
                file = request.files[filename]
                name, ext = os.path.splitext(filename)
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

    if(GPIO.input(offButton) == GPIO.HIGH):
        p1 = subprocess.Popen("sudo halt", stdout=subprocess.P)
