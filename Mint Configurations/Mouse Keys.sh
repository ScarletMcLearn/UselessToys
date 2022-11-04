#!/bin/bash
[ $(xfconf-query -c accessibility -p /MouseKeys) == "false" ] \
    && $(xfconf-query -c accessibility -p /MouseKeys -s true) \
    || $(xfconf-query -c accessibility -p /MouseKeys -s false)
