import webbrowser
from nlp.text_to_speech import speakAloud
def search(text):
    speakAloud(f"Sure, Searching {text} in google")
    webbrowser.open(f'https://www.google.com/search?q={text}')

    # //*[@id="Ac2FZtLiLOPPxc8Pn-azoAU__155"]/div/div/span/span
    # 
