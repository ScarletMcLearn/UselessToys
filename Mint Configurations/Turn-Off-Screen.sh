#!/bin/sh

#### sleep 1 && xset dpms force standby
# sleep 0.2
bash -c "sleep 1; xset -display $DISPLAY dpms force off"
