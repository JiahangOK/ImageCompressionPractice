# coding=utf-8
import cv2

from PIL import Image
import glob
import os
import time

def webp_encode(image):
    qualitys = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for q in qualitys:
        dir = './webp_lossy_compressed_files/{}'.format(q)
        os.makedirs(dir, exist_ok=True)
        # webp
        filepath = "./webp_lossy_compressed_files/{}/kodim01.webp".format(q)
        start = time.time()
        image.save(filepath, "WEBP", quality=q)
        end = time.time()

        w, h = image.size
        size = w * h

        file_size = os.path.getsize(filepath) * 8
        bpp = file_size / size
        with open('./webp_lossy_compressed_files/bpp.txt', 'a+') as f:
            f.write(str(bpp)+'\n')
        with open('./webp_lossy_compressed_files/time.txt', 'a+') as f:
            f.write(str(end - start)+'\n')
def webp_decode():
    qualitys = [10, 20, 30, 40, 50, 60, 70, 80, 90]

    for q in qualitys:
        dir = './webp_lossy_compressed_files/{}'.format(q)
        os.makedirs(dir, exist_ok=True)
        # webp
        filepath = "./webp_lossy_compressed_files/{}/kodim01.webp".format(q)
        save_filepath =  "./webp_lossy_compressed_files/{}/kodim01.png".format(q)
        im = Image.open(filepath).convert("RGB")
        im.save(save_filepath, "PNG")

if __name__ == "__main__":
    im = Image.open(
        '../CA_EntropyModel/examples/kodim01.png').convert("RGB")
    webp_encode(im)
    webp_decode()
