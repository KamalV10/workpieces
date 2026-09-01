import pygame
import vars as v
class Player():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= v.SPEED
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= v.SPEED            
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += v.SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += v.SPEED
    def barrier(self):
        if self.x < v.RAD:
            self.x = v.RAD
        if self.x > v.WID - v.RAD:
            self.x = v.WID - v.RAD
        if self.y < v.RAD:
            self.y = v.RAD
        if self.y > v.HEI - v.RAD:
            self.y = v.HEI - v.RAD