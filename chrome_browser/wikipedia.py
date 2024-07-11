from nlp.text_to_speech import speakAloud
def wikipedia(text):
    print(text)
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service as ChromeService
    from webdriver_manager.chrome import ChromeDriverManager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print("Driver imported ")
    # speakAloud("What do you want in wikipedia?")
    # text=speechToText()
    driver.get(url=f"https://en.wikipedia.org/wiki/{text}")
    b=driver.find_elements(by='xpath', value='//*[@id="mw-content-text"]/div[1]/p')
    print("Found b", b)
    for c in b:
        print(c, c.text)
        speakAloud(c.text)
    # input("Press enter to exit")
    driver.quit()