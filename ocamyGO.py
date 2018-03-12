"""
This is a minimal python chat client which connects to the `room:lobby` topic.
The server is supposed to be
http://www.phoenixframework.org/docs/channels#section-tying-it-all-together
"""
from __future__ import print_function
import numpy as np
from time import sleep
from PIL import Image
import sys


try:  # py2
    get_user_input = raw_input
except:  # py3
    get_user_input = input

from occamy import Socket


# socket = Socket("ws://dlevs.me:4000/socket")
# socket.connect()
# channel = socket.channel("room:lobby", {})
# channel.on("new_msg", lambda msg, x: print("> {}".format(msg["body"])))
# channel.join()
#print("Enter your message and press return to send the message.")
#print()


def load_img(filename):
    img = Image.open(filename)
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


# geebs = np.zeros(1152);
strobo = ''
name = sys.argv[1]
filename = 'tests/'+name+'/screenshot_pixelated_gray_inverted.png'
img = load_img(filename)
num_cols = int(48)
square_w = float(img.shape[1]) / num_cols
num_rows = int(24)
square_h = float(img.shape[0]) / num_rows

f = open('tests/'+name+'/out.txt', 'w')

# while True: 
for row in range(num_rows):
    for col in range(num_cols):
        ele = make_one_square(img, row, col, square_h, square_w)
        # print(ele)
        f.write(" "+ str(ele)) 

f.close()


f = open('tests/'+name+'/out.txt', 'r')
strobo = f.read();
f.close()
print(strobo)

# channel.push("input",{"body": strobo})
