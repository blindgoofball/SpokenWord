from queue import Queue
from threading import Thread
import pyttsx3

messages=Queue()

def runSpeech():
    engine=pyttsx3.init()
    while (msg := messages.get()):
        engine.say(msg)
        engine.runAndWait()

def start():
    Thread(target=runSpeech, daemon=True).start()