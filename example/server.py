#!/usr/bin/env python3

from os import path as osp

from flask import Flask, request
from werkzeug.utils import secure_filename

from sapulatar import queue
from config import *

app = Flask( __name__ )

@app.route('/', methods = ['GET'])
def index():
    return 'Hello world'

@app.route('/unggah-gambar', methods = ['POST'])
def unggah_gambar():
    # TODO save file
    f = request.files['gambar']
    f.save( secure_filename(f.filename) )
    # TODO call rembg server to process uploaded file
    # TODO return rembg server output to client
    return 'successfully uploaded'

@app.route('/ping', methods = ['GET'])
def ping():
    return 'pong'

if __name__ == '__main__':
    app.run(HOST, PORT, DEBUG)
