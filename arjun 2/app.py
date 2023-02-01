from flask import Flask, request, render_template, redirect, url_for
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'


def unique_filename(filename):
    i = 0
    new_filename = filename
    while os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], new_filename)):
        i += 1
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}{i}{ext}"
    return new_filename


@app.route('/')
def index():
    files = os.listdir("uploads")
    return render_template("upload.html", files=files)


@app.route('/', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filename = "myjpeg.jpeg"
        filename = unique_filename(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('index', message="File uploaded successfully"))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
