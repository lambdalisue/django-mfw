#!/bin/bash
ROOT=$(cd $(dirname $0);pwd)
VIRTUALENV="$ROOT/../env"
PIP="$VIRTUALENV/bin/pip"
REQUIREMENTS="$ROOT/../tests/requirements.txt"

$PIP install -r "$REQUIREMENTS"

