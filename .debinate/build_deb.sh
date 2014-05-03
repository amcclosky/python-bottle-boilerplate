#!/bin/bash

set -e

function run() { echo "\$ $@" ; "$@" ; }

# http://stackoverflow.com/questions/59895/can-a-bash-script-tell-what-directory-its-stored-in
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

export PROJECT_NAME='hello'

run cd $SCRIPT_DIR/..

run debinate clean
run debinate package