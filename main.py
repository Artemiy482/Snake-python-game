import random

import pygame
from random import randint, randrange

pygame.init()
WIDTH = 1280
LENGTH = 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
BlACK = (0,0,0)
SIZE = 20


# создаем окно размера 800 на 600
screen = pygame.display.set_mode((WIDTH,LENGTH))
screen.fill(pygame.Color(WHITE))
clock = pygame.time.Clock()
speed = 40
# указываем название
pygame.display.set_caption("Snake")
#Добавляем змею
x1 = WIDTH // 2
y1 = LENGTH // 2
x2 = (random.randrange(0, WIDTH - 1,SIZE) + 10) % WIDTH
y2 = (random.randrange(0, LENGTH- 1,SIZE) + 10) % LENGTH
pygame.draw.rect(screen, (255, 165, 0), (x1, y1,SIZE,SIZE))
direction = 'right'
snake = [[x1,y1],[x1-20,y1],[x1-40,y1]]
#Добавляем еду
def draw_food():
    pygame.draw.circle(screen, (0, 0, 255), (x2, y2), 10)


def drawGrid():
    blockSize = SIZE #Set the size of the grid block
    for x in range(0, WIDTH, blockSize):
        for y in range(0, LENGTH, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BlACK, rect, 1)



def draw_snake():
    for i in range(len(snake)):
        pygame.draw.rect(screen, (255, 165, 0), (snake[i][0],snake[i][1], SIZE, SIZE))
# игровой цикл
while True:
    # обрабатываем события

    for event in pygame.event.get():
        # если нажали на крестик
        if event.type == pygame.QUIT:
            raise SystemExit("QUIT")
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            direction = 'up'
        elif keys[pygame.K_DOWN]:
            direction = 'down'
        elif keys[pygame.K_LEFT]:
            direction = 'left'
        elif keys[pygame.K_RIGHT]:
            direction = 'right'
    rock = snake[0][1]
    stone = snake[0][0]
    if direction == 'up':
        rock -= SIZE
    elif direction == 'down':
        rock  += SIZE
    elif direction == 'left':
        stone -= SIZE
    elif direction == 'right':
        stone += SIZE
    for el in range(len(snake)-1,0,-1):
        snake[el][0] = snake[el - 1][0]
        snake[el][1] = snake[el - 1][1]

    snake[0][0] = stone % WIDTH
    snake[0][1] = rock % LENGTH
    if y2 == snake[0][1] + SIZE / 2 and x2 == snake[0][0] + SIZE / 2:
        x2 = (random.randrange(0, WIDTH - 1, SIZE) + 10) % WIDTH
        y2 = (random.randrange(0, LENGTH - 1, SIZE) + 10) % LENGTH
        snake.append([snake[-1][0],snake[-1][1]])

    screen.fill(WHITE)
    drawGrid()
    draw_food()

    draw_snake()
    pygame.display.update()
    clock.tick(speed)
