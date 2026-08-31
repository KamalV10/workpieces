import pygame
import vars as v
import defs as d
pygame.init()
screen = pygame.display.set_mode((v.WID, v.HEI))
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    d.movement(keys)
    d.barrier()
    screen.fill(v.BLACK)
    pygame.draw.circle(screen, v.WHITE, (v.x, v.y), v.RAD)
    pygame.display.flip()
    clock.tick(60)