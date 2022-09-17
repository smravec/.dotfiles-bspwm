# Overview
<img src=Preview1.png/>

- **Window Manager:** [bspwm](https://github.com/baskerville/bspwm)
- **Shell:** [fish](https://github.com/fish-shell/fish-shell)
- **Term:** [st](https://st.suckless.org)
- **Bar** [polybar](https://github.com/polybar/polybar)
- **Compositor** [picom](https://github.com/yshui/picom)
- **Editor** vim/nvim
- **Application Launcher** [rofi](https://github.com/davatorium/rofi)
- **GTK Theme** [oranchelo](https://github.com/OrancheloTeam/oranchelo-icon-theme)
- **Notification Daemon** [dunst](https://github.com/dunst-project/dunst)
- **Music server** [mpd](https://github.com/MusicPlayerDaemon/MPD)

# Instalation
Clone this repo
```
git clone https://github.com/smravec/.dotfiles
```

## Os
Install arch with this guide: -

## Term
Compile st
```
cd .dotfiles/st
sudo make install
```

## Dependencies

Install dependencies
```
yay -S xorg xorg-xinit xclip xcursor-breeze xcb-util-cursor unclutter oranchelo-icon-theme \
       bspwm sxhkd picom polybar \
       fish \
       ttf-material-desing-icons-webfont ttf-jetbrains-mono \
       pulseaudio pulse-bluetooth pulsemixer mpd mpc \
       rofi clipster dunst \
       firefox-developer-edition libreoffice vscodium-bin superproductivity-bin ocenaudio-bin krita vlc shotcut \
       discord signal-desktop \
       brightnessctl bluetoothctl \
       cmatrix oneko cava pfetch feh colorpicker gtop pipes.sh tty-clock-git ranger libmagick \
       nodejs npm python python-pip \
       xf86-video-intel intel-media-driver 
```
```
pip install pypresence youtube-dl yt-dlp
```

# Keybinds

## Wm and Other Keybinds

|    Keybind      |             Command                  |
|:---------------:|:------------------------------------:|
|   super + Enter |              Term                    |
|   super + r     |             Launcher                 |
|   super + c     |            Clipboard                 |
|   super + m     |              Music                   |
| super + {a,s,d} | Floating, Tiled or Fullscreen state  |
|   super + q     |          Close Window                |
|super + Shift + r|            Restart X                 |
|   super + f     |           Change focus               |
|   super + b     |       Connect to headphones          |
|   super + g     |          Copy git token              |
|   super + m     |         Select playlist              |
|   super + n     |    Show last Dunst notification      |

****super = Windows Key***

## St Keybinds

| Keybind|   Command |
|:------:|:---------:|
|ctrl + z|   Zoom    |
|ctrl + x|  Unzoom   |
|ctrl + o| Scroll up |
|ctrl + p|Scroll down|
