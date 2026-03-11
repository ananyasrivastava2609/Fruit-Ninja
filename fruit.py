import random
import cv2

class Fruit:
    def __init__(self, width, height):
        self.x = random.randint(50, width - 50)
        self.y = 0
        self.radius = 25
        self.speed = random.randint(10, 15)

    def move(self):
        self.y += self.speed

    def draw(self, frame):
        cv2.circle(frame, (self.x, self.y), self.radius, (0,255,0), -1)