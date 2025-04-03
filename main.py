from flask import Flask, render_template, request, jsonify
from model import segmenter
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/segmenter_method', methods=['POST'])
def segmenter_method():
    if request.method == 'POST':
        print(request.form)

        with open('InfoJson.json', 'r', encoding="utf8") as file:
            data = json.load(file)

            song_title = request.form.get('songTitle')
            model_name = request.form.get('modelName')

            lyrics = data.get(song_title)

            print(song_title)
            print(lyrics)
            
            if lyrics is not None:

                answer = segmenter(lyrics, model_name)
                print(answer)

                # answerjson = json.loads(answer)

                # print(answerjson)

                answerjson = {"Error": "Model returned invalid format."}

                try:
                    answerjson = json.loads(answer)
                    print(answerjson)
                except json.JSONDecodeError as e:
                    print("Model returned invalid format.")

                return answerjson
            
            else:
                return {"Error": f"Title '{song_title}' not found in the JSON data."}
        

if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5001,
        debug=True
    )