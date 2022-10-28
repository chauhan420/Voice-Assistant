import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import pyjokes
import os
import time
import pywhatkit
import phonenumbers
import wikipedia


def sptext():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        recognizer.pause_threshold = 1
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio, language='en-in')
            print(f"user said: {data}\n")
            return data
        except sr.UnknownValueError:
            print("Not Understanding")


def textto_speech(x):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 130)
    engine.say(x)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        textto_speech("Good Morning,sir")
    elif hour >= 12 and hour < 18:
        textto_speech("Good Afternoon,sir")
    else:
        textto_speech("Good Evening,sir")

    textto_speech("Please tell your identity")

def sent_whatmsg(message):
    pywhatkit.sendwhatmsg("mibile_no", message, 9, 6)


def sent_messages():
    file = open("PyWhatKit_DB.txt", "r")
    print(file.read())


def phone_location():
    number = "Mobile_no"
    from phonenumbers import geocoder
    ch_nmber = phonenumbers.parse(number, "CH")
    loc = geocoder.description_for_number(ch_nmber, "en")
    print("Phone number located in :", loc)
    textto_speech("Phone number located in :{}".format(loc))


if __name__ == '__main__':
    wishMe()
    if sptext().lower() == "sudheer":
        textto_speech("you are most welcome sir, now i am your personal assistant ,how can i help you")
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is jira"
                textto_speech(name)
            elif "old are you" in data1:
                age = "I was just created a few time ago  "
                textto_speech(age)
            elif "time" in data1:
                time = datetime.datetime.now().strftime("%I%M%p")
                textto_speech(time)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "joke" in data1:
                joke_1 = pyjokes.get_joke(language="en", category="neutral")
                print(joke_1)
                textto_speech(joke_1)
            elif "play song" in data1:
                add = "D:\music"
                listsong = os.listdir(add)
                print(listsong)
                os.startfile(os.path.join(add, listsong[1]))
            elif "whatsapp" in data1:
                textto_speech("what is the message")
                message=sptext()
                sent_whatmsg(message)
                print("Message sent!")
            elif "send data" in data1:
                sent_messages()
            elif "number location" in data1:
                phone_location()
            elif "wikipedia" in data1:
                textto_speech('I am searching wait....')
                data1 = data1.replace("wikipedia", "")
                results = wikipedia.summary(data1, sentences=1)
                textto_speech("According to wikipedia")
                print(results)
                textto_speech(results)
            elif "exit" in data1:
                textto_speech("Thnak You")
                print("Thanku!")
                break
            time.sleep(3)
    else:
        print("Thanks!")
