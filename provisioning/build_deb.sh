#!/bin/bash

function run() { echo "\$ $@" ; "$@" ; }

export PROJECT_NAME='hello'

run debinate clean
run debinate package