import cv2
import numpy as np

def nothing(x):
    pass


drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
Color=(0,0,0)
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,Color

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),Color,2)
            else:
                cv2.circle(img,(x,y),5,Color,2)

    elif event == cv2.EVENT_LBUTTONUP:
        
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),Color,3)
        else:
            cv2.circle(img,(x,y),5,Color,3)
            
while True:            
    img=np.zeros((400,400,3), np.uint8)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    cv2.createTrackbar('R','image',0,255,nothing)
    cv2.createTrackbar('G','image',0,255,nothing)
    cv2.createTrackbar('B','image',0,255,nothing)


    switch = '0 : OFF \n1 : ON'
    cv2.createTrackbar(switch, 'image',0,1,nothing)



    while(1):
    
        r = cv2.getTrackbarPos('R','image')
        g = cv2.getTrackbarPos('G','image')
        b = cv2.getTrackbarPos('B','image')
        s = cv2.getTrackbarPos(switch,'image')
        Color=(r,g,b)
        if s==1:
            img=cv2.resize(cv2.imread("target.jpg"),(400,400))
#             org=img
        else:
            img=np.zeros((400,400,3), np.uint8)
#             org=img
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode
        elif k == 27:
            break

cv2.destroyAllWindows()