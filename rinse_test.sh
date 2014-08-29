#!/bin/sh

cd ~/Desktop/onsets/

arr=($(find . -name 'rinse*'))
echo ${arr[@]}

for x in ${arr[@]}
do 
    cd ~/Desktop/onsets/
    sed '1d' $x > $x.tmp
    mv $x.tmp $x
    echo "rinse line removed from $x"
done
