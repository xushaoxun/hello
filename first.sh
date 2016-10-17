#!/bin/bash


for i in `seq 1 5`; do
    echo $i
done

for f in `ls ~`; do
    echo $f
done

a=5
while [ $a -ge 1 ]; do
    echo $a
    a=$[$a-1]
done
