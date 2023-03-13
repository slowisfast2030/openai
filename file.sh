#!/bin/bash
line_num=0
while read line
do
    #line_num=$(($line_num+1))
    let "line_num=line_num+1"
    printf "Line %3d : %s\n" $line_num $line
done < "file.txt"


// 写一段快排代码