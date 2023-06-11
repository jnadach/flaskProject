import random


class Square:
    def __init__(self):
        self.color = random.choice(["red", "green", "blue", "grey"])
        self.counter = 0
