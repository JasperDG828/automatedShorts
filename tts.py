import pyttsx3
engine = pyttsx3.init()
engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.setProperty('rate', 150) 
def say(text, save):
    engine.save_to_file(text, f'./audio/{save}.mp3')
    engine.runAndWait()
