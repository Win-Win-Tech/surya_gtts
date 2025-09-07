import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)      # Speed of speech
engine.setProperty('volume', 10.0)    # Volume (0.0 to 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_DAVID_11.0')  # Change index for male/female

for voice in voices:
    print(voice.id, voice.name)

engine.say("Hello FIVE, your automation is sounding great!")
engine.runAndWait()




