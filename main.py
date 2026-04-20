# 1️⃣ IMPORTS 
import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" 
import pygame
import time
import re

from chatbot import chat_with_ai
from memory import set_memory, get_memory
from dotenv import load_dotenv

# 2️⃣ GLOBAL SETUP
load_dotenv("API.env")
newsapi = os.getenv("NEWS_API_KEY")

recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
recognizer.pause_threshold = 0.8
nova_active = True
session_active = False

# 3️⃣ SPEAK FUNCTION
engine = pyttsx3.init() 
pygame.mixer.init()

def clean_text(text):
    # remove emojis
    # text = re.sub(r'[^\x00-\x7F]+', '', text)

    # remove special symbols
    text = re.sub(r'[\*\#\@\$\%\^\&\(\)\[\]\{\}]', '', text)

    return text

def speak(text):
    text = clean_text(text)   # 🔥 yaha clean kiya
    print(text)
    tts = gTTS(text)       # Convert text to speech audio
    tts.save('temp.mp3')   # Save generated audio as mp3 file

    pygame.mixer.music.load('temp.mp3')   # Load audio file into mixer
    pygame.mixer.music.play()             # Start playing the audio

    while pygame.mixer.music.get_busy():  # Wait until audio finishes playing
        pygame.time.Clock().tick(10)      # Control loop speed while waiting

    pygame.mixer.music.unload() # Remove audio from memory
    os.remove("temp.mp3")       # Delete temporary audio file

def processCommand(command):
    command = command.lower().strip()

    # 📂 Web Commands
    if "open google" in command:
        open_google()

    elif "open youtube" in command:
        open_youtube()

    # 🎵 Music Commands
    elif command.startswith("play song"):
        play_song(command)

    # 🎗️Linkein Command 
    elif "open linkedin" in command:
        open_linkedin()

    # Facebook Command
    elif "open facebook" in command:
        open_facebook()

    #Instagram Command
    elif "open instagram" in command:
        open_insta()

    # 📰 News Commands
    elif "news" in command:
        get_news(command)

    # 🧠 Memory Commands
    elif "my name is" in command:
        set_name(command)

    elif "tell me my name" in command:
        get_name()

    elif "what do i like" in command or "what i like" in command:
        get_likes()

    elif "i like" in command and "what i like" not in command:
        set_likes(command)

    # ❌ Exit
    elif "exit" in command or "stop nova" in command:
        speak("Okay Goodbye!")
        return "exit"
    
    elif "thank" in command:
        speak("Welcome! I always there for you")

    # List of songs🎶🎶
    elif "list songs" in command:
        songs = ", ".join(musicLibrary.music.keys())
        speak(f"Available songs are {songs}")

    # fallback
    else:
        # speak("Command not recognized")
        reply = chat_with_ai(command)
        speak(reply)

# function deffinition
def open_google():
    webbrowser.open("https://google.com")

def open_youtube():
    webbrowser.open("https://youtube.com")

def open_linkedin():
    webbrowser.open("https://linkedin.com")

def open_facebook():
    webbrowser.open("https://facebook.com")

def open_insta():
    webbrowser.open("https://www.instagram.com/victim__09")

def play_song(command):
    global nova_active
    parts = command.split(" ")  #["play","song_name"]
    song = " ".join(parts[2:])
    song_data = musicLibrary.music.get(song)

    if song_data:
        speak(f"Playing {song} for 2 minutes")
        nova_active = False   # 🔴 nova pause
        webbrowser.open(song_data["link"])
        time.sleep(120)   # demo pause
        nova_active = True
        speak("Back online 😎")
    else:
        speak("Song not found")

def get_news(command):
    if "tech" in command:
        category = "technology"
    elif "sports" in command:
        category = "sports"
    elif "business" in command:
        category = "business"
    elif "entertainment" in command:
        category = "entertainment"
    else:
        category = "general"
    try:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={newsapi}"
        r = requests.get(url)
        # print("Status Code:", r.status_code)   # 👈 status

        if r.status_code == 200:  #show successful fetching
            data = r.json()

                # Extract the articles
            articles = data.get('articles', [])
            for article in articles[:5]:   # only top 5 news
                speak(article['title'])
    except Exception as e:
        print(e)
        speak("Error fetching news")
    
def set_name(command):
    name = command.replace("my name is","").strip()
    set_memory("name", name)
    speak(f"Okay, I will remember your name is {name}")

def get_name():
    name = get_memory("name")
    if name:
        speak(f"Your name is {name}")
    else:
        speak("I don't know your name yet")

def set_likes(command):
    like = command.replace("i like","").strip()
    set_memory("likes", like)
    speak(f"Okay, I will remember you like {like}")

def get_likes():
    like = get_memory("likes")
    if like:
        speak(f"You like {like}")
    else:
        speak("I don't know what you like yet")


command_count = 0
MAX_COMMANDS = 5  

# 4️⃣ command function
if __name__ == "__main__":
    speak("Novaa active....")
    while nova_active:
        # Listen for the wake word "Hello Nova"
        # obtain audio from the microphone
        r = recognizer
         
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening...")
                audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print("You said:", word)

            wake_words = ["nova","nora","novaa","noah","nua","navo","no","nov","noa","nowa","one"]
            if any(w in word.lower() for w in wake_words):
                speak("Yes")
                session_active = True
                command_count = 0

                 # 🔥 START SESSION LOOP (5 commands)
                while session_active and command_count < MAX_COMMANDS:
                    try:
                        with sr.Microphone() as source:
                            print(f"Listening command (7 sec) {command_count+1}/5...")
                            audio = r.listen(source, timeout=5, phrase_time_limit= 7)
                            command = r.recognize_google(audio)
                            print("Command:", command)

                            result = processCommand(command)
                            command_count += 1
                            if result == "exit":
                                nova_active = False
                                session_active = False
                                break

                    except sr.WaitTimeoutError:
                        speak("No command received")
                        command_count += 1

                    except sr.UnknownValueError:
                        speak("Could not understand")
                        command_count += 1

                    except Exception as e:
                        print(e)
                        command_count += 1
                             
        except sr.UnknownValueError:
            speak("Could not understand audio")
            # kuch mat bol (silent reh)

        except sr.RequestError:
            speak("Internet issue")

        except Exception as e:
            speak(f"Error: {e}")



