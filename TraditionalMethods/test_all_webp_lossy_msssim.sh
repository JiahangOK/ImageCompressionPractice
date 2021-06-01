#!/bin/bash  

for q in $(seq 1 9)  
do
    num=`echo $q | awk '{printf("%d",$0)}'`
    echo "file: ./webp_compressed_files/${q}0/kodim01.jpg msssim"
    python msssim.py --original_image=../CA_EntropyModel_Test_v2/examples/kodim01.png --compared_image=./webp_compressed_files/${q}0/kodim01.png --output_path output_webp.msssim
done
