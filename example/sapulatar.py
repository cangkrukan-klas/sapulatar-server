import sys
from os import path as osp
try:
    from rembg.bg import remove as remove_bg
except ImportError:
    print('rembg module not found!')

def process_files(input_file):
    """ Process uploaded files.
    @param input_file -> str: queued input file location,
    return str of output location
    """
    # TODO for each input_file, do process remove_bg
    # TODO save rembg output into results folder
    # TODO return output location
    pass

def queue(input_files, key):
    """ Queue uploaded files to process.
    @param input_files -> list: array of uploaded files,
    @param key -> str : unique key each request
    return (key, [output locations])
    """
    # TODO validate key
    # TODO process_files(input_files) using queue
    # TODO return tuple of key, [output locations]
    pass
