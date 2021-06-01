# coding=utf-8
import cv2

from PIL import Image
import glob
import os
import time

def jpeg_encode(image):
    qualitys = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for q in qualitys:
        dir = './jpeg_compressed_files/{}'.format(q)
        os.makedirs(dir, exist_ok=True)
        # jpeg
        filepath = "./jpeg_compressed_files/{}/kodim01.jpg".format(q)
        start = time.time()
        image.save(filepath, "JPEG", quality=q)
        end = time.time()

        w, h = image.size
        size = w * h

        file_size = os.path.getsize(filepath) * 8
        bpp = file_size / size
        with open('./jpeg_compressed_files/bpp.txt', 'a+') as f:
            f.write(str(bpp)+'\n')
        with open('./jpeg_compressed_files/time.txt', 'a+') as f:
            f.write(str(end-start)+'\n')


if __name__ == "__main__":
    im = Image.open(
        '../CA_EntropyModel_Test_v2/examples/kodim01.png').convert("RGB")
    jpeg_encode(im)
