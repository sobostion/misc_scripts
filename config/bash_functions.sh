#!/bin/bash

# Some functions that come in handy every now and again

# numgrep: count number of times a phrase appears in each file of a directory
ng(){
    grep --count -ir $1 . | grep -v :0
}

# for renaming terminal windows
title() {
    echo -ne "\033]0;"$*"\007"
}

# clear screen with new lines
# useful when you need to see where one long output ends
# and another begins
cl() {
    count=0;
    while [ $count -lt 50 ]; do
        echo ""
        count=$(($count + 1))
    done
}
