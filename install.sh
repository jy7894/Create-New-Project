#!/bin/bash

if grep -wq export PATH="$"PATH:/home/josh/Create-New-Project your_file.txt; then
    echo already installed
else
    echo export PATH="$"PATH:/home/josh/Create-New-Project >> ~/.bash_profile
fi