#!/bin/bash  
for q in $(seq 1 9)  
do
    num=`echo $q | awk '{printf("%d",$0)}'`
    echo "file: ./compressed_files/1/${q}/kodim01.png msssim"
    python msssim.py --original_image=./examples/kodim01.png --compared_image=./compressed_files/1/${q}/kodim01.png
done
