
import pygame
import threading
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        pygame.init()
        
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)

        self.dis_width = 1000
        self.dis_height = 600

        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake Game with Multithreading')

        self.clock = pygame.time.Clock()
        self.snake_block = 10
        self.snake_speed = 15

        self.font_style = pygame.font.SysFont("", 50)

        self.snakes = [
                        Snake(self.snake_block, 100, 300, 'P1', self.black), 
                        Snake(self.snake_block, 700, 300, 'P2', self.white),
                    ]
        self.scores = [0, 0]
        self.food = Food(self.dis_width, self.dis_height, self.snake_block)

    def score(self, scores):
        value1 = self.font_style.render("Player 1 Score: " + str(scores[0]), True, self.black)
        self.dis.blit(value1, [0, 0])
        value2 = self.font_style.render("Player 2 Score: " + str(scores[1]), True, self.black)
        self.dis.blit(value2, [0, 30])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def gameLoop(self):
        game_over = False
        game_close = False
        
        

        def move_snake(snake):
            nonlocal game_over, game_close
            while not game_over:
                if game_close:
                    break
                snake.move()
                if snake.x >= self.dis_width or snake.x < 0 or snake.y >= self.dis_height or snake.y < 0:
                    game_close = True
                pygame.time.wait(100)

        # Threads das cobras
        threads = [threading.Thread(target=move_snake, args=(self.snakes[i],)) for i in range(2)]
        for thread in threads:
            thread.start()

            
        while not game_over:
            while game_close:
                self.dis.fill(self.blue)
                self.message("Game Over! Press Q to Quit or P to Play Again", self.red)
                self.score(self.scores)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_p:
                            self.__init__()
                            self.gameLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                        self.snakes[0].change_direction(event)
                    if event.key in [pygame.K_a, pygame.K_d, pygame.K_w, pygame.K_s]:
                        self.snakes[1].change_direction(event)

            for i, snake in enumerate(self.snakes):
                if snake.x == self.food.x and snake.y == self.food.y:
                    self.food.new_food()
                    snake.length += 1
                    self.scores[i] += 1

            self.dis.fill(self.blue)
            pygame.draw.rect(self.dis, self.green, [self.food.x, self.food.y, self.snake_block, self.snake_block])
            for snake in self.snakes:
                snake.update_snake()
                if snake.check_collision():
                    game_close = True
                snake.draw(self.dis)
            self.score(self.scores)

            pygame.display.update()
            self.clock.tick(self.snake_speed)

        quit()
