import vars as v
import pygame
def movement(keys):
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        v.y -= v.SPEED
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        v.x -= v.SPEED
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        v.y += v.SPEED
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            v.x += v.SPEED
def barrier():
    if v.x < v.RAD:
        v.x = v.RAD
    if v.x > v.WID - v.RAD:
        v.x = v.WID - v.RAD
    if v.y < v.RAD:
        v.y = v.RAD
    if v.y > v.HEI - v.RAD:
        v.y = v.HEI - v.RAD