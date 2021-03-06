import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

### EXAMPLES ###

# Load in gray scale
img = cv2.imread('1_opencv.jpg', 0)

# Show image
# cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# cv2.imshow('1_opencv.jpg', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Display with Matplotlib
# plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
# plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
# plt.show()

# Writes gray scale image load
# cv2.imwrite('1_opencv_gray.jpg', 0)
# cv2.destroyAllWindows()

# Merge gray scale image with color and export, it needs to be same dimension
# img2 = cv2.imread('1_opencv_gray.jpg')
# dst = cv2.addWeighted(img, 0.7, img2, 0.3, 0)
# cv2.imshow('dst', dst)
# cv2.destroyAllWindows()

# Accessing only blue pixel
# blue = img[100, 100, 0]
# print (blue)

# Accessing info
# print (img.shape)
# print (img.size)

##########
## GOAL ##
##########

# NOTE # It doesn't seem like you can change the aperture in OpenCV
# NOTE # Aperture settings are probably only during the actual photo shoot
# NOTE # Try Histograms Equalization in OpenCV

# Write example

# Aperture settings are not in OpenCV (at least from my research),
# Try using Histograms examples

equ = cv2.equalizeHist(img)
res = np.hstack((img, equ))
cv2.imwrite('exports/equalize_opencv.png', res)

# 1. Change the image aperture +1
# a. Export to JPG
cv2.imwrite('exports/aperture_plus_1.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
# b. Export to PNG
cv2.imwrite('exports/aperture_plus_1.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 9])

#2. Change the image aperture +2
# a. Export to JPG
cv2.imwrite('exports/aperture_plus_2.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
# b. Export to PNG
cv2.imwrite('exports/aperture_plus_2.png', img)

#3. Change the image aperture -1
# a. Export to JPG
cv2.imwrite('exports/aperture_minus_1.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
# b. Export to PNG
cv2.imwrite('exports/aperture_minus_1.png', img)

#4. Change the image apeture -2
# a. Export to JPG
cv2.imwrite('exports/aperture_minus_2.jpg', img, [int(cv2.IMWRITE_JPEG_QUALITY), 90])
# b. Export to PNG
cv2.imwrite('exports/aperture_minus_2.png', img)
