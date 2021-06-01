#!/bin/bash  
for q in $(seq 1 9)  
do
    num=`echo $i | awk '{printf("%02d",$0)}'`
    echo "decoding ./examples/kodim${num}.png quality: ${q}"
    python decode.py --compressed_file_path ./compressed_files/1/${q}/kodim01.cmp --no_proc 4
done