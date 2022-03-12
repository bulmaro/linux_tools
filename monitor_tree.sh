#!/bin/bash
while :
do
    cd .
    clear
	tree
    echo
    df -h | grep '/data\|Filesystem'
	sleep 1
done