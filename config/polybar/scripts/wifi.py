#!/usr/bin/python

import time
import subprocess

icons = ["󰖩","󱚵","󰖪"]

def wifi_status():
    
    #Check if wifi module is enabled
    wifi_enabled = subprocess.run("nmcli radio wifi",
                                   capture_output = True, shell=True)
    
    if wifi_enabled.stdout.decode("utf8") == "enabled\n":

        nmcli = subprocess.run("nmcli -o | grep wlan0",
                            capture_output = True, shell=True)

        wifi_status = nmcli.stdout.decode("utf8")
    
        wifi_status = wifi_status.split(":")
        wifi_status = wifi_status[1].split("\n")
        wifi_status = wifi_status[0].strip(" ")
        
        if wifi_status == "disconnected":
            return "disconnected"
        
        else: 
            return "connected"
    else:
        return "turned off"


def echo_wifi(status):
    subprocess.run("echo " + "'   " + "%{T4}" + status +"%{T-}  '",
                    shell=True)


while True:

    wifi_status_parsed = wifi_status()

    if wifi_status_parsed == "turned off":
        echo_wifi(icons[2])        

    else:

        if wifi_status_parsed == "disconnected":
            echo_wifi(icons[1])

        else:
            echo_wifi(icons[0])
                

    time.sleep(0.5)

