from .chrome import driver
from nlp.text_to_speech import speakAloud
from nlp.speech_to_text import speechToText
def wikipedia():
    speakAloud("What do you want in wikipedia?")
    text=speechToText()
    driver.get(url=f"https://en.wikipedia.org/wiki/{text}")
    b=driver.find_elements(by='xpath', value='//*[@id="mw-content-text"]/div[1]/p')
    for c in b:
        print(c, c.text)
        speakAloud(c.text)
    # input("Press enter to exit")
    driver.quit()