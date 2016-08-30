#!/bin/sh

set -e

find -name "*.ps" -delete

for x in `find -name "*.py" -executable`; do
    echo python3 $x;
done | parallel -j 20 --eta

for x in `find -name "*.py" -executable`; do
    f=`basename $x`
    echo ./create_gif.sh "${f%.*}" 10
done | parallel --eta