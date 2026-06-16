# Source - https://stackoverflow.com/a/11449901
# Posted by sastanin, modified by community. See post 'Timeline' for change history
# Retrieved 2026-06-15, License - CC BY-SA 3.0

import cv2

cv2.namedWindow("Webcam")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("Webcam", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

cv2.destroyWindow("Webcam")
vc.release()
