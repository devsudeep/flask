from flask import request, render_template, Flask

app = Flask(__name__)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'GET':
        return render_template('upload.html')

    if request.method == 'POST':
        f = request.files['the_file']
        print()
        f.save('uploads/sample.sql')
        return 'file uploaded successfully'
