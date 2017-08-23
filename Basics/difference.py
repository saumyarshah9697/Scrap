import cv2

i1=cv2.imread("0.jpeg")
i2=cv2.imread("1.jpeg")

img1=cv2.cvtColor(i1,cv2.IMREAD_GRAYSCALE)
img2=cv2.cvtColor(i2,cv2.IMREAD_GRAYSCALE)

ret,im=cv2.threshold(img1,100,255,cv2.THRESH_BINARY_INV)
ret,im2=cv2.threshold(img2,100,255,cv2.THRESH_BINARY_INV)

cv2.imshow("frame",cv2.bitwise_and(img1,img2))
# cv2.imshow("framee2",cv2.subtract(img2,img1))
k=cv2.waitKey(0)& 0xFF
if(k==ord('q')):
    cv2.destroyAllWindows()
    
