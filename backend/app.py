import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
# from groq import Groq

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# This is a placeholder for the actual Groq client
# In Stage 1, we are not making real API calls.
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route("/health", methods=["GET"])
def health_check():
    """A simple health check endpoint."""
    return jsonify({"status": "healthy"}), 200

@app.route("/api/convert", methods=["POST"])
def convert_text():
    """
    Handles the text conversion request.
    In Stage 1, this returns a dummy response.
    """
    data = request.get_json()

    if not data or "text" not in data or "target" not in data:
        return jsonify({"error": "Invalid input. 'text' and 'target' are required."}), 400

    original_text = data.get("text")
    target = data.get("target")

    # Dummy response for Stage 1
    dummy_converted_text = f"""'{original_text}'
This is a dummy converted response for the target: '{target}'. 
The real AI conversion will be implemented in a later stage."""

    return jsonify({
        "original_text": original_text,
        "converted_text": dummy_converted_text
    })

if __name__ == "__main__":
    # This block is for local development and won't be used by Vercel
    app.run(debug=True, port=5000)
