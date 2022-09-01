#!/usr/bin/python

import time
import subprocess
import socket
import sys

keypress_or_loop = sys.argv[1]

icons = ["󰃚","󰃛","󰃜","󰃝","󰃞","󰃟","󰃠"]
options = [960,12000,24000,40000,68000,83000,96000]


def get_brightness():

    current_brightness = subprocess.run("brightnessctl g",
                                        shell=True,capture_output=True)

    current_brightness = int(current_brightness.stdout.decode("utf-8"))


    return current_brightness

def send_brightness(status):
    status = "'     %{T5}" + status + "%{T-}  '"
    subprocess.run(f"echo -e {status}",shell=True)

current_brightness = get_brightness()

if len(sys.argv) >= 3:
    operator = sys.argv[2]

    if operator == "-" and current_brightness != options[0] or operator == "+" and current_brightness != options[-1]:

        if operator == "+":
            subprocess.run(f"brightnessctl s {options[options.index(current_brightness)+1]}",shell=True)
    
        else:
            subprocess.run(f"brightnessctl s {options[options.index(current_brightness)-1]}",shell=True)


if keypress_or_loop == "loop":
        
    while True:

        current_brightness = get_brightness()

        send_brightness(icons[options.index(current_brightness)])

        time.sleep(0.3)
