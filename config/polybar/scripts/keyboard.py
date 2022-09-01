#!/usr/bin/python

import time
import subprocess

def echo_keyboard(keyboard):
    subprocess.run("echo " + "' | " + keyboard + "'",shell=True)

while True:
    current_keyboard = subprocess.run("setxkbmap -query | grep us",
                                      shell = True, capture_output = True)
    current_keyboard = current_keyboard.stdout.decode("utf-8")

    if current_keyboard != "":
        echo_keyboard("ENG")
    else:
        echo_keyboard("SLK")

    time.sleep(0.3)
