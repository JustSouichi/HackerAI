import subprocess
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/launch-analyzer', methods=['POST'])
def launch_analyzer():
    try:
        # Esegui lo script di monitoraggio schermo
        print("Launching screen analyzer script...")
        subprocess.Popen(['python', 'screen_analyzer.py'])
        return jsonify({"message": "Screen analyzer launched successfully!"})
    except Exception as e:
        print("Error launching screen analyzer:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
