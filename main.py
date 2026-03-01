import pygame

pygame.init()
WIDTH = 800
LENGTH = 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
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

    # перерисовать окно
    pygame.display.update()