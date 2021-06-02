#!/bin/bash  
rm -rf output_webp.msssim

arr=(10 20 30 40 50 60 70 80 90 95 98)

for q in ${arr[*]} 
do
    num=`echo $q | awk '{printf("%d",$0)}'`
    echo "file: ./webp_compressed_files/${q}/kodim01.jpg msssim"
    python msssim.py --original_image=../CA_EntropyModel/examples/kodim01.png --compared_image=./webp_lossy_compressed_files/${q}/kodim01.png --output_path output_webp.msssim
done
