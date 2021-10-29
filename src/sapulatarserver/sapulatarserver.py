import os.path
from datetime import datetime

from flask import (
    Blueprint, jsonify, request, current_app, send_file
)
from werkzeug.utils import secure_filename
from sapulatarserver.rembg import remove_background
from sapulatarserver.form import SapulatarFrom

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
        current_time = datetime.now()
        timestamp = current_time.strftime("%Y%m%d%H%M%S")
        folder_name = current_time.strftime("%Y%m%d")

        # Get Data
        form = SapulatarFrom()
        if not form.validate():
            return jsonify({
                'status': 'error',
                'message': form.errors
            }), 400

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
        filename = timestamp + "_" + filename
        # create a new folder for each request with unix time for the name
        if not os.path.exists(os.path.join(current_app.config['UPLOAD_FOLDER'], folder_name)):
            os.mkdir(os.path.join(current_app.config['UPLOAD_FOLDER'], folder_name), 666)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], folder_name)
        file.save(os.path.join(filepath, filename))

        # process remove background
        output_filename = remove_background(filename, filepath)

        # return the url of result image
        return jsonify({
            'status': 'success',
            'message': 'Image uploaded',
            'filename': output_filename,
            'url': request.host_url + os.path.join("result", folder_name, output_filename)
        }), 200

    # if request method is not POST
    return jsonify({
        'status': 'error',
        'message': 'Bad method'
    }), 405


@sapulatarserver_bp.route('/result/<image_folder>/<image_filename>', methods=['GET'])
def get_image(image_folder, image_filename):
    """
    Serve image from the url
    @type image_path: str
    @param image_path: The location of image
    """
    file_fullpath = os.path.join(current_app.config['UPLOAD_FOLDER'], image_folder, image_filename)

    # check if file path exists in uploads directory
    if not os.path.exists(file_fullpath):
        return jsonify({
            'status': 'error',
            'message': f'File {image_filename}, doesn\'t exists.'
        }), 404

    # check if the file is PNG Image (security purpose)
    if not image_filename.endswith(".png"):
        return jsonify({
            'status': 'error',
            'message': f'File {image_filename}, is not PNG file'
        }), 500

    # return the image
    return send_file(file_fullpath, mimetype='image/png', as_attachment=True, attachment_filename=image_filename)


@sapulatarserver_bp.route('/ping', methods=['GET'])
def ping():
    """
    Healthcheck endpoint
    """
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
