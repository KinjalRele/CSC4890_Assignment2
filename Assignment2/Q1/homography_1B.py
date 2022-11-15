import cv2
import numpy as np
import matplotlib.pyplot as plt

src_points = np.array([[1218,860],[1041,850],[1229,340],[1054,318],[1498,973] ])
dest_points = np.array([[1028,117],[1208,114],[1019,691],[1202,702],[809,681]])


h, status = cv2.findHomography(src_points, dest_points)
print(h)
im_src = cv2.imread('leftImg.png')
im_dst = cv2.imread('midImg.png')

im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1],im_dst.shape[0]))

cv2.imshow("Warped_Source_Image", im_out)
plt.imshow(im_out)
plt.show()

#
#LEFT IMG COORDINATES
#1218   860
#1041   850
#1229   340
#1054   318
#1498   873

#MID IMG COORDINATES
#1028   117
#1208   144
#1019   691
#1202   702
# 809   681




