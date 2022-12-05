import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3
import speech_recognition


def talk(words):
    print(words)
    engene = pyttsx3.init()
    engene.say(words)
    engene.runAndWait()


def command():
    r = sr.Recognizer()

    with sr.Microphone() as sourse:
        print("Вы можете говорить: ")
        talk('Вы можете говорить')

