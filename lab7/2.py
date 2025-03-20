import pygame
from datetime import datetime
import math
pygame.init()

weight, height = 600, 400
H_weight, H_height = weight // 2, height // 2
rad = H_height - 50

screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('di')
clock = pygame.time.Clock()

bg = pygame.image.load("bg.png")
bg = pygame.transform.scale(bg, (600, 400))

hour_hand = pygame.image.load("min.png")
minute_hand = pygame.image.load("sec.png")

def draw_rotated_image(image, angle, position, offset_x=0, offset_y=0):
    rotated_image = pygame.transform.rotate(image, -angle)
    rect = rotated_image.get_rect(center=(position[0] + offset_x, position[1] + offset_y))
    screen.blit(rotated_image, rect.topleft)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    t = datetime.now()
    hour, minute, second = t.hour % 12, t.minute, t.second

    screen.blit(bg, (0, 0))

    draw_rotated_image(hour_hand, minute * 6, (H_weight, H_height), offset_x=10)  # Смещение минутной стрелки вправо
    draw_rotated_image(minute_hand, second * 6, (H_weight, H_height))

    pygame.display.flip()
    clock.tick(20)
