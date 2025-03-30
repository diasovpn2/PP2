import pygame
import random
import time

# Начальная скорость змейки
snake_speed = 5

pygame.init()

# Размеры экрана
W, H = 720, 480
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake Game")

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128, 0, 128)

FPS = pygame.time.Clock()

# Начальные параметры змейки
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

# Функция генерации еды
food_list = []
def generate_food():
    return {
        "pos": [random.randrange(1, (W // 10)) * 10, random.randrange(1, (H // 10)) * 10],
        "value": random.randint(1, 3) * 10,  # Очки: 10, 20, 30
        "time": time.time()  # Время появления еды
    }

# Изначально создаем 3 еды
for _ in range(3):
    food_list.append(generate_food())

direction = "RIGHT"
change_to = direction

score = 0
count_food = 0

# Функция отображения счета
def show_score(color, font, size):
    score_font = pygame.font.Font(font, size)
    score_surf = score_font.render(f'Score: {score}', True, color)
    screen.blit(score_surf, (10, 10))

# Функция завершения игры
def game_over():
    my_font = pygame.font.Font("font_user.ttf", 30)
    game_over_surf = my_font.render(f"Your score is: {score}", True, RED)
    screen.blit(game_over_surf, (W // 4, H // 4))
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
            if event.key == pygame.K_UP:
                change_to = 'UP'
            elif event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # Запрет на разворот на 180 градусов
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Движение змейки
    if direction == 'UP':
        snake_pos[1] -= 10
    elif direction == 'DOWN':
        snake_pos[1] += 10
    elif direction == 'LEFT':
        snake_pos[0] -= 10
    elif direction == 'RIGHT':
        snake_pos[0] += 10

    snake_body.insert(0, list(snake_pos))

    # Проверка на съедание еды
    for food in food_list[:]:
        if snake_pos == food["pos"]:
            score += food["value"]
            count_food += 1
            food_list.remove(food)
            food_list.append(generate_food())
            break
    else:
        snake_body.pop()

    # Удаление еды через 5 секунд
    current_time = time.time()
    food_list = [food for food in food_list if current_time - food["time"] < 5]
    while len(food_list) < 3:
        food_list.append(generate_food())

    # Проверка выхода за границы
    if snake_pos[0] < 0 or snake_pos[0] > W - 10 or snake_pos[1] < 0 or snake_pos[1] > H - 10:
        game_over()
    
    # Проверка столкновения с собственным телом
    for block in snake_body[1:]:
        if snake_pos == block:
            game_over()

    # Увеличение скорости змейки
    if count_food == 4 and snake_speed < 24:
        snake_speed += 3
        count_food = 0

    # Отрисовка объектов
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, GREEN, pygame.Rect(pos[0], pos[1], 10, 10))
    for food in food_list:
        pygame.draw.rect(screen, RED, pygame.Rect(food["pos"][0], food["pos"][1], 10, 10))
    
    show_score(PURPLE, 'font_user.ttf', 20)
    pygame.display.update()
    FPS.tick(snake_speed)