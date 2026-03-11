import cv2
from hand_tracker import HandTracker

cap = cv2.VideoCapture(0)

tracker = HandTracker()

while True:

    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    finger = tracker.get_finger_position(frame)

    if finger:
        cv2.circle(frame, finger, 10, (0,0,255), -1)

    cv2.imshow("Hand Tracking Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()