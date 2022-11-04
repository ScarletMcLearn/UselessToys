bash -c 'flatpak run com.google.Chrome'
bash -c 'flatpak run com.microsoft.Teams'
bash -c 'sleep 1; xset -display $DISPLAY dpms force off'
bash -c "xrandr --output eDP-1 --off" 
