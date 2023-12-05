import gtts
import playsound
from time import sleep
import os
from datetime import datetime


while True:
    user_input = input("What do you want to type? (Type 'no' to stop) ")

    if user_input.lower() == "no":
        break  # Exit the loop if the user inputs 'no'

    text_to_speech = gtts.gTTS(user_input, lang='en')
    text_to_speech.save("speech.mp3")
    playsound.playsound("speech.mp3")
    os.remove("speech.mp3")
    
