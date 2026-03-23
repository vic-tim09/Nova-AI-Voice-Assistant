# Nova-AI-Voice-Assistant
A Python-based AI voice assistant using SpeechRecognition, gTTS, and News API for automation tasks.


# 🤖 Nova AI Voice Assistant
Nova is a Python-based voice assistant that can perform tasks like opening websites, playing music, fetching news, and remembering user preferences.

---

## 🚀 Features

* 🎙️ Voice Recognition (SpeechRecognition)
* 🔊 Text-to-Speech (gTTS + pygame)
* 🌐 Open websites (Google, YouTube, LinkedIn, etc.)
* 🎵 Play songs from custom music library 
* 📰 Fetch latest news using News API 
* 🧠 Memory system (remembers name & likes)
* ⚡ Session-based commands (5 commands per activation)

---

## 📁 Project Structure

```
├── main.py
├── musicLibrary.py
├── memory.json
├── requirements.txt
├── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/vic-tim09/Nova-AI-Voice-Assistant.git
cd nova-assistant
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create `.env` file and add:

```
NEWS_API_KEY=your_api_key_here
```

## ▶️ Run the Project

```bash
python main.py
```

## 🧠 How It Works

* Say "Nova" to activate assistant
* You can give up to 5 commands per session
* Example commands:

  * "Open Google"
  * "Play song kesariya"
  * "Play song tum hi ho"
  * "Tell me my name"
  * "News tech"
  * "News business"
  * "List songs"
  * 
---

## ⚠️ Notes

* Make sure microphone is working
* Internet is required for speech recognition & news
* API key must be valid {add your API}💫

---
## 🛠️ Technologies Used

* Python 🐍 – Core programming language
* SpeechRecognition 🎙️ – For voice input
* gTTS (Google Text-to-Speech)🔊 – Convert text to voice
* Pygame 🎧 – Play audio output
* Requests 🌐 – Fetch news data from API
* News API 📰 – Get real-time news
* Webbrowser 🌍 – Open websites
* Python-dotenv 🔐 – Manage environment variables
* JSON 🧠 – Store user memory (name, likes)

## 💡 Future Improvements

* ChatGPT integration 🤖
* GUI (Tkinter or PyQt)
* Spotify API integration 🎵
* Continuous listening mode
* Better NLP (intent detection)

---

## 👨‍💻 Author

Ankit Singh (AIML Student 🚀)

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

