"""
================
RAG Thresholding
================

This example constructs a Region Adjacency Graph (RAG) and merges regions
which are similar in color. We construct a RAG and define edges as the
difference in mean color. We then join regions with similar mean color.
"""

from skimage import data, io, segmentation, color
from skimage.future import graph
from matplotlib import pyplot as plt
import os
from PIL import Image

path = 'in/'
expression = [fileName for fileName in os.listdir(path) if fileName[-4:] in [".png",".PNG", ".jpg", ".JPG"]]
for fileName in expression:
	imageName = os.path.splitext(fileName)[0]
	print('RAG running on %s' % imageName)
	img = io.imread(path+fileName)
	labels = segmentation.slic(img, compactness=10, n_segments=24 * 12)
	out = color.label2rgb(labels, img, kind='avg')

	plt.imsave('out/'+imageName+'.png', out)
	print('RAG finished on %s' % imageName)
	img = Image.open('out/'+imageName+'.png').convert('LA')
	print('converting %s to grayscale ' % imageName)
	img.save('out/'+imageName+'.png')
