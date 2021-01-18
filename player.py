import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, filename, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self, location):
        self.rect.left, self.rect.top = location
