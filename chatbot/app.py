from flask import Flask, render_template, request, jsonify


from transformers import *
import torch
import ligia


modelos = ['mrm8488/distill-bert-base-spanish-wwm-cased-finetuned-spa-squad2-es']

nlp = pipeline(
            'question-answering', 
            model=modelos[0]
        )
        


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    subject = request.form["subject"]
    print(subject)
    input = msg
    return ([get_Chat_response(input), subject])


def get_Chat_response(text):

    return ligia.consulta(question = text, nlp = nlp)


if __name__ == '__main__':
    app.run()
