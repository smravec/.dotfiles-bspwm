#!/bin/sh

workspaces() {
	#Check if Focused
	f2=$(bspc query -D -d focused --names | grep 2)
	f3=$(bspc query -D -d focused --names | grep 3)
	f4=$(bspc query -D -d focused --names | grep 4)
	f5=$(bspc query -D -d focused --names | grep 5)
	f6=$(bspc query -D -d focused --names | grep 6)
	f7=$(bspc query -D -d focused --names | grep 7)
	
	#Colors
	foc="#ffffff"
	focnot="#281E2D"
	underline="#cccccc"

	content2="%{F$focnot}󰅬%{F-}"
	content3="%{F$focnot}󰅨%{F-}"
	content4="%{F$focnot}󰛍%{F-}" 
	content5="%{F$focnot}󱃖%{F-}"	
	content6="%{F$focnot}󰈚%{F-}"
	content7="%{F$focnot}󰇟%{F-}"

	[[ "$f2" ]] && content2="%{u$underline}%{+u}%{F$foc}󰅬%{F-}%{-u}"
	[[ "$f3" ]] && content3="%{u$underline}%{+u}%{F$foc}󰅨%{F-}%{-u}"
	[[ "$f4" ]] && content4="%{u$underline}%{+u}%{F$foc}󰛍%{F-}%{-u}"
	[[ "$f5" ]] && content5="%{u$underline}%{+u}%{F$foc}󱃖%{F-}%{-u}"
	[[ "$f6" ]] && content6="%{u$underline}%{+u}%{F$foc}󰈚%{F-}%{-u}"
	[[ "$f7" ]] && content7="%{u$underline}%{+u}%{F$foc}󰇟%{F-}%{-u}"

	echo -e "$content2       $content3      $content4      $content5      $content6      $content7"
}

workspaces
bspc subscribe desktop node_transfer | while read -r _ ; do
workspaces
done
