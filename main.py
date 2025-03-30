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

        with open('InfoJson.json', 'r', encoding="utf8") as file:
            data = json.load(file)

            song_title = request.form.get('songTitle')

            lyrics = data.get(song_title)

            print(song_title)
            print(lyrics)
            
            if lyrics is not None:

                answer = analyst(lyrics)

                answerjson = json.loads(answer)

                print(answerjson)

                return answerjson
            
            else:
                return {"Error": f"Title '{song_title}' not found in the JSON data."}
        

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )