import sys

import cv2
import numpy as np

# Read image
# im_in = cv2.imread("out/screenshot_pixelated.png", cv2.IMREAD_GRAYSCALE);
filename = sys.argv[1]
filename_parts = filename.rsplit('.', 1)
im_in = cv2.imread(filename, cv2.IMREAD_GRAYSCALE);
# cv2.imwrite('out/screenshot_pixelated_gray.png', im_in)
cv2.imwrite(str(filename_parts[0])+'_gray.png', im_in)

th, im_th = cv2.threshold(im_in, 255, 255, cv2.THRESH_TOZERO_INV);
 
# Copy the thresholded image.
im_floodfill = im_th.copy()
 
# Mask used to flood filling.
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)
 
# Floodfill from point (0, 0)
cv2.floodFill(im_floodfill, mask, (0,0), 255);
 
# Invert floodfilled image
im_floodfill_inv = cv2.bitwise_not(im_floodfill)
# Save
# cv2.imwrite('out/screenshot_pixelated_gray_inverted.png', im_floodfill_inv)
cv2.imwrite(str(filename_parts[0])+'_gray_inverted.png', im_floodfill_inv)
