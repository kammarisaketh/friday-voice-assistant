# 🎙️ FRIDAY – Real-Time AI Voice Assistant

FRIDAY is a full-stack, real-time AI voice assistant built with a **FastAPI backend** and a **browser-based UI** using the Web Speech API. It supports **speech recognition (STT)**, **text-to-speech (TTS)**, **intent-based command handling**, and **browser automation**, enabling natural interaction directly from the browser.

---

## 🚀 Features

- 🎤 **Speech-to-Text (STT)** using the browser’s Web Speech API  
- 🔊 **Text-to-Speech (TTS)** responses from backend → browser  
- ⚡ **WebSocket-based real-time communication**  
- 🧠 **Intent-based command system** (Info, Web Search, Job Search, System Actions)  
- 🌍 **Browser automation** (open Google, YouTube, custom URLs)  
- 🖥️ **Clean UI** with mic button, logs, and dynamic response display  
- 🧩 Modular architecture: `core`, `intents`, `config`, `api_server`  
- 💡 Easily extendable to new commands & features  

---

## 🏗️ Project Structure

friday-voice-assistant/
│
├── friday/
│ ├── core/
│ │ ├── assistant.py
│ │ ├── voice.py
│ │ └── init.py
│ │
│ ├── intents/
│ │ ├── info_intents.py
│ │ ├── jobsearch_intents.py
│ │ ├── web_intents.py
│ │ └── init.py
│ │
│ ├── api_server.py
│ ├── config.py
│ └── init.py
│
├── ui/
│ ├── index.html
│ ├── script.js
│ └── style.css
│
├── main.py
├── api_server.py
├── requirements.txt
└── README.md

---

## 🧠 How It Works

### **1️⃣ Frontend (Browser)**  
- Uses **Web Speech API** to listen and convert voice → text  
- Sends text to backend via **WebSockets**  
- Plays voice responses with **TTS**  
- Displays logs + system messages  

### **2️⃣ Backend (FastAPI)**  
- Receives user command  
- Routes through **intent system**  
- Executes logic (time, info, job search, open website, etc.)  
- Sends structured JSON response back to frontend  

Example response:

```json
{
  "type": "speak",
  "msg": "The time is 10:30 PM"
}
⚙️ Run the Project Locally
1️⃣ Clone the repository
git clone https://github.com/kammarisaketh/friday-voice-assistant
cd friday-voice-assistant

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start the backend server
python main.py

4️⃣ Open the frontend

Open this file in your browser:

ui/index.html

🧩 Technologies Used
Backend
Python
FastAPI
WebSockets
Modular Intent System

Frontend
HTML
CSS
JavaScript
Web Speech API (STT/TTS)


📌 Example Commands
Command	Action
"What is the time"	Speaks the current time
"Open Google"	Opens a new Google tab
"Search for jobs"	Runs job search intent
"Tell me about X"	Info intent
"Play YouTube"	Opens YouTube
🔮 Future Improvements

AI/NLP integration (ChatGPT / LLaMA)

Wake-word activation (“Hey FRIDAY”)

Desktop automation

User profiles

Activity logs dashboard


👨‍💻 Author
Saketh Kammari
Full-Stack & Backend Developer
MS Computer Science – AUM
GitHub: https://github.com/kammarisaketh
