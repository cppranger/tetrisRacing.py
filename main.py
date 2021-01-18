import pygame
from player import Player
from enemy import Enemy
from background import Background

pygame.init()
WHITE = (255, 255, 255)
width, height = 400, 800
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60
running = True
pos_left = 105
pos_right = 205

speed = 1
player1 = Player('img/player.png', [pos_right, height - 200])
enemy1 = Enemy('img/enemy.png')
bg = Background('img/bg.png', [0, 0])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill(WHITE)
    window.blit(bg.image, bg.rect)
    window.blit(player1.image, player1.rect)
    window.blit(enemy1.image, enemy1.rect)
    pygame.display.update()

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1.move([pos_right, height - 200])
            elif event.key == pygame.K_LEFT:
                player1.move([pos_left, height - 200])
            elif event.key == pygame.K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            exit()
    if enemy1.rect.y < height - 200:
        enemy1.rect.y += speed
    else:
        enemy1.rect.y = 0
