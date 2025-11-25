#!/bin/bash

projectName=$1
language=$2
path=$3
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

if [ -x "$path"]; then 
    path="$(pwd)"
fi

if [ -z "$PY_CMD" ] && command -v py >/dev/null 2>&1; then
    PY_CMD=py
fi

if [ -z "$PY_CMD" ] && command -v python3 >/dev/null 2>&1; then
    PY_CMD=python3
fi

if [ -z "$PY_CMD" ] && command -v python >/dev/null 2>&1; then
    PY_CMD=python
fi

if [ -z "$PY_CMD" ]; then
    echo "No Python installation found."
    exit 1
fi

"$PY_CMD" "$SCRIPT_DIR"/src/main.py "$projectName" "$language" "$path"
