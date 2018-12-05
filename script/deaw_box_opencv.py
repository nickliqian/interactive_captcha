# -*- coding: UTF-8 -*-
import cv2

imgpath = "wangyi_data/JPEGImages/100000.jpg"
img = cv2.imread(imgpath)
print(img.shape)
cv2.rectangle(img, (90, 38), (124, 72), (0, 255, 0), 1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
