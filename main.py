from utils import *
from flask import Flask, render_template, request
from flask_cors import cross_origin

app = Flask(__name__)


@app.route('/', methods=['GET'])
@cross_origin()
def search():
    return render_template('index.html')


@app.route('/weather', methods=['GET', 'POST'])
@cross_origin()
def result():
    if request.method == 'POST':
        city = request.form['city-name']
        data = weather(city)

        return render_template('result.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
