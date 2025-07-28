#Coded with gpt help
import pygame
import time
import random

pygame.init()

# Game window
width, height = 600, 800
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (213, 50, 80)
green = (0, 255, 0)

# Snake settings
snake_block = 10
snake_speed = 10
clock = pygame.time.Clock()

font = pygame.font.SysFont("Arial", 25)

def draw_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], snake_block, snake_block])

def game_loop():
    game_over = False
    x, y = width // 2, height // 2
    dx, dy = 0, 0
    snake_list = []
    length = 1

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx, dy = -snake_block, 0
                elif event.key == pygame.K_RIGHT:
                    dx, dy = snake_block, 0
                elif event.key == pygame.K_UP:
                    dx, dy = 0, -snake_block
                elif event.key == pygame.K_DOWN:
                    dx, dy = 0, snake_block

        x += dx
        y += dy

        if x < 0 or x >= width or y < 0 or y >= height:
            break  # hit wall

        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, snake_block, snake_block])

        snake_head = [x, y]
        snake_list.append(snake_head)
        if len(snake_list) > length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True  # hit self

        draw_snake(snake_list)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    time.sleep(2)
    pygame.quit()

game_loop()
