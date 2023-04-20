import pyttsx3  # module to convert text to speech
import speech_recognition as sr  # pip install SpeechRecognition #speech to text
import webbrowser  # builtin module
import datetime
import pyjokes  # generate jokes programatically
import os
import time


def speech_text():
    recognize = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something to recognize")
        print("Listening...")
        recognize.adjust_for_ambient_noise(source)
        audio = recognize.listen(source)
        try:
            data = recognize.recognize_google(audio)
            return data
        except sr.UnknownValueError:
            print("Unable to recognize speech")
        except sr.RequestError:
            print("Speech recognition request error")


def textsp(x):
    class_call = pyttsx3.init()
    voices_call = class_call.getProperty('voices')
    class_call.setProperty('voice', voices_call[0].id)
    speed_rate = class_call.getProperty('rate')
    class_call.setProperty('rate', 150)
    class_call.say(x)
    class_call.runAndWait()


textsp("Hello Welcome")

if __name__ == '__main__':
    keyword = 'hey barshan'
    while True:
        data1 = speech_text().lower()
        if keyword in data1:
            if "what is your name" in data1:
                name = "my name is Barshan"
                textsp(name)
            elif "how old are you" in data1:
                age = "I am 26 years old"
                textsp(age)
            elif "can you take me to google search engine" in data1:
                webbrowser.open("https://google.com")
            elif "now time" in data1:
                # strftime for searching#I for hr#M for minute#p for AM or PM
                time = datetime.datetime.now().strftime("%I%M%p")
                textsp(time)
            elif "joke" in data1:
                joke1 = pyjokes.get_jokes(language="en", category="neutral")
                textsp(joke1)
            elif "play music" in data1:
                add = "D:\AudioSSSS\band"
                listsong = os.listdir(add)
                os.startfile(os.path.join(add, listsong[0]))
            elif "exit" in data1:
                textsp("Thank You")
                break
            time.sleep(5)
        else:
            print("Thanks")
    # Change ends here
