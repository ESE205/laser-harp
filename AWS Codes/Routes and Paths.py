from bottle import route, run, request, template, static_file
import os
from os import walk

@route('/upload/<filename>', method='POST')
def upload(filename):
    print(request.POST)
    file = request.files[filename]
    name, ext = os.path.splitext(filename)
    if ext not in ('.wav'):
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
    for (dirpath, dirnames, filenames) in walk('./experiment'):
        files.extend(filenames)
    return template('home', files=files)

if __name__ == '__main__':
    run(host='localhost', port=3000, debug = True)