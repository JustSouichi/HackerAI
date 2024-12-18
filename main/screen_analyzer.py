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
    "click here", "claim your prize", "gift card", "winner", "verify",
    "urgent", "reset password", "free trial", "limited time offer", "discount"
]

def show_alert(title, message, details):
    """Mostra un alert con tutte le segnalazioni."""
    root = Tk()
    root.withdraw()
    full_message = (
        f"{message}\n\n"
        f"--- SUSPICIOUS DETECTIONS ---\n{details}"
    )
    messagebox.showwarning(title, full_message)
    root.update()
    root.destroy()

def find_suspicious_phrases(text):
    """Trova frasi sospette nel testo."""
    suspicious_phrases = []
    for line in text.splitlines():
        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword.lower() in line.lower():
                reason = f"Keyword '{keyword}' detected."
                suspicious_phrases.append(f"'{line.strip()}' → {reason}")
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

            if "phishing" in response.text.lower():
                suspicious_links.append(f"'{link}' → Reported as suspicious online.")
        except Exception as e:
            print(f"Error checking link {link}: {e}")
    return suspicious_links

def analyze_with_model(text):
    """Analizza il testo con il modello AI con una soglia moderata."""
    MAX_LENGTH = 1024
    truncated_text = text[:MAX_LENGTH]
    try:
        result = model(truncated_text)
        label = result[0]['label']
        score = result[0]['score']

        if label.lower() in ["neutral", "negative"] and score >= 0.6:
            return f"AI Analysis → '{label}' detected with confidence {score:.2f}."
    except Exception as e:
        print(f"Error analyzing text with model: {e}")
    return None

def capture_and_analyze():
    """Cattura lo schermo, analizza il testo e controlla i link."""
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        text = pytesseract.image_to_string(img)

        if text.strip():
            print("Extracted Text:", text)

            # Trova frasi sospette
            suspicious_phrases = find_suspicious_phrases(text)

            # Controlla i link
            links = extract_links(text)
            suspicious_links = check_links_online(links)

            # Analisi con il modello AI
            ai_analysis = analyze_with_model(text)
            if ai_analysis:
                suspicious_phrases.append(ai_analysis)

            # Combina i risultati
            results = suspicious_phrases + suspicious_links

            # Mostra un alert se ci sono risultati sospetti
            if results:
                print("Suspicious content found!")
                show_alert(
                    "⚠️ Spam Alert",
                    "This is probably spam. Do not click anything!",
                    "\n".join(results)
                )

if __name__ == "__main__":
    print("Starting Screen Analyzer...")
    while True:
        capture_and_analyze()
        time.sleep(5)  # Controlla ogni 5 secondi
