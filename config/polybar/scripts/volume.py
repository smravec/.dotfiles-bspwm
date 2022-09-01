#!/usr/bin/python

import time
import subprocess

icons = ["󰝟","󰕾"]

def echo_volume(status):
    subprocess.run("echo " + "'     %{T6}" + status + "%{T-}'",shell = True)

while True:
    
    mute = subprocess.run("pulsemixer --get-mute",shell=True,capture_output=True)
    mute = int(mute.stdout.decode("utf-8"))

    if mute != 0:
        echo_volume(icons[0])
    
    else:
        echo_volume(icons[1])

    time.sleep(0.5)
