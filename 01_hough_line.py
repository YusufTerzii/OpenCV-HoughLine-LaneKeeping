import cv2
import numpy as np
 

original = cv2.imread ("06_Hough_Transforms/resimler/h_line.png")
img = cv2.imread ("06_Hough_Transforms/resimler/h_line.png")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,75,150)

lines = cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap = 200)##Filling the gaps with maxlinegap

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

cv2.imshow("org",original)
cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

