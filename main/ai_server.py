from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS  # Importa CORS

app = Flask(__name__)
CORS(app)  # Abilita CORS per tutte le route

# Carica il modello NLP
model = pipeline("text-classification", model="facebook/bart-large-mnli")

@app.route("/analyze", methods=["POST"])
def analyze_email():
    data = request.json
    email_content = data.get("content", "")

    if not email_content:
        return jsonify({"error": "No email content provided"}), 400

    # Esegui l'analisi
    result = model(email_content)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
