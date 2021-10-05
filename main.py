import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init ( 'sapi5' )
voices = engine.getProperty ( 'voices' )
print ( voices[1].id )
engine.setProperty ( 'voice', voices[0].id )


def speak(audio):
    engine.say ( audio )
    engine.runAndWait ()


def wishMe():
    hour = int ( datetime.datetime.now ().hour )
    if 0 <= hour < 12:
        speak ( "Good Morning Ohm!" )

    elif 12 <= hour < 18:
        speak ( "Good Afternoon Ohm!" )

    else:
        speak ( "Good Evening Ohm!" )

    speak ( "I am Jarvis Sir. Please tell me how may I help you ?" )


def takeCommand():
    r = sr.Recognizer ()
    with sr.Microphone () as source:
        print ( "Listening..." )
        r.pause_threshold = 1
        audio = r.listen ( source )

    try:
        print ( "Recognizing..." )
        queried = r.recognize_google ( audio, language='en-in' )
        print ( f"You told me to: {queried}\n" )

    except Exception:
        print ( "Say that again please..." )
        return "None"
    return queried


if __name__ == "__main__":
    wishMe ()
    run = True
    while run:

        query = takeCommand ().lower ()

        if 'youtube' in query:
            speak ( "Opening Youtube" )
            print ( "Opening Youtube" )
            webbrowser.open ( "youtube.com" )

        elif 'google' in query:
            speak ( "Opening Google" )
            print ( "Opening Google" )
            webbrowser.open ( "google.com" )

        elif 'stack overflow' in query:
            speak ( "Opening Stackoverflow" )
            print ( "Opening Stackoverflow" )
            webbrowser.open ( "stackoverflow.com" )

        elif 'time' in query:
            strTime = datetime.datetime.now ().strftime ( "%H:%M:%S" )
            speak ( f"Sir, the time is {strTime}" )

        elif 'wikipedia' in query:
            speak ( 'Searching Wikipedia...' )
            query = query.replace ( "wikipedia", "" )
            results = wikipedia.summary ( query, sentences=2 )
            speak ( "According to Wikipedia" )
            print ( results )
            speak ( results )

        elif 'exit' in query:
            run = False
