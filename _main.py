from nlp.text_to_speech import speakAloud
from nlp.speech_to_text import speechToText
from chrome_browser.google import search
import time
import threading
from wit import Wit
# x=speechToText()
# speakAloud(x)
# while True:
t=threading.Thread(target=speakAloud, args=("Hello, I'm your virtual assistant, how may I help you?",))
t.run()
# speakAloud("Hello, I'm your virtual assistant, how may I help you?")
helpme=speechToText()

if helpme != 0:
    helpme = helpme.lower()
if 'wikipedia' in helpme:
    from chrome_browser.wikipedia import wikipedia
    wikipedia()
else:
    search(helpme)
# speakAloud("")
# search("John the baptist")

# wit
access_token = 'USWFVMIH62OO2XZXWU3VFUXW2TDFXXOV'
client = Wit(access_token)
client.message(helpme)

print("complete")