
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from transformers import pipeline
import json

app = Flask(__name__)
api = Api(app)
CORS(app)

# Carregar o pipeline de análise de sentimentos
sentiment_analysis = pipeline('sentiment-analysis')

# Classe para Análise de Sentimentos
class SentimentAnalysis(Resource):
    def post(self):
        data = request.get_json()
        text = data['text']
        result = sentiment_analysis(text)
        return jsonify(result)

# Classe para Meditações
class Meditations(Resource):
    def get(self):
        with open('meditations.json') as f:
            meditations = json.load(f)
        return jsonify(meditations)

# Classe para Chatbot (simulação de respostas)
class Chatbot(Resource):
    def post(self):
        data = request.get_json()
        text = data['text'].lower()
        if "oi" in text or "olá" in text:
            response = "Olá! Como posso ajudar você hoje?"
        elif "tudo bem" in text or "como você está" in text:
            response = "Estou bem, obrigado! E você?"
        else:
            response = "Desculpe, não entendi. Pode reformular?"
        return jsonify({"response": response})

# Adicionar recursos à API
api.add_resource(SentimentAnalysis, '/analyze')
api.add_resource(Meditations, '/meditations')
api.add_resource(Chatbot, '/chatbot')

@app.route('/')
def home():
    return "API de Saúde Mental com IA"

if __name__ == '__main__':
    app.run(debug=True)
