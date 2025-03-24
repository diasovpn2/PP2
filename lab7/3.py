<<<<<<< HEAD
import pygame
import sys
from pygame.locals import *
import random

pygame.init()
FPS = 60
FramePerSec = pygame.time.Clock()

W = (255, 255, 255)
B = (0, 0, 0)
R = (255, 0, 0)
G = (0, 255, 0)

widht = 400
hight = 600

DISPLAYSURF = pygame.display.set_mode((widht, hight))
DISPLAYSURF.fill(W)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, widht - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < widht and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player()
E1 = Enemy()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    P1.update()
    E1.move()

    DISPLAYSURF.fill(W)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
=======
import pygame
import os

pygame.init()
pygame.mixer.init()

playlist = [f for f in os.listdir() if f.endswith(".mp3")]
current_track = 0


def play_music(track):
    pygame.mixer.music.load(playlist[track])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[track]}")


if playlist:
    play_music(current_track)
else:
    print("No music files found in the folder.")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    print("Paused")
                else:
                    pygame.mixer.music.unpause()
                    print("Resumed")
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("Stopped")
            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(playlist)
                play_music(current_track)
            elif event.key == pygame.K_p:
                current_track = (current_track - 1) % len(playlist)
                play_music(current_track)

pygame.quit()
>>>>>>> e63b64598f430e27656b86c7e8b1691cb67dcf30
