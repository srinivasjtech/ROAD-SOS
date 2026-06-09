import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from groq import Groq

# Reads API key from Render's environment variables (set in Render dashboard)
API_KEY = os.environ.get("GROQ_API_KEY", "gsk_your_key_here")

client = Groq(api_key=API_KEY)
app = Flask(__name__, static_folder=".")
CORS(app)

SYSTEM_PROMPT = """You are RoadSOS Emergency Assistant, a location-based emergency chatbot for Chennai, India.

Your job is to help people involved in road accidents or emergencies get fast, clear help.

Rules you must always follow:
1. ALWAYS start your very first message by telling the user to call 108 immediately if it's a real emergency.
2. Ask the user for three things in your first message:
   - What happened (one short line)
   - Whether it's them or someone else
   - The approximate area or landmark in Chennai
3. Once you have those details, respond with:
   - The nearest trauma centre or hospital for that area in Chennai (with a phone number if you know it)
   - 2-3 simple first-aid steps they can do RIGHT NOW while waiting for help
4. Keep all responses short, calm, and easy to read under stress.
5. Never give complicated medical advice. You are a guide, not a doctor.
6. If the user seems panicked, be extra calm and reassuring.
7. If the situation is unclear, ask only ONE clarifying question at a time.

Chennai emergency reference:
- National Ambulance: 108
- Police: 100
- Fire: 101
- Apollo Hospitals (Greams Road): 044-2829-0200
- MIOT International (Manapakkam): 044-4200-2288
- Fortis Malar Hospital (Adyar): 044-4289-2222
- Government General Hospital (Park Town): 044-2530-5000
- Sri Ramachandra Hospital (Porur): 044-4592-8000
"""

@app.route("/")
def index():
    return send_from_directory(".", "index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    history = data.get("history", [])
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            max_tokens=1024,
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})

    except Exception as e:
        error = str(e)
        if "401" in error or "invalid_api_key" in error:
            return jsonify({"error": "Invalid API key."}), 401
        elif "429" in error:
            return jsonify({"error": "Rate limit hit. Please wait a moment."}), 429
        else:
            return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
