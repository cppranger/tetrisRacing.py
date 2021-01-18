import random
import pygame

from player import Player
from enemy import Enemy
from background import Background


def gameOver():
    window.fill(WHITE)
    player1.kill()
    enemy1.kill()
    bg.kill()
    pygame.display.flip()
    font = pygame.font.SysFont('comicsansms', 24)
    text = "GAME IS OVER. Your score is " + str(score)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (width // 2, height // 2)
    window.blit(text_surface, text_rect)
    pygame.display.flip()


def drawText(text):
    font = pygame.font.SysFont('comicsansms', 24)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (width // 2, height - 50)
    window.blit(text_surface, text_rect)
    pygame.display.flip()


pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
width, height = 400, 400
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 150
running = True
pos_left = 105
pos_right = 205
score = 0
pygame.mixer.music.load('sound/music.mp3')
boom = pygame.mixer.Sound('sound/boom.mp3')

speed = 1
player1 = Player('img/player.png', [pos_right, height - 200])
enemy1 = Enemy('img/enemy.png')
bg = Background('img/bg.png', [0, 0])

pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill(WHITE)
    window.blit(bg.image, bg.rect)
    window.blit(player1.image, player1.rect)
    window.blit(enemy1.image, enemy1.rect)
    str_score = "Your score:" + str(score)
    drawText(str_score)
    pygame.display.update()

    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player1.move([pos_right, height - 200])
                player1.isLeft = False
            elif event.key == pygame.K_LEFT:
                player1.move([pos_left, height - 200])
                player1.isLeft = True
            elif event.key == pygame.K_SPACE:
                if player1.isLeft:
                    player1.move([pos_right, height - 200])
                    player1.isLeft = False
                else:
                    player1.move([pos_left, height - 200])
                    player1.isLeft = True
            elif event.key == pygame.K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            exit()
    if enemy1.rect.y >= 100 and (enemy1.isLeft == player1.isLeft):
        pygame.mixer.music.pause()
        boom.play()
        running = False
        break
    elif enemy1.rect.y < height - 200:
        enemy1.rect.y += speed
    else:
        if random.randint(0, 1) == 0:
            enemy1.rect.left = 105
            enemy1.rect.y = 0
            enemy1.isLeft = True
        else:
            enemy1.rect.left = 205
            enemy1.rect.y = 0
            enemy1.isLeft = False
        score += 1
        if fps < 250:
            fps += 10
        elif fps < 300:
            fps += 5
        else:
            fps += 1
gameOver()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()
        elif event.type == pygame.QUIT:
            exit()
