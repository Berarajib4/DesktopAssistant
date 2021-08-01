import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    time = int(datetime.datetime.now().hour)
    if 0 <= time <= 6:
        speak("It's late night sir. It's bad for your health. Please go to sleep sir..")
    elif 6 <= time <= 12:
        speak("Good Morning Sir!")
    elif 12 <= time <= 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")

    speak("I'm Jarvis developed by Silent knight. Please tell me, how can i help you..")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening......')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except:
        # print(e)
        print("I can't recognized it sir.say again please..")
        speak("sorry sir. I'm not able to do that for you..")
        return "None"

    return query


if __name__ == '__main__':
    wishMe()

    keep_going = True
    while keep_going:
        query = takeCommand().lower()
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            # print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")

        elif 'open github' in query:
            webbrowser.open("www.github.com")

        elif 'open facebook' in query:
            webbrowser.open("www.facebook.com")

        elif 'open instagram' in query:
            webbrowser.open("www.instagram.com")

        elif 'open twitter' in query:
            webbrowser.open("www.twitter.com")
        
        elif 'play music' in query:
            music_dir = 'D:\\Mp3_Songs\\ENGLISH'
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
           Time = datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"It's {Time} sir")

        elif 'quit' in query:
            speak("okay bye sir. have a nice day")
            keep_going = False

    

