
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
api = Api(app)
CORS(app)

sentiment_analysis = pipeline('sentiment-analysis')

class SentimentAnalysis(Resource):
    def post(self):
        data = request.get_json()
        text = data['text']
        result = sentiment_analysis(text)
        return jsonify(result)

api.add_resource(SentimentAnalysis, '/analyze')

@app.route('/')
def home():
    return "API de Saúde Mental com IA"

if __name__ == '__main__':
    app.run(debug=True)
