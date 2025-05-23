# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN pip install ollama

RUN ollama create segmenter_llama2 -f ./segmenter_model/ModelfileLlama2
RUN ollama create segmenter_gemma3 -f ./segmenter_model/ModelfileGemma3
RUN ollama create segmenter_deepseekr1 -f ./segmenter_model/ModelfileDeepSeekR1

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]