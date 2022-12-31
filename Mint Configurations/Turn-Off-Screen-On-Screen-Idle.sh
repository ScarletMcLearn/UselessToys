#!/bin/sh

# Initial
#while :; do
#    [ $(xprintidle) -lt 3 ] && echo Hello\ World
#    sleep 1;
#done
#

# First er ta millisecond = 600000 = 10 min
# Second er ta second = 5*60 = 300 sec = 5 min


#while :; do
#    [ $(xprintidle) -lt 6000000 ] && echo Hello\ World
#    sleep 3;
#done
#

#while :; do
#    [ $(xprintidle) -eq 600000 ] && echo Hello\ World
#    sleep 3;
#done
#



#while :; do
#    [ $(xprintidle) -gt 600000 ] && echo Hello\ World
#    sleep 600;
#done




#while :; do
#    now=$(date +"%T")
#    [ $(xprintidle) -gt 60000 ] && echo "Current time : $now"
#    sleep 60;
#done


trap 'echo Turn Off Idle Screen Stopped' EXIT



echo Turn Off Idle Screen Running

while :; do
    now=$(date +"%T")
    [ $(xprintidle) -gt 10000 ] && bash -c "sleep 1; xset -display $DISPLAY dpms force off"
    sleep 10;
done




#echo Turn Off Idle Screen Stopped
