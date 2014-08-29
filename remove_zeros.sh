#!/bin/sh
FILES=~/Desktop/onsets/liquid_6-19-14/*

for x in $FILES
do
	echo "start process"
        cd ~/Desktop/onsets/liquid_6-19-14
        echo 'run' $x
	test -f "$x" || continue
	echo "Replacing on : $x"
	sed '/0$/d' $x > $x.tmp
	mv $x.tmp $x
	echo "Replacement done on : $x"
	echo "process done"
done 
