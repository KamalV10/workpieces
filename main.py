import pygame
import vars as v
pygame.init()
screen = pygame.display.set_mode((v.WID, v.HEI))
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        v.y -= v.SPEED
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        v.x -= v.SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        v.y += v.SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        v.x += v.SPEED

    if v.x < v.RAD:
        v.x = v.RAD
    if v.x > v.WID - v.RAD:
        v.x = v.WID - v.RAD

    screen.fill(v.BLACK)
    pygame.draw.circle(screen, v.WHITE, (v.x, v.y), v.RAD)
    pygame.display.flip()
    clock.tick(60)