#!/usr/bin/python

import subprocess

input_to_rofi = "'Casual\nMotivational\nUpbeat\nStop playback'"

config = "~/.config/rofi/select_playlist_rofi.rasi"

title = "'Select a playlist'"

def check_if_first_startup():
    #This function checks how many things are turned off in mpd
    #There are 4 things that can be turned off from which 2 I want to be turned on

    status = subprocess.run("mpc status | grep -o off | wc -l ", shell = True, capture_output = True)
    
    #Here compares how many things it are off if more than 2 are off, this is first startup
    if int(status.stdout.decode("utf-8")) > 2:
         
        subprocess.run("mpc random", shell = True)
        subprocess.run("mpc repeat", shell = True)

rofi_instance = subprocess.run(
                                f"echo -e {input_to_rofi} | rofi -dmenu -p {title} -config {config}",
                                shell = True,
                                capture_output = True
                                )

output = rofi_instance.stdout.decode("utf-8")

#Check if something was selected
if output != "":
    
    subprocess.run("mpc clear", shell = True)
    
    #Check if any playlist was selected
    if output != "Stop playback\n":
        
        check_if_first_startup() 
        
        subprocess.run(f"mpc load {output[:-1].lower()}", shell = True)
        subprocess.run(f"mpc play" , shell = True)
