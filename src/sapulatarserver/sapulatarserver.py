import functools
import os.path

from flask import (
    Blueprint, g, redirect, jsonify, request, url_for, current_app, send_file
)
from werkzeug.utils import secure_filename

sapulatarserver_bp = Blueprint('sapulatar', __name__, url_prefix='/')


def allowed_file(filename):
    """Check if the filename match with the allowed extensions.
    return bool if matched
    @type filename: str
    @param filename: The name of file to check
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


@sapulatarserver_bp.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        
        # Check if there is no file uploaded
        if 'file' not in request.files or request.files['file'].filename == '':
            return jsonify({
                'status': 'error',
                'message': 'Upload your file in the file field'
            }), 400

        file = request.files['file']

        # Check if the file is in allowed extensions
        if not allowed_file(file.filename):
            return jsonify({
                'status': 'error',
                'message': f'File type must be in: {current_app.config["ALLOWED_EXTENSIONS"]}'
            }), 400

        filename = secure_filename(file.filename)
        # TODO create a new folder for each request with unix time for the name
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'])
        file.save(filepath + filename)
        return jsonify({
            'status': 'success',
            'message': 'Image uploaded',
            'filename': filename,
            'url': request.base_url + os.path.join(filepath, filename)
        }), 200
    
    # if request method not POST
    return jsonify({
        'status': 'error',
        'message': 'Bad method'
    }), 405


@sapulatarserver_bp.route('/result/<image_path>', methods=['GET'])
def get_image(image_path):
    """ Serve image from the url
    @type image_path: str
    @param image_path: The location of image
    """
    # TODO check if file path exists in uploads directory
    # TODO check if the file is PNG Image (security purpose)
    # TODO return the image
    # return send_file(filename, mimetype='image/png')
    pass


@sapulatarserver_bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
