# Nova-AI-Voice-Assistant

# AI Powered Voice Assistant (Nova 🤖)
Nova is a Python-based voice assistant that can perform tasks like opening websites, playing music, fetching news, and remembering user preferences.

## 🚀 Features
*  Voice Recognition (SpeechRecognition)
*  Utilizes the speech_recognition library to listen for and recognize voice commands. 
*  Text-to-Speech (gTTS + pygame)
*  Activates upon detecting the wake word "Nova"
*  Converts text to speech using pyttsx3 for local conversion. 
*  Open websites liske Google, YouTube, LinkedIn, Instagram etc based on voice commands.)
*  Play songs from custom music library 
*  Fetch latest news using News API 
*  Memory system (remembers name & likes)
*  Session-based commands (5 commands per activation)
*  🤖 AI Chatbot Integration (NEW 🔥)
  → Handles unknown commands intelligently
  → Gives human-like responses

🎥 Demo Video: https://www.linkedin.com/posts/ankit-singh-233a07336_python-ai-machinelearning-activity-7441889276797272064-t9eC?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFSCyIcBgCrCisFoXWT9qHj4Sixo3TSEbmY
---

## Environment Variables  

Create a file named API.env and add: <br>
NVIDIA_API_KEY=your_api_key_here <br>
NEWS_API_KEY=your_news_api_key

## 🧠 How It Works

* Say "Hello Nova" to activate assistant
* You can give up to 5 commands per session
* Example commands:

  * "Open Google"
  * "Play song kesariya"
  * "Play song tum hi ho"
  * "Tell me my name"
  * "News tech"
  * "News business"
  * "List songs"
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
* NVIDIA Chat API (Mistral Model)
* JSON 🧠 – Store user memory (name, likes)

##  Future Improvements

* GUI (Tkinter or PyQt)
* Spotify API integration 🎵
* Continuous listening mode
* Better NLP (intent detection)

---

## 👨‍💻 Author

Ankit Singh (AIML Student 🚀)

## ⭐ If you like this project

Give it a star ⭐ on GitHub!

