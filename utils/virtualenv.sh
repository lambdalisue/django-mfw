#!/bin/bash
ROOT=$(cd $(dirname $0);pwd)
VIRTUALENV="$ROOT/../env"

if [ -e "$VIRTUALENV" ]; then
    rm -rf "$VIRTUALENV"
fi
virtualenv --distribute --no-site-packages "$VIRTUALENV"
