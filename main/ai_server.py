from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Carica il modello NLP (es. sentiment analysis come base)
model = pipeline("text-classification", model="facebook/bart-large-mnli")

@app.route("/analyze", methods=["POST"])
def analyze_email():
    data = request.json
    email_content = data.get("content", "")
    
    if not email_content:
        return jsonify({"error": "No email content provided"}), 400

    # Esegui analisi sul contenuto
    result = model(email_content)

    # Restituisci risultato
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
