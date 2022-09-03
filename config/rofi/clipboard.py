#!/usr/bin/python

import subprocess

how_many_items_to_display = 32

clipboard = subprocess.run(["clipster","-c","-n","0","-o","-0"],
                            capture_output=True,encoding="utf-8").stdout.split("\0")

current_item_from_back = len(clipboard) - 1

while current_item_from_back >= 0:
     
    if clipboard[current_item_from_back] == "" or clipboard[current_item_from_back].strip() == "" :
        del clipboard[current_item_from_back]
    
    elif clipboard[current_item_from_back][0] == " " and len(clipboard[current_item_from_back]) == 1 :
        del clipboard[current_item_from_back]

    else:
        clipboard[current_item_from_back] = clipboard[current_item_from_back].strip()
        
    current_item_from_back -= 1

clipboard_to_display = [item.replace('\n', ' ')[0:250] for item in clipboard]

rofi = subprocess.run(["rofi", "-config", "~/.config/rofi/clipboard.rasi", "-dmenu","-p","Clipboard","format","i","-i","-sep","nul"],
                        encoding = "utf-8",input="\n".join(clipboard_to_display), capture_output=True)

paste_to_xclip = rofi.stdout

paste_to_xclip = paste_to_xclip.strip("\n")

subprocess.run(f"echo -e -n '{paste_to_xclip}' | xclip -selection clipboard",shell=True)
