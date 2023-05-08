from flask import Flask, render_template, request
import to_file

app = Flask(__name__)

@app.route('/' or '/index.html')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            to_file.write_to_file(data)
            to_file.write_to_csv(data)
        except:
            return "Did not save to database."
    return render_template('thankyou.html')