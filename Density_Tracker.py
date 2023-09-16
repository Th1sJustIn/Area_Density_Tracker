
import numpy as np
import cv2
from tracker import *

peopleCount = 0


def Run_Code():
    global peopleCount

    ## Tracker object
    tracker = EuclideanDistTracker()


    cap = cv2.VideoCapture(0)

    # Object detection
    object_detector = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=20)

    while True:
        ret, frame = cap.read()
        height, width, _ = frame.shape
        if(peopleCount != tracker.currNum):
           peopleCount = tracker.currNum

        ## Region of Interest (roi)
        roi = frame[0 : 1080 , 0 : 1920]

        #mask
        mask = object_detector.apply(roi)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY)
        contours, _ =  cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        detections = []

        for cnt in contours:
            ##  Calculate area and remove walls
            area = cv2.contourArea(cnt)
            if area > 95000:
                # cv2.drawContours(roi, [cnt], -1, (0,255,0),2)
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(roi, (x,y), (x + w, y+h), (0,255,0), 8)

                detections.append([x,y,w,h])


        # Object Tracking

        boxes_ids = tracker.update(detections)

        cv2.putText(roi, f"Count: {tracker.currNum}", (10, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        for box_id in boxes_ids:
            x,y,w,h, id = box_id
            cv2.putText(roi, str(id), (x,y-15), cv2.FONT_HERSHEY_PLAIN, 5, (255,0,0), 0)
            cv2.rectangle(roi, (x,y), (x+w,y+h),(0,255,0), 3)

        #cv2.imshow('frame',frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("roi", roi)

        key = cv2.waitKey(30)


        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

