import pygame
from random import randint
pygame.init()
WIDTH = 800
LENGTH = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
x = randint(0, WIDTH - 1)
y = randint(0, LENGTH - 1)
x1 = randint(0, WIDTH - 1)
y1 = randint(0, WIDTH - 1)
x2 = randint(0, WIDTH - 1)
y2 = randint(0, WIDTH - 1)
x3 = randint(0, WIDTH - 1)
y3 = randint(0, WIDTH - 1)
SIZE = 50
# создаем окно размера 800 на 600
screen = pygame.display.set_mode((WIDTH,LENGTH))
screen.fill(pygame.Color(WHITE))

# указываем название
pygame.display.set_caption("Snake")

# игровой цикл
while True:
    # обрабатываем события
    for e in pygame.event.get():
        # если нажали на крестик
        if e.type == pygame.QUIT:
            # закрыть окно
            raise SystemExit("QUIT")
    pygame.draw.circle(screen, (255, 0 , 0), (x, y), 10)
    pygame.draw.rect(screen, (255,165,0), (x1, y2, 50,50))
    pygame.draw.circle(screen, (0, 0, 255), (x2, y2), 10)
    pygame.draw.circle(screen, (139,0,255), (x3, y3), 10)
    # перерисовать окно
    pygame.display.update()