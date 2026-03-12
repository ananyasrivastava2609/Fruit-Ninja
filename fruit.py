import random
import cv2


class Fruit:
    def __init__(self, width, height):
        self.x = random.randint(50, width - 50)
        self.y = 0
        self.radius = 25
        self.speed = random.randint(10, 15)

        # load fruit images
        self.images = [
            cv2.imread("assets/fruits/apple.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/banana.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/orange.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/grapes.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/avocado.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/dragonfruit.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/pineapple.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/kiwi.png", cv2.IMREAD_UNCHANGED),
            cv2.imread("assets/fruits/blueberry.png", cv2.IMREAD_UNCHANGED)
        ]
        
        # remove images that failed to load
        self.images = [img for img in self.images if img is not None]
        
        self.image = random.choice(self.images)

         # resize for display
        self.image = cv2.resize(self.image, (200, 200))

    def move(self):
        self.y += self.speed 

    def draw(self, frame):
        h, w, _ = self.image.shape

        x1 = int(self.x - w / 2)
        y1 = int(self.y - h / 2)
        x2 = x1 + w
        y2 = y1 + h

        # keep inside frame
        if x1 < 0 or y1 < 0:
            return

        roi = frame[y1:y2, x1:x2]
        
        if roi.shape[0] != h or roi.shape[1] != w:
            return
        
        fruit_rgb = self.image[:, :, :3]
        alpha = self.image[:, :, 3] / 255.0
        
        for c in range(3):
            roi[:, :, c] = (1 - alpha) * roi[:, :, c] + alpha * fruit_rgb[:, :, c]