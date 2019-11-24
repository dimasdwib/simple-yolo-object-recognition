from darkflow.net.build import TFNet
import numpy as np
import time
import cv2

option = {
   'model': './cfg/yolo.cfg',
   'load': './bin/yolo.weights',
   'threshold': 0.55
}

tfnet = TFNet(option)

# video source
cap = cv2.VideoCapture('./sample_video/indo_1.mp4')

while(cap.isOpened()):
   ret, frame = cap.read()

   img = frame # cv2.imread('../sample/sample2.jpg', cv2.IMREAD_COLOR)
   result = tfnet.return_predict(img)

   for obj in result:
      tl = (obj['topleft']['x'], obj['topleft']['y'])
      br = (obj['bottomright']['x'], obj['bottomright']['y'])
      conf = round(float(obj['confidence']) * 100, 2)
      label = obj['label']
      label = f'{label} {conf}%'

      # prediction result      
      print(obj)

      img = cv2.rectangle(img, tl, br, (0, 255, 255), 1)
      img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

      # show frames 
      cv2.imshow('frame', img)

   if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
