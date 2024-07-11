from AppOpener import open, close
from nlp.text_to_speech import speakAloud
def open_app(*args):
    for apps in args:
        speakAloud(f"Opening {apps}")
        open(apps, match_closest=True)

def close_app(*args):
    for apps in args:
        speakAloud(f"Closing {apps}")
        close(apps, match_closest=True)