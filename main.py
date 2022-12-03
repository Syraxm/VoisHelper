import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
from playsound import playsound

mic = sr.Microphone(device_index=1)
translator = Translator()

r = sr.Recognizer()
with mic as source:
    print("Что перевести?: ")
    tts = gTTS("Что вы хотите перевести?", lang="ru")
    tts.save("output.mp3")
    playsound("output.mp3")
    audio = r.listen(source)

try:
    a = r.recognize_google(audio, language="ru-RU")
    result = translator.translate(a, src='ru', dest='en').text
    print(result)
    tts = gTTS(result, lang="en")
    tts.save("outputt.mp3")
    playsound("outputt.mp3")
except sr.UnknownValueError:
    print("Говори по-человечески, плиз")
except sr.RequestError as e:
    print("Хз чё случилось")
