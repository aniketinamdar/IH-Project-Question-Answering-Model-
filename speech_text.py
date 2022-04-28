import speech_recognition as sr
# from speech.stt import SpeakText

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak anything : ")
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        # SpeakText(text)
    except:
        print("Not being able to recieve")
