import pygame
import vars as v
import defs as d

pygame.init()
screen = pygame.display.set_mode((v.WID, v.HEI))
running = True
clock = pygame.time.Clock()
x, y = v.WID / 2, v.HEI / 2

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    x, y = d.movement(keys, x, y)
    x, y = d.barrier(x, y)

    screen.fill(v.BLACK)
    pygame.draw.circle(screen, v.WHITE, (int(x), int(y)), v.RAD)
    pygame.display.flip()
    clock.tick(60)