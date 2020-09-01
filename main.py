import keyboard
from playsound import playsound

import threading
import random
import os

# Value can be changed.
# The max number of sounds allow to be played at the same time
max_sounds = 10
sounds_folder="./sounds"

# ----------------------------------------
# FROM HERE ON DOWN DON'T THE CHANGE CODE!
#                (or do?)
# ----------------------------------------

# Loads all sounds files from "sounds" directory in the same parent directory as main program.
files = os.listdir(sounds_folder)
sounds_absolute_path = os.path.abspath(sounds_folder)
files = [f'{sounds_absolute_path}/{file}' for file in files]

sounds_playing = threading.Semaphore(max_sounds)

def playsong():
    # Picks a random sound from the list of sound files
    random_index = random.randrange(len(files))
    random_sound = files[random_index]
    print(sounds_playing)
    playsound(random_sound)

    sounds_playing.release()

def callback(event):
    if sounds_playing.acquire(blocking=False):
        thread = threading.Thread(target=playsong)
        thread.start()


while keyboard.on_press(callback):
    pass
