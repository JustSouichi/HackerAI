import time
import pytesseract
import re
import requests
from PIL import Image
from mss import mss
from transformers import pipeline
from tkinter import messagebox, Tk

# Configura Tesseract su macOS
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# Modello AI
print("Loading AI Model...")
model = pipeline("text-classification", model="facebook/bart-large-mnli")

# Parole chiave sospette
SUSPICIOUS_KEYWORDS = [
    "click here", "claim your prize", "gift card", "winner", "verify", "urgent",
    "reset password", "free trial", "promotion", "limited time offer", "discount"
]

def show_alert(title, message, details):
    """Mostra un singolo alert con tutte le segnalazioni combinate."""
    root = Tk()
    root.withdraw()
    full_message = (
        f"{message}\n\n"
        f"--- DETAILS ---\n{details}"
    )
    messagebox.showwarning(title, full_message)
    root.update()
    root.destroy()

def find_suspicious_phrases(text):
    """Trova frasi sospette nel testo."""
    suspicious_phrases = []
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword.lower() in text.lower():
            reason = f"Keyword '{keyword}' detected in the text."
            suspicious_phrases.append(reason)
    return suspicious_phrases

def extract_links(text):
    """Estrae i link dal testo usando regex."""
    return re.findall(r'https?://\S+', text)

def check_links_online(links):
    """Controlla i link online per vedere se sono segnalati."""
    suspicious_links = []
    for link in links:
        try:
            print(f"Checking link: {link}")
            query = f"https://www.google.com/search?q={link}+phishing+report"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(query, headers=headers, timeout=5)

            if "phishing" in response.text.lower() or "report" in response.text.lower():
                suspicious_links.append(f"'{link}' → Reported as suspicious online.")
        except Exception as e:
            print(f"Error checking link {link}: {e}")
    return suspicious_links

def analyze_context_with_ai(text):
    """Analizza il contesto del testo con il modello AI."""
    try:
        result = model(text[:1024])  # Analizza solo i primi 1024 caratteri
        label = result[0]['label']
        score = result[0]['score']

        if label.lower() in ["neutral", "negative"] and score >= 0.5:
            return f"AI Analysis → '{label}' detected with confidence {score:.2f}."
    except Exception as e:
        print(f"Error analyzing text with AI: {e}")
    return None

def capture_and_analyze():
    """Cattura lo schermo, analizza il testo e poi analizza i link solo se il testo è sospetto."""
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        text = pytesseract.image_to_string(img)

        if text.strip():
            print("Extracted Text:\n", text)

            # Analisi del testo
            suspicious_phrases = find_suspicious_phrases(text)
            ai_context_analysis = analyze_context_with_ai(text)

            # Se il testo è sospetto
            if suspicious_phrases or ai_context_analysis:
                print("Text is suspicious. Proceeding to analyze links...")
                links = extract_links(text)
                suspicious_links = check_links_online(links)
            else:
                suspicious_links = []

            # Combina i risultati
            results = suspicious_phrases + suspicious_links
            if ai_context_analysis:
                results.append(ai_context_analysis)

            # Mostra un alert se ci sono segnalazioni
            if results:
                print("Suspicious content detected!")
                show_alert(
                    "⚠️ Spam Alert",
                    "Potential spam detected. Review the details below:",
                    "\n".join(results)
                )

if __name__ == "__main__":
    print("Starting Screen Analyzer...")
    while True:
        capture_and_analyze()
        time.sleep(5)  # Controllo ogni 5 secondi
