import speech_recognition as sr
r=sr.Recognizer()
WIT_AI_KEY = "USWFVMIH62OO2XZXWU3VFUXW2TDFXXOV"
def speechToText(): 
    with sr.Microphone() as source:
        print("Please wait. Calibrating microphone...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say someting")
        audio = r.listen(source)
    try:
        txt=r.recognize_wit(audio, key=WIT_AI_KEY)
        return txt
    except sr.UnknownValueError:
        print("I could not understand what you said")
    except sr.RequestError as e:
        print("Could not request results")
    return 0
