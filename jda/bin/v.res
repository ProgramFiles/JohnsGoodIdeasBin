#!/bin/bash

pdur() {
    local A="$1" 
    local B=${#A}
    if ((B > 50)); then
        echo -ne "$A:\n    "
    else
        echo -n "$A: "
    fi
    echo -n "Resolution: "
    avprobe "$A" 2>&1 | grep "Video:" | grep -o -E "[0-9]+x[0-9]+"
}
pfs() {
    for s; do
        pdur "$s"
    done
}

if [ -z "$*" ]; then
    pfs *.mp4
else
    pfs "$@"
fi
