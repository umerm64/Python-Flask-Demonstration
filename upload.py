from flask import Flask, render_template, request
# from werkzeug import secure_filename

app = Flask(__name__)

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        # f.save(secure_filename(f.filename)) secure_filename is not found in werkzeug so continuing without it
        return 'file upload successfully'

if __name__ == '__main__':
    app.run(debug=True)
