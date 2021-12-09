import os
from flask import Flask, request, jsonify, send_from_directory
from storage import Storage
from werkzeug.utils import secure_filename

app = Flask(__name__)
s = Storage()

@app.route('/', methods=['GET'])
def index():
    return {'Hello': 'Bro!'}

@app.route('/files/', methods=['GET', 'POST'])
def storage_manager():
    if request.method == 'GET':
        return jsonify(s.getFiles())

    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_PATH'], secure_filename(file.filename)))
        return jsonify(True)

    return jsonify(False)

@app.route('/files/<name>/', methods=['GET', 'DELETE'])
def storage_interaction(name):
    if request.method == 'GET':
        return send_from_directory(app.config['UPLOAD_PATH'], name)
    
    if request.method == 'DELETE':
        return jsonify(s.deleteFile(name))

    return jsonify(False)

if __name__ == '__main__':
    app.run()
