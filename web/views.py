from flask import request, send_from_directory
import os
from . import app
import utils


@app.route('/')
def index():
    return 'Hello!'


@app.route('/files', methods=['POST'])
def files_post():
    if ('file' not in request.files):
        return {'response': 'empty request attach the file'}, 400

    file = request.files['file']
    if utils.allowed_file(file.filename):
        utils.save_file(file)
    else:
        return {'response': 'not acceptable file name'}, 406


@app.route('/files', methods=['GET'])
def files_get():
    path = app.config['UPLOAD_FOLDER']
    files_list = os.listdir(path)
    files = {}
    if (not files_list):
        return {'response': 'upload folder is empty'}, 200
    else:
        for file in files_list:
            files |= ({file: str(os.stat(path + file).st_size) + ' bytes'})
    return files, 200


@app.route("/files/<string:name>", methods=['GET'])
def download_file(name):
    files_list = os.listdir(app.config['UPLOAD_FOLDER'])
    if (name not in files_list):
        return {'response': f'{name} - file not exists'}, 404
    else:
        return send_from_directory(
            app.config['UPLOAD_FOLDER'], name, as_attachment=False), 200


@app.route("/files/<string:name>", methods=['DELETE'])
def delete_file(name):
    if (not os.path.exists(app.config['UPLOAD_FOLDER']+name)):
        return {'response': f'{name} - file not exists'}, 404
    else:
        os.remove(app.config['UPLOAD_FOLDER']+name)
        return {'response': f'{name} - file deleted'}, 200
