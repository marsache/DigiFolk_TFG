import sys
import os

folder_path = os.path.join(os.path.dirname(__file__), 'digifolk-api')
sys.path.append(folder_path)

from flask import Flask, render_template, request, redirect, url_for
import textComp 
import LevenshteinDistances
import hermetricsMed
import SemanticTextSimilarity
import TopicModelingGensim2
from model import segmenter
import json

app = Flask(__name__)
@app.route('/api/textos/', methods=["GET", "POST"])
def getInformationAndProcess():

    if request.method == 'GET':
        return 'Esto es la api de Digifolk! Por favor, elige la opción y manda la información correcta'
    if request.method == 'POST':
        contentJson = request.json
        titulo1 = str(contentJson[0]["Obra"])
        titulo2 = str(contentJson[1]["Obra"])
        response = {}
        response["1-comparacion"] = titulo1 + "-" + titulo2
        response["TextSimilarity"] = textComp.calcular_similitud(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["levenshteinCustom"] = LevenshteinDistances.levenshteinDistanceDP(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["levenshteinHermetrics"] = hermetricsMed.hermetricsLevenstein(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["comparativaHermetrics"] = hermetricsMed.hermetricsComp(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        response["SemanticTextSimilarity"] = SemanticTextSimilarity.predictionComparision(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        #response["SimilarityCheck"] = SimilarityCheckMed.similarityChecker(contentJson[0]['Letra concatenada'], contentJson[1]['Letra concatenada'])
        #response["JensenShanon2"] = TopicModelingGensim2.calcularGensim(contentJson, contentJson[0]['Letra concatenada'])
        return response    

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
            
            if lyrics is not None:

                answer = segmenter(lyrics, model_name)

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