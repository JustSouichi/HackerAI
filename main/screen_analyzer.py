import time
import pytesseract
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
SUSPICIOUS_KEYWORDS = ["click here", "claim your prize", "gift card", "winner", "verify", "urgent", "reset password"]

def show_alert(title, message, details):
    """Mostra un alert con le frasi sospette e il motivo."""
    root = Tk()
    root.withdraw()  # Nasconde la finestra principale di tkinter
    full_message = (
        f"{message}\n\n"
        f"--- SUSPICIOUS PHRASES DETECTED ---\n{details}"
    )
    messagebox.showwarning(title, full_message)
    root.update()
    root.destroy()  # Chiude correttamente la finestra

def find_suspicious_phrases(text):
    """Trova frasi sospette e restituisce i motivi."""
    suspicious_phrases = []
    for line in text.splitlines():
        for keyword in SUSPICIOUS_KEYWORDS:
            if keyword.lower() in line.lower():
                reason = f"Keyword '{keyword}' detected."
                suspicious_phrases.append(f"'{line.strip()}' → {reason}")
    return suspicious_phrases

def capture_and_analyze():
    """Cattura lo schermo, analizza il testo e mostra un alert se necessario."""
    with mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        img = Image.frombytes("RGB", (screenshot.width, screenshot.height), screenshot.rgb)
        text = pytesseract.image_to_string(img)

        if text.strip():
            print("Extracted Text:", text)
            suspicious_phrases = find_suspicious_phrases(text)

            if suspicious_phrases:
                print("Suspicious phrases found!")
                show_alert(
                    "⚠️ Spam Alert",
                    "This is probably spam. Do not click anything!",
                    "\n".join(suspicious_phrases)
                )

if __name__ == "__main__":
    print("Starting Screen Analyzer...")
    while True:
        capture_and_analyze()
        time.sleep(5)  # Analizza ogni 5 secondi
