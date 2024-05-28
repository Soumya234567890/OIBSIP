import os
import datetime
import random
import wikipedia
import pyttsx3
import sounddevice as sd
from scipy.io.wavfile import write
import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak('Hello Sir, I am Friday, your Artificial intelligence assistant. Please tell me how may I help you')

def takeCommand():
    fs = 44100  # Sample rate
    seconds = 3  # Duration of recording
    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()  # Wait until recording is finished
    write('output.wav', fs, myrecording)  # Save as WAV file

    audio_file = open("output.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    query = transcript.text
    return query

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()
        if 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'play music' in query:
            music_dir = 'path_to_your_music_directory'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        elif 'open Stackoverflow' in query:
            os.startfile("https://stackoverflow.com")
        elif 'search on Wikipedia' in query:
            query = query.replace("search on Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        else:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                max_tokens=1024,
                temperature=0.5,
            )
            speak(response.choices[0].text)