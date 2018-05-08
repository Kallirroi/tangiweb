
from __future__ import print_function
import numpy as np
from time import sleep
from PIL import Image
import sys

try:  # py2
    get_user_input = raw_input
except:  # py3
    get_user_input = input

def load_img(filepath):
    img = Image.open(filepath)
    data = np.array(img)
    return data

def all_square_pixels(row, col, square_h, square_w):
    for y in xrange(int(round(row*square_h)), int(round((row+1)*square_h))):
        for x in xrange(int(round(col*square_w)), int(round((col+1)*square_w))):
            yield y, x

def make_one_square(img, row, col, square_h, square_w):
    pixels = []
    for y, x in all_square_pixels(row, col, square_h, square_w):
        pixels.append(img[y][x])
    av = 0
    for x in pixels:
        av += x
    av /=len(pixels)
    return av

path = sys.argv[1]
for x in xrange(1,37):
    filepath = path+'screen_'+str(x)+'_pixelated_gray.png'
    print(filepath)
    img = load_img(filepath)
    img = np.concatenate((img, img, img), axis=1)
    num_cols = int(48)
    square_w = float(img.shape[1]) / num_cols
    num_rows = int(24)
    square_h = float(img.shape[0]) / num_rows

    f = open(path+'out'+str(x)+'.txt', 'w')
    for row in range(num_rows):
        for col in range(num_cols):
            ele = make_one_square(img, row, col, square_h, square_w)
            f.write(" "+ str(ele)) 
    f.close()
