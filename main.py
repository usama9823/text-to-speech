


import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    speech = input("please enter your text to say: ")
    while(True):
        engine.say(speech)
        engine.runAndWait()
        speech = input("please enter quit to quit or enter another text to say: ")
        if(speech=='quit'):
            engine.say('Thankyou for using text to speech')
            engine.runAndWait()
            break