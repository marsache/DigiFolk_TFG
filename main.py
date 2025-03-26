from flask import Flask, render_template, request, jsonify
from model import analyst
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyst_method', methods=['POST'])
def analyst_method():
    if request.method == 'POST':
        print(request.form)

        answer = analyst("Venid, pastorcitos, venid adorar al Rey de los cielos que_ha nacido ya.")

        answerjson = json.loads(answer)

        print(answerjson)

        return answerjson

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )