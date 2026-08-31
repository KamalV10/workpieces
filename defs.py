import vars as v
import pygame
def movement(keys, x, y):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= v.SPEED
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= v.SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += v.SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            x += v.SPEED
    return(x, y)

def barrier(x, y):
    if x < v.RAD:
        x = v.RAD
    if x > v.WID - v.RAD:
        x = v.WID - v.RAD
    if y < v.RAD:
        y = v.RAD
    if y > v.HEI - v.RAD:
        y = v.HEI - v.RAD
    return(x, y)