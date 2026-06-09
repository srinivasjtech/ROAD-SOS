# 🚨 RoadSOS — Emergency Response Chatbot

> **If this is a real emergency, call 108 immediately.**

RoadSOS is an AI-powered emergency chatbot that helps people involved in road accidents in Chennai instantly find the nearest trauma centres and receive first-aid guidance — all from a simple web browser.

---

## 🌐 Live Demo
👉 [roadsos.onrender.com](https://roadsos.onrender.com)

---

## ✨ Features
- 🏥 Finds nearest trauma centres in Chennai with direct phone numbers
- 🩹 Gives 2–3 first-aid steps tailored to the incident
- 📞 One-tap quick-dial for 108, 100, and 101
- 💬 Conversational AI powered by LLaMA 3.3 via Groq
- 🌐 Works on any browser — mobile or desktop, no app needed

---

## 🗂️ Project Structure
```
roadsos/
├── server.py          # Flask backend — handles Groq API calls
├── index.html         # Frontend chat UI (HTML + CSS + JS)
├── requirements.txt   # Python dependencies
└── render.yaml        # Render deployment config
```

---

## 🚀 Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/YOUR_USERNAME/roadsos.git
cd roadsos
```

**2. Install dependencies**
```bash
pip install flask flask-cors groq
```

**3. Add your Groq API key**

Get a free key at [console.groq.com](https://console.groq.com) and paste it in `server.py`:
```python
API_KEY = "gsk_your_key_here"
```

**4. Run the server**
```bash
python server.py
```

**5. Open in browser**
```
http://localhost:5000
```

---

## ☁️ Deploy on Render (Free)

1. Fork this repo
2. Go to [render.com](https://render.com) → New → Web Service
3. Connect your GitHub repo
4. Add environment variable:
   - Key: `GROQ_API_KEY`
   - Value: your Groq key
5. Click **Deploy** — your site goes live in ~2 minutes

---

## 🧰 Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML5, CSS3, Vanilla JavaScript |
| Backend | Python 3, Flask, flask-cors |
| AI Model | LLaMA 3.3 70B via Groq API |
| Deployment | Render (free tier) |

---

## 🏥 Chennai Emergency Reference

| Service | Number |
|---|---|
| National Ambulance | 108 |
| Police | 100 |
| Fire | 101 |
| Apollo Hospitals | 044-2829-0200 |
| MIOT International | 044-4200-2288 |
| Fortis Malar (Adyar) | 044-4289-2222 |
| Govt General Hospital | 044-2530-5000 |
| Sri Ramachandra (Porur) | 044-4592-8000 |

---

## 📄 License
Open Source — [Apache 2.0](LICENSE)

---

*Built for Hackathon 2026 · Because every second matters.*
