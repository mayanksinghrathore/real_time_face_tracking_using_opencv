import cv2

cap = cv2.VideoCapture(0)
tracker = cv2.legacy.TrackerMOSSE_create()# opencv legacy is used for tracking
#tracker = cv2.legacy.TrackerCSRT_create()#trackercsrt is far more accurate than tracker moose however lags in speed
success, img = cap.read()
bBox = cv2.selectROI("Tracking", img, False)
tracker.init(img,bBox)

def drawBox(img,bBox):
    x,y,w,h = int(bBox[0]), int(bBox[1]), int(bBox[2]), int(bBox[3])# bBox is a tuple thus it can't be used directly.
    cv2.rectangle(img,(x,y),((x+w),(y+h)),(255,0,255),3,1) #bBox has 4 values.
    cv2.putText(img,"Tracking",(75,75),cv2.FONT_HERSHEY_SIMPLEX,0.7,(100,20,80),2)


while True:
    timer = cv2.getTickCount()
    success, img = cap.read()

    success,bBox = tracker.update(img)

    if success:
        drawBox(img,bBox)
    else:
        cv2.putText(img, "Lost", (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    fps = cv2.getTickFrequency()/(cv2.getTickCount()-timer)
    cv2.putText(img,str(int(fps)),(75,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
    cv2.imshow("Tracking",img)

    if cv2.waitKey(1) & 0xff == ord('q'):
       break
