#!/bin/bash

set -e

usage(){
    echo "Usage: create_gif.sh <name> <delay>"
    exit 1
}

[ ! -z "$1" ] || usage
[ ! -z "$2" ] || usage

convert -alpha set -dispose 2 -delay $2 "$1".*.ps "../../../images/lab8/$1.gif"
rm -f "$1".*.ps
