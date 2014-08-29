#!/bin/sh
#removing missing

FILES=~/Desktop/onsets/output/*

for x in $FILES
do
	echo "start process"
        cd ~/Desktop/onsets/output
        echo 'run' $x
	test -f "$x" || continue
	echo "Replacing on : $x"
	grep 999 $x >$x.tmp
	mv $x.tmp $x"miss".txt
	sed '/999.000000$/d' $x > $x.tmp
	mv $x.tmp $x
	echo "Replacement done on : $x"
	echo "process done"
done 
