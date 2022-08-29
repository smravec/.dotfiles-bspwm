#Global vars
#Welcome message when starting fish
set -U -x fish_greeting ""

#Fixes for bspwm
set -U -x SXHKD_SHELL /usr/bin/bash
set -U -x SXHKD_SHELL sh
set -U -x custom_cursor_colors true

#Pfetch setup
set -U -x PF_INFO "ascii title os wm shell kernel pkgs"

if status is-interactive
    	
	#Global Path
	set -Ua fish_user_paths /home/simon/Aliases/*
	set -Ua fish_user_paths /home/simon/.local/bin
end

if status --is-login

	#Automatically execute startx on login and hide its output
	if test -z "$DISPLAY"
  	exec startx -- -keeptty >~/.xorg.log 2>&1
  end	
end
