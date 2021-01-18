import pygame
import random


class Enemy(pygame.sprite.Sprite):

    isLeft = False

    def __init__(self, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        gen = random.randint(0, 1)
        if gen == 0:
            self.rect.left = 105
            self.isLeft = True
        else:
            self.rect.left = 205
            self.isLeft = False
        self.rect.top = 0

