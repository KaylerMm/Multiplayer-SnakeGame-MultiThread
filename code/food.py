
import random

class Food:
    def __init__(self, dis_width, dis_height, snake_block):
        self.dis_width = dis_width
        self.dis_height = dis_height
        self.snake_block = snake_block
        self.new_food()

    def new_food(self):
        self.x = round(random.randrange(0, self.dis_width - self.snake_block) / 10.0) * 10.0
        self.y = round(random.randrange(0, self.dis_height - self.snake_block) / 10.0) * 10.0
