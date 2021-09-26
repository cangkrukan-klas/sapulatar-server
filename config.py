from os import path as osp


HOST = '0.0.0.0'
PORT = '12345'
DEBUG = True

UPLOAD_DIR = osp.join(osp.dirname( __file__ ), 'uploads')
RESULT_DIR = osp.join(osp.dirname( __file__ ), 'results')
