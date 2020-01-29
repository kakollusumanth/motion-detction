import cv2
import numpy as np
cap=cv2.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()
#diff=cv2.absdiff(frame1,frame2)


#print(gray)

#cv2.imshow(gray)
while cap.isOpened():
    #ret,frame=cap.read()
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x,y,w,h)=cv2.boundingRect(contour)
        if cv2.contourArea(contour)<1400:
            continue
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,255,0),4)
        cv2.putText(frame1,'status: {}'.format('Movement'),(10,20),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,2550),3)

        #cv2.drawContours(frame1,contours,-1,(255,255,0),2)
    cv2.imshow('feed',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    
    #cv2.absdiff(frame1,frame2)
    #cv2.imshow('fr',)
    if cv2.waitKey(10)==27:#escape
        break
cv2.destroyAllWindows()
cap.release()
