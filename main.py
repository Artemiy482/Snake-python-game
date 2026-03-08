import pygame
from random import randint
pygame.init()
WIDTH = 1280
LENGTH = 720
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)

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
pygame.draw.rect(screen, (255, 165, 0), (x1, y1,SIZE,SIZE))
direction = 'right'
snake = [[x1,y1],[x1-20,y1],[x1-40,y1]]
#Добавляем еду
def draw_food():
    x2 = randint(0, WIDTH - 1)
    y2 = randint(0, WIDTH - 1)
    pygame.draw.circle(screen, (0, 0, 255), (x2, y2), 10)


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
    snake[0][0] = snake[0][0] % WIDTH
    snake[0][1] = snake[0][1] % LENGTH



    screen.fill(WHITE)
    draw_snake()
    pygame.display.update()
    clock.tick(speed)
