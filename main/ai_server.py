from flask import Flask, request, jsonify
from transformers import pipeline
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Abilita CORS per permettere richieste da React

# Carica il modello NLP di Hugging Face
print("Loading AI Model...")
model = pipeline("text-classification", model="facebook/bart-large-mnli")  # Modello generico per il text classification

# Lista di parole chiave sospette (controllo manuale)
SUSPICIOUS_KEYWORDS = [
    'claim your prize', 'click here', 'gift card', 'winner', 
    'verification', 'forfeited', 'urgent', 'reward', 'lifetime opportunity',
    'credit card', 'password', 'reset', 'lottery', 'selected as the winner'
]

def keyword_check(email_content):
    """
    Controlla se l'email contiene parole chiave sospette.
    Restituisce True se trova parole sospette, altrimenti False.
    """
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in email_content.lower():
            return True
    return False

@app.route("/analyze", methods=["POST"])
def analyze_email():
    """
    Endpoint principale per analizzare il contenuto delle email.
    """
    data = request.json
    email_content = data.get("content", "")

    # Verifica se il contenuto è vuoto
    if not email_content.strip():
        return jsonify({"error": "No email content provided"}), 400

    # Filtro manuale per parole chiave sospette
    if keyword_check(email_content):
        return jsonify({
            "result": [{
                "label": "Suspicious",
                "score": 0.99
            }],
            "source": "Keyword Filter"
        })

    try:
        # Analisi con il modello AI
        print("Analyzing email content with AI...")
        result = model(email_content)
        print("AI Result:", result)

        return jsonify({
            "result": result,
            "source": "AI Model"
        })

    except Exception as e:
        print("Error during AI analysis:", e)
        return jsonify({"error": "AI analysis failed", "details": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
