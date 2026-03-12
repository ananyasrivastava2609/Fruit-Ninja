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
        cv2.circle(frame, finger, 10, (0,0,255), -1)

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

    cv2.putText(
        frame,
        f"Score: {score}",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        2
    )

    cv2.imshow("Hand Tracking Test", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()