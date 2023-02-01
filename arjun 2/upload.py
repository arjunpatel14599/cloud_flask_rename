# import the necessary libraries
from flask import Flask, request
import requests

# create the Flask application
app = Flask(__name__)

# define the routes


@app.route('/upload', methods=['POST'])
def upload():
    # get the file from the request
    file = request.files['file']
    # send the file to the third layer
    requests.post('http://third_layer_url/upload', files={'file': file})
    return 'File uploaded successfully'


@app.route('/view')
def view():
    # get the file from the third layer
    response = requests.get('http://third_layer_url/view')
    # return the file as a response
    return response.content, 200, {'Content-Type': 'image/jpeg'}


# run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3030, debug=True)
