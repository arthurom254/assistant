from nlp.text_to_speech import speakAloud
import wit, json
WIT_AI_KEY = "USWFVMIH62OO2XZXWU3VFUXW2TDFXXOV"
def aiEngine(text):
    client = wit.Wit(access_token=WIT_AI_KEY)
    response=client.message(text)
    intents = response.get('intents', [])

    if intents :        
        intent = intents[0]['name']
        if intent == 'google':
            from chrome_browser.google import search
            q = response.get('text', '')
            search(q)
        elif intent == 'wikipedia':
            print("wikipedia one.......................................................")
            from chrome_browser.wikipedia import wikipedia            
            q = response.get('text', '')
            print("wiki.......................................................",q)
            wikipedia(q)
        elif intent == 'open_app':
            from open_app.applications import open_app
            app_name = response['entities']['app_name:app_name'][0]['value']
            open_app(app_name)
        elif intent == 'close_app':
            from open_app.applications import close_app
            app_name = response['entities']['app_name:app_name'][0]['value']
            close_app(app_name)
        elif intent == 'mail_send':
            # mail = response['entities']['app_name:app_name'][0]['value']
            mail='No mail'
            speakAloud(f"Do you want to send an email to {mail}")
    else:
        speakAloud(f"Sorry, I am not able to do that yet")
        
        print("Done.......................................................")