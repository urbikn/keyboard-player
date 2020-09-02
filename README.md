# Keyboard player (⌨🔉)

A program which plays an audio sample on every keypress.

The audio samples are read from the directory "**./sounds**".

## Installation

The project comes with a **requirements.txt** file, so just clone the repo and run:

    sudo pip3 install -r requirements.txt

After that just run the program like so:

    sudo python3 main.py

The program has to be run with sudo privilages, because the keyboard library uses global event hooks - meaning it captures keys regardless of the program currently listening to the keyboard.

## Advice

Use short audio samples, because if the sample is too long, it just gets annoying and boring to listen to... A good rule of thumb is anything below a second. Or just try it for yourself.
