#!/usr/bin/python

import socket
import subprocess
import time

default_status = "Pick a playlist to play"
status = None

current_status = None
parse_status = None

def parse_status(status):

    #Remove the .mp3 part
    status = status[:-5]

    artist, title = status.split("-")

    parsed_status = f"{artist} - {title}"
    
    if len(parsed_status) > 27:

        rm_chars = len(parsed_status) - 25
        
        if parsed_status[:-rm_chars][-1] == " ":
            rm_chars += 1

        parsed_status = parsed_status[:-rm_chars]

        parsed_status = parsed_status + ".."
    
    return  parsed_status

def send_status(status):
    
    subprocess.run(f"echo '   Music : {status}'",shell=True)


#Send innitial default status msg
send_status(default_status)


while True:

    current_status = subprocess.run(["mpc","current"], capture_output=True) 
    current_status = current_status.stdout.decode("utf-8")

    if current_status != status:
        
        if current_status == None or current_status == "":
            send_status(default_status)

        else:
            parsed_status = parse_status(current_status) 
            send_status(parsed_status)

        status = current_status

    time.sleep(0.2)
