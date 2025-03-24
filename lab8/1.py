import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Параметры игрока
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - 2 * player_size]
player_speed = 8

# Параметры врагов
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 5

# Параметры монет
coin_size = 30
coin_pos = [random.randint(0, WIDTH - coin_size), 0]
coins_collected = 0

# FPS
clock = pygame.time.Clock()

# Шрифт для отображения очков
font = pygame.font.SysFont("monospace", 35)

def detect_collision(obj1_pos, obj1_size, obj2_pos, obj2_size):
    """Проверка столкновения между двумя объектами."""
    return (obj1_pos[0] < obj2_pos[0] < obj1_pos[0] + obj1_size or
            obj2_pos[0] < obj1_pos[0] < obj2_pos[0] + obj2_size) and \
           (obj1_pos[1] < obj2_pos[1] < obj1_pos[1] + obj1_size or
            obj2_pos[1] < obj1_pos[1] < obj2_pos[1] + obj2_size)

# Основной игровой цикл
running = True
while running:
    screen.fill(BLACK)

    # Проверка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed

    # Движение врага
    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]

    # Движение монеты
    coin_pos[1] += enemy_speed
    if coin_pos[1] > HEIGHT:
        coin_pos = [random.randint(0, WIDTH - coin_size), 0]

    # Проверка столкновений
    if detect_collision(player_pos, player_size, enemy_pos, enemy_size):
        print("Game Over!")
        running = False

    if detect_collision(player_pos, player_size, coin_pos, coin_size):
        coins_collected += 1
        coin_pos = [random.randint(0, WIDTH - coin_size), 0]  # Появление новой монеты

    # Рисование объектов
    pygame.draw.rect(screen, RED, (*player_pos, player_size, player_size))
    pygame.draw.rect(screen, WHITE, (*enemy_pos, enemy_size, enemy_size))
    pygame.draw.circle(screen, (255, 215, 0), (coin_pos[0] + coin_size // 2, coin_pos[1] + coin_size // 2), coin_size // 2)

    # Отображение количества собранных монет
    score_text = font.render(f"Coins: {coins_collected}", True, WHITE)
    screen.blit(score_text, (WIDTH - 200, 10))

    # Обновление экрана
    pygame.display.flip()

    # Ограничение FPS
    clock.tick(30)

pygame.quit()