#!/bin/bash
ROOT=$(cd $(dirname $0);pwd)
VIRTUALENV="$ROOT/../env"
PYTHON="$VIRTUALENV/bin/python"
SH="/bin/bash"

$SH $ROOT/virtualenv.sh
$SH $ROOT/pip_install.sh

cd "$ROOT/../"
$PYTHON tests/src/miniblog/manage.py jenkins

