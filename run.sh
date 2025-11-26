#!/bin/bash

projectName=$1
language=$2
path=$3
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ -z "$projectName" ]; then
    echo "project name:"
    read projectName
fi

if [ -z "$language" ]; then
    echo "language:"
    read language
fi

if [ -z "$path" ]; then 
    echo "path<Optional>:"
    read path

    if [ -z "$path" ]; then 
        path="$(pwd)"
    fi
fi

for i in python3 python py; do
    if [ -z "$PY_CMD" ] && command -v $i >/dev/null 2>&1; then
        PY_CMD="$i"
    fi
done

if [ -z "$PY_CMD" ]; then
    echo "No Python installation found."
    exit 1
fi

"$PY_CMD" "$SCRIPT_DIR"/src/main.py "$projectName" "$language" "$path"
