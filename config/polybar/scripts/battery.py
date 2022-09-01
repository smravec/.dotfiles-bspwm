#!/usr/bin/python

import subprocess
import time

def current_bat_level():
    acpi = subprocess.run(["acpi"], capture_output=True)

    bat_status = acpi.stdout.decode("utf-8") 
    
    #Format bat level
    bat_level = bat_status.split(",")[1]
    bat_level = bat_level[:-1]
    bat_level = bat_level.strip(" ")

    return int(bat_level)

def is_charging():
    
    charging = ""

    acpi = subprocess.run("acpi | grep Discharging",
                          capture_output = True,shell = True)

    bat_status = acpi.stdout.decode("utf-8")
   
    if bat_status == "":
        charging = "%{T3}󱐋%{T-}"

    return charging

def echo_bat(battery):
    subprocess.run("echo -e " + is_charging() + "%{T3}" + battery  + "%{T-}",shell = True)

while True:
    if current_bat_level() >= 91:
        echo_bat("󰁹") 
    
    elif current_bat_level() >= 81:
        echo_bat("󰂂")

    elif current_bat_level() >= 71:
        echo_bat("󰂁")

    elif current_bat_level() >= 61:
        echo_bat("󰂀")

    elif current_bat_level() >= 51:
        echo_bat("󰁿")

    elif current_bat_level() >= 41:
        echo_bat("󰁾")
    
    elif current_bat_level() >= 31:
        echo_bat("󰁽")

    elif current_bat_level() >= 21:
        echo_bat("󰁼")

    elif current_bat_level() >= 11:
        echo_bat("󰁻")

    else: 
        echo_bat("󰁺")


    time.sleep(1)


