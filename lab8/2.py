import pygame
import random
import time

# Начальная скорость
snake_speed = 5

pygame.init()

W, H = 720, 480

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)

pygame.display.set_caption("Snake Game")
screen = pygame.display.set_mode((W, H))

clock = pygame.time.Clock()  

snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

fruit_pos = [random.randrange(1, (W // 10)) * 10, random.randrange(1, (H // 10)) * 10]
fruit_spawn = True

direction = "RIGHT"
change_to = direction
score = 0
count_food = 0  # Счетчик съеденных фруктов

# Функция отображения счета
def show_score(color, size):
    score_font = pygame.font.Font(None, size)  # Используем встроенный шрифт
    score_surf = score_font.render(f'Score: {score}', True, color)
    score_rect = score_surf.get_rect(topleft=(10, 10))
    screen.blit(score_surf, score_rect)

# Функция завершения игры
def game_over():
    my_font = pygame.font.Font(None, 30)
    game_over_surf = my_font.render(f"Your score: {score}", True, RED)
    game_over_rect = game_over_surf.get_rect(center=(W // 2, H // 2))
    screen.blit(game_over_surf, game_over_rect)
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

# Игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
    
    # Движение змейки
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    
    snake_body.insert(0, list(snake_pos))

    # Проверка на поедание фрукта
    if snake_pos == fruit_pos:
        score += 10
        count_food += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (W // 10)) * 10, random.randrange(1, (H // 10)) * 10]
    
    fruit_spawn = True
    screen.fill(BLACK)

    # Отрисовка змейки
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, RED, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    # Проверка выхода за границы
    if snake_pos[0] < 0 or snake_pos[0] >= W or snake_pos[1] < 0 or snake_pos[1] >= H:
        game_over()
    
    # Проверка на столкновение с самим собой
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Увеличение скорости после каждых 4 фруктов
    if count_food == 4 and snake_speed < 24:
        snake_speed += 3
        count_food = 0

    show_score(PURPLE, 20)
    pygame.display.update()
    clock.tick(snake_speed)  
