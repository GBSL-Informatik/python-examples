from gtts import gTTS
from playsound import playsound

text = 'Hallo ich bin Elsa'

gruefnisch = text.lower()
gruefnisch = gruefnisch.replace('a', 'anafa')
gruefnisch = gruefnisch.replace('e', 'enefe')
gruefnisch = gruefnisch.replace('i', 'inifi')
gruefnisch = gruefnisch.replace('o', 'onofo')
gruefnisch = gruefnisch.replace('u', 'unufu')
gruefnisch = gruefnisch.replace('ä', 'änäfä')
gruefnisch = gruefnisch.replace('ö', 'önöfö')
gruefnisch = gruefnisch.replace('ü', 'ünüfü')

print(gruefnisch)

spoken_text = gTTS(text=text, lang='de', slow=False)
spoken_text.save('speak_out.mp3')
playsound('speak_out.mp3')
