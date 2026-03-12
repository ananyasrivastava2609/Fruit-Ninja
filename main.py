import cv2
import math
import random
from hand_tracker import HandTracker
from fruit import Fruit

cap = cv2.VideoCapture(0)

tracker = HandTracker()
fruits = []
frame_count = 0
score = 0
missed = 0
trail_points = [] 


while True:

    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    frame_count += 1

    # spawn fruit
    if frame_count % 17 == 0:
        height, width, _ = frame.shape
        fruits.append(Fruit(width, height))
        print(len(fruits))

    finger = tracker.get_finger_position(frame)

    if finger:
        trail_points.append(finger)

        if len(trail_points) > 10:
            trail_points.pop(0)

    else:
        trail_points.clear()

    for i in range(1, len(trail_points)):
        cv2.line(frame, trail_points[i-1], trail_points[i], (255, 0, 0), 5)

    # move and draw fruits
    for fruit in fruits[:]:
        fruit.move()
        
        fruit.draw(frame)

        if finger:
            fx, fy = finger
            distance = math.hypot(fx - fruit.x, fy - fruit.y)

            if distance < fruit.radius:
                fruits.remove(fruit)
                score += 1
                print("Fruit sliced! Score:", score)

        # remove fruits that fall off screen
        if fruit.y - fruit.radius > frame.shape[0]:
            fruits.remove(fruit)
            missed += 1
            print("Missed a fruit! Missed:", missed)

    cv2.putText(frame, f"Score: {score}", (10,40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.putText(frame, f"Missed: {missed}", (10,80),
            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)



    cv2.imshow("Hand Tracking Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()