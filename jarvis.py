# Just A Rather Very Intelligent System(JARVIS)

import pyttsx3
import datetime
import speech_recognition as sr
#import pyaudio
import webbrowser

engine = pyttsx3.init('sapi5')


voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

 
def wishme():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    elif currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')


    speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
    speak('How may I help you?')

def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
if __name__ == '__main__':
    wishme()
    #speak('ravi gupta .. hello sir ')
    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
          #  speak('okay')
            webbrowser.open('www.youtube.com')




     
