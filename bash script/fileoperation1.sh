#!/bin/bash

FILE="/home/ken/code/bash script/randomfile"

if [ -e "$FILE" ]
	then 
		echo "file $FILE path is valid"
fi

if [ -x "$FILE" ]
	then
		echo "the file can be modified"
	else
		echo "the file can not be modified"
fi

