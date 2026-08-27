import pygame
import vars as v
pygame.init()
screen = pygame.display.set_mode((v.WID, v.HEI))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(v.BLACK)
    clock.tick(60)
    pygame.draw.circle((v.YELLOW), (v.x, v.y), v.RAD)