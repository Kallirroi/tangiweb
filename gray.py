from skimage import data, io, segmentation, color
from skimage.future import graph
from matplotlib import pyplot as plt
import os
from PIL import Image
from collections import defaultdict
import operator

path = 'out/'
expression = [fileName for fileName in os.listdir(path) if fileName[-4:] in [".png",".PNG", ".jpg", ".JPG"]]
for fileName in expression:
	imageName = os.path.splitext(fileName)[0]
	img_gray= Image.open(path+imageName+'.png').convert('LA')
	print('converting %s to grayscale ' % imageName)
	img_gray.save('out/'+imageName+'_gray.png')
	print('done')