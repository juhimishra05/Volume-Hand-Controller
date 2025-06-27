import math
import cv2 
import time
import numpy as np 
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from handTrackingModule import HandDetector

wCam,hCam = 640,480 




capture = cv2.VideoCapture(0)
capture.set(3,wCam)
capture.set(4,hCam)

pTime  = 0 

detector = HandDetector(maxHands=1)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

volRange = volume.GetVolumeRange()
newVolume = 0 
newVolumeBar = 400
newVolumePercentage = 0

minVolume = volRange[0]
maxVolume = volRange[1]



while True: 
    success,img = capture.read()
    img =  detector.findHands(img)
    
    lmList = detector.findPostition(img,draw=False)
    if len(lmList) !=0:
        x1,y1 = lmList[4][1],lmList[4][2]
        x2,y2 = lmList[8][1],lmList[8][2]
        x3,y3 = lmList[12][1],lmList[12][2]
        
        cx,cy = (x1+x2)//2,(y1+y2)//2
         
        cv2.circle(img, (x1,y1),12,(255,0,255),cv2.FILLED)
        cv2.circle(img, (x2,y2),12,(255,0,255),cv2.FILLED)
        cv2.circle(img, (cx,cy),12,(255,0,255),cv2.FILLED)
        cv2.line(img, (x1,y1),(x2,y2),(255,0,255),3)
        
        length= math.hypot(x2-x1,y2-y1)
        
        if length<50:
            cv2.circle(img, (cx,cy),12,(0,255,0),cv2.FILLED)
        #  Volume functionality will only work when middle finger is open
        if y3<y2:
            newVolume = np.interp(length,[50,300],[minVolume,maxVolume])
            newVolumeBar = np.interp(length,[50,300],[400,150])
            newVolumePercentage = np.interp(length,[50,300],[0,100])
            # Setting master volume
            print(f"Volume:{newVolume}")
            volume.SetMasterVolumeLevel(newVolume, None)
    
    cv2.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv2.rectangle(img,(50,int(newVolumeBar)),(85,400),(0,255,0),cv2.FILLED)
    cv2.putText(img, f"{int(newVolumePercentage)}%", (40,450),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
        
    
    
    
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,f"FPS: {int(fps)}",(20,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
    cv2.imshow("Hand Track volume",img)
    cv2.waitKey(1)
