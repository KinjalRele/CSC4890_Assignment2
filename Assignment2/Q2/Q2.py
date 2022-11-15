import numpy as np
import cv2

imgPath=["Test1/testLeft.jpg","Test1/testCenter.jpg","Test1/testRight.jpg"]

imgPath2=["Test2/store1.jpg","Test2/store2.jpg","Test2/store3.jpg"]

imgPath3=["Test3/store5.jpg" ,"Test3/store6.jpg","Test3/store7.jpg"]

imgPath4=["Test4/Scenter1.jpg" , "Test4/Scenter2.jpg" , "Test4/Scenter3.jpg"]

imgPath5=["Test5/ulife1.jpg" , "Test5/ulife2.jpg" , "Test5/ulife3.jpg"]

images = []

for path in imgPath5:
	image = cv2.imread(path)
	images.append(image)

print(len(images))
stitcher = cv2.Stitcher_create()
(status, stitched) = stitcher.stitch(images)

if status == 0:
	print("Image Stitching Successful")
	cv2.imshow("Stitched Image", stitched)
	cv2.imwrite("Q2stichedImage5.png",stitched)
	cv2.waitKey(0)
else:
	print("[INFO] Failed Image Stitching ({})"/format(status))
