import pyttsx3 as p

engine = p.init()

def speakAloud(word):
    engine.say(word)
    engine.runAndWait()