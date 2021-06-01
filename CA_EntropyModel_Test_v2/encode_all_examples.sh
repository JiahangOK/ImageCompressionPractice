#!/bin/bash  
for q in $(seq 1 9)  
do
    # for i in $(seq 1 24)  
    # do
    num=`echo $i | awk '{printf("%02d",$0)}'`
    echo "encoding ./examples/kodim${num}.png quality: ${q}"
    python encode.py --model_type 1 --input_path ./examples/kodim01.png --quality_level ${q} --no_proc 4
    # done   
done