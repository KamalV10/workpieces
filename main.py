import pygame
import vars as v
import classes as c

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
    player = c.Player(x, y)
    player.movement()
    player.barrier()
    x, y = player.x, player.y
    screen.fill(v.BLACK)
    pygame.draw.circle(screen, v.WHITE, (int(x), int(y)), v.RAD)
    pygame.display.flip()
    clock.tick(60)