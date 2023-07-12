import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

MASTER="Shubham"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    #init function is for converting the hour from string to integer 
    hour = int(datetime.datetime.now().hour)
   
    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)
    elif hour>=12 and hour <18:
        speak("Good Afternoon" + MASTER)
    else:
        speak("Good Evening"+ MASTER)
wishMe()
speak("I am your assistant. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
         print("Recognizing..." + r.recognize(audio))
         query = r.recognize_google(audio, language ='en-in')
         print(f"user said:{query}\n")
# python -m speech_recognition
    except Exception as e:
         print("Say that again please")
         query = None

    return query


query = takeCommand()

if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query, sentences =2)
        print(results)
        speak(results)

elif 'open google' in query.lower():
    url = "google.com"
    chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe %s'
    webbrowser.get(using='google-chrome').open(url, new=2)

elif 'open youtube' in query.lower():
    url = "youtube.com"
    chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe %s'
    webbrowser.get(using='google-chrome').open(url, new=2)

elif 'open spotify' in query.lower():
    url = "spotify.com"
    chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe %s'
    webbrowser.get(using='google-chrome').open(url, new=2)

elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("C://")

elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
