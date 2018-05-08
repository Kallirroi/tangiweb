import cv2
from occamy import Socket
import numpy as np
from matplotlib import pyplot as plt


# ---------------------------------------- data loading
dictlist = []
originals = {}
for x in xrange(1,37):
    originalImagePath = 'tests/semantic/everything/CNNshortNoExtensionCropped/screen_'+str(x)+'.png'
    im = cv2.imread(originalImagePath)
    height, width = im.shape[:2]
    originals[x] = cv2.resize(im, (2400/2, 1400/2), interpolation = cv2.INTER_NEAREST)
dictlist.append(originals)

finals = {}
for x in xrange(1,37):
    finalImagePath = 'tests/semantic/everything/CNNshort16x24/pixelated_grayCropped/screen_'+str(x)+'_pixelated_gray.png'
    im = cv2.imread(finalImagePath)
    height, width = im.shape[:2]
    finals[x] = cv2.resize(im, (2400/2, 1400/2), interpolation = cv2.INTER_NEAREST)
dictlist.append(finals)

forServer = {}
for x in xrange(1,37):
    with open('tests/semantic/everything/CNNshort16x24/finalServer/out'+str(x)+'.txt', 'rb') as f:
        finalText = f.read()
    forServer[x] = finalText
dictlist.append(forServer)

def showIndex(index):
    # original
    currentOriginalDictElement = dictlist[0].values()[index]
    # plt.imshow(currentOriginalDictElement)
    cv2.imshow('original',currentOriginalDictElement)

    # pixels
    currentPixelsDictElement = dictlist[1].values()[index]
    cv2.imshow('pixels',currentPixelsDictElement )

    # server
    currentServerDictElement = dictlist[2].values()[index]
    if connected:
    	print(currentServerDictElement)
        # channel.push("input",{"body": currentServerDictElement})

# ----------------------------------------  handle key presses

connected = True
try:
	socket = Socket("ws://dlevs.me:4000/socket")
	socket.connect()
	channel = socket.channel("room:lobby", {})
	channel.join()
except:
	print("can't do it")
	connected = False


index = 0
while True:
    k = cv2.waitKeyEx() & 0xFF
    print(k)
    if k == 121 and index < 37:
        index += 1
    elif k == 116 and index > 0:
        index -= 1
    else:
    	print('done')
    showIndex(index)