# Overview

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

## Os

Install arch with this guide: -

## Dependencies

Install dependencies
```
yay -S bspwm sxhkd fish polybar ttf-material-design-icons-webfont ttf-jetbrains-mono picom rofi clipster oranchelo-icon-theme dunst pulseaudio pulse-bluetooth pulsemixer mpd mpc  
```

# Keybinds

## Wm Keybinds

|    Keybind      |             Command                  |
|:---------------:|:------------------------------------:|
|   super + Enter |              Term                    |
|   super + r     |             Launcher                 |
|   super + c     |            Clipboard                 |
|   super + m     |              Music                   |
| super + {a,s,d} | Floating, Tiled or Fullscreen state  |
| super + q       |          Close Window                |
|super + Shift + r|            Restart X                 |
|   super + f     |           Change focus               |
|   super + b     |       Connect to headphones          |
|   super + g     |          Copy git token              |
|   super + m     |         Select playlist              |

*super = Windows Key

## St Keybinds

| Keybind|   Command |
|:------:|:---------:|
|ctrl + z|    Zoom   |
|ctrl + x|   Unzoom  |
|ctrl + o| Scroll up |
|ctrl + p|Scroll down|

# TCP ports used

|Port |   Script   |
|:---:|:----------:|
|3001 |  music     |
|3002 | keyboard   |
|3003 | brightness |
|3004 |  volume    |
