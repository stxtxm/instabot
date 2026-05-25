#!/bin/bash
while true; do
    python main.py
    delay=$(( (RANDOM % 7200) + 3600 ))  # 3600-10800 sec = 1h-3h
    echo "Next run in $((delay / 60)) minutes..."
    sleep "$delay"
done