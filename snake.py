
import pygame

class Snake:
    def __init__(self, snake_block, init_x, init_y, player_id, colour):
        self.x = init_x
        self.y = init_y
        self.x_change = 0
        self.y_change = 0
        self.snake_block = snake_block
        self.snake_list = []
        self.length = 1
        self.player_id = player_id
        self.colour = colour

    def move(self):
        self.x += self.x_change
        self.y += self.y_change

    def change_direction(self, event):
        if self.player_id == 'P1':
            if event.key == pygame.K_LEFT and self.x_change == 0:
                self.x_change = -self.snake_block
                self.y_change = 0
            elif event.key == pygame.K_RIGHT and self.x_change == 0:
                self.x_change = self.snake_block
                self.y_change = 0
            elif event.key == pygame.K_UP and self.y_change == 0:
                self.y_change = -self.snake_block
                self.x_change = 0
            elif event.key == pygame.K_DOWN and self.y_change == 0:
                self.y_change = self.snake_block
                self.x_change = 0
                
        elif self.player_id == 'P2':
            if event.key == pygame.K_a and self.x_change == 0:
                self.x_change = -self.snake_block
                self.y_change = 0
            elif event.key == pygame.K_d and self.x_change == 0:
                self.x_change = self.snake_block
                self.y_change = 0
            elif event.key == pygame.K_w and self.y_change == 0:
                self.y_change = -self.snake_block
                self.x_change = 0
            elif event.key == pygame.K_s and self.y_change == 0:
                self.y_change = self.snake_block
                self.x_change = 0

    def update_snake(self):
        snake_head = [self.x, self.y]
        self.snake_list.append(snake_head)
        if len(self.snake_list) > self.length:
            del self.snake_list[0]

    def check_collision(self):
        snake_head = [self.x, self.y]
        for segment in self.snake_list[:-1]:
            if segment == snake_head:
                return False
        return False

    def draw(self, dis):
        for segment in self.snake_list:
            pygame.draw.rect(dis, self.colour, [segment[0], segment[1], self.snake_block, self.snake_block])
