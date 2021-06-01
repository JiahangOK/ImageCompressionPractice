# coding=utf-8
import cv2

from PIL import Image
import glob
import os
import time

def webp_encode(image):
    dir = './webp_lossless_compressed_files/'
    os.makedirs(dir, exist_ok=True)
    # png
    filepath = "./webp_lossless_compressed_files/kodim01.webp"
    start = time.time()
    image.save(filepath, "WEBP", lossless = True)
    end = time.time()

    w, h = image.size
    size = w * h

    file_size = os.path.getsize(filepath) * 8
    bpp = file_size / size
    with open('./webp_lossless_compressed_files/bpp.txt', 'w') as f:
        f.write(str(bpp)+'\n')
    with open('./webp_lossless_compressed_files/time.txt', 'w') as f:
        f.write(str(end-start)+'\n')


if __name__ == "__main__":
    im = Image.open(
        '../CA_EntropyModel/examples/kodim01.png').convert("RGB")
    webp_encode(im)
