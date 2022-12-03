from googletrans import Translator

text1 = "Я люблю пиццу"

translator = Translator()

print(translator.translate(text1, src='ru', dest='en').text)