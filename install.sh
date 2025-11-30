#!/bin/bash

LINE='export PATH="$PATH:/home/josh/Create-New-Project"'
FILE="$HOME/.bash_profile"

# Check if the line already exists
if grep -Fxq "$LINE" "$FILE"; then
    echo "already installed"
else
    echo "$LINE" >> "$FILE"
    echo "installed"
fi