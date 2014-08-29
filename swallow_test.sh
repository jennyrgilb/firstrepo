#!/bin/sh

cd ~/Desktop/onsets/

arr=($(find . -name 'swallow*'))
echo ${arr[@]}

for x in ${arr[@]}
do 
    cd ~/Desktop/onsets/
    sed '1d' $x > $x.tmp
    mv $x.tmp $x
    echo "swallow line removed from $x"
done
