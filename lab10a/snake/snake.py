import pygame
import random
import psycopg2

# Подключение к базе данных
def connect():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="Qazmlp12"
    )

# Функция для создания таблиц
def create_tables():
    conn = connect()
    cur = conn.cursor()

    # Таблица user
    cur.execute("""
    CREATE TABLE IF NOT EXISTS "user" (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) UNIQUE
    )
    """)

    # Таблица user_score
    cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES "user"(id),
        score INTEGER,
        level INTEGER,
        date_played TIMESTAMP DEFAULT current_timestamp
    )
    """)

    conn.commit()
    cur.close()
    conn.close()

# Запрос имени пользователя и получение/создание пользователя в базе данных
def get_user_id(username):
    conn = connect()
    cur = conn.cursor()

    # Проверка, существует ли пользователь в базе данных
    cur.execute("SELECT id FROM \"user\" WHERE username = %s", (username,))
    user_result = cur.fetchone()

    if user_result:
        user_id = user_result[0]
    else:
        # Если пользователя нет, создаем нового
        cur.execute("INSERT INTO \"user\" (username) VALUES (%s) RETURNING id", (username,))
        user_id = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return user_id


# Инициализация Pygame
pygame.init()

# Настройки игры
WIDTH = 600
HEIGHT = 600
CELL = 30
FPS_START = 5.5

screen = pygame.display.set_mode((WIDTH, HEIGHT))
game_over = False 

# Цвета
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)

# Отображение сетки
def draw_grid_chess():
    colors = [colorWHITE, colorGRAY]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# Класс точки (координаты)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

# Класс змеи
class Snake:
    def __init__(self):
        self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
        self.dx, self.dy = 0, -1  # Изначально движется вверх

    def move(self):
        # Создание новой головы
        new_head = Point(self.body[0].x + self.dx, self.body[0].y + self.dy)
        
        # Проверка границ
        if new_head.x < 0 or new_head.x >= WIDTH // CELL or new_head.y < 0 or new_head.y >= HEIGHT // CELL:
            return True  # Игра завершена

        # Проверка на столкновение с собой
        if new_head in self.body:
            return True  # Игра завершена
        
        # Перемещение тела змеи
        self.body.insert(0, new_head)  # Добавление новой головы
        self.body.pop()   # Удаление хвоста
        return False

    def draw(self):
        pygame.draw.rect(screen, colorRED, (self.body[0].x * CELL, self.body[0].y * CELL, CELL, CELL))
        for segment in self.body[1:]:
            pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

    def check_collision(self, food):
        global score, FPS, lvl 
        if self.body[0] == food.pos:  # Съесть еду
            self.body.append(Point(self.body[-1].x, self.body[-1].y))  # Увеличить длину тела
            food.move(self)
            score += food.cost 

            if score % 5 == 0:
                FPS += 0.5
                lvl += 1

# Класс еды
class Food:
    def __init__(self, disapper=True):
        self.disapper = disapper
        self.last_spawn_time = pygame.time.get_ticks()  # Запоминаем время последнего спауна
        self.move(snake=None)

    def move(self, snake):
        while True:
            self.x = random.randrange(0, WIDTH // CELL)  
            self.y = random.randrange(0, HEIGHT // CELL)  
            self.pos = Point(self.x, self.y)
            self.cost = random.randrange(1, 4)

            # Проверка, чтобы еда не спаунилась на теле змеи
            if snake is None or self.pos not in snake.body:
                if self.disapper:
                    self.last_spawn_time = pygame.time.get_ticks()  # Обновляем таймер спауна
                    break

    def draw(self):
        pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))


# Настройки игры
FPS = FPS_START
score = 0
lvl = 1
clock = pygame.time.Clock()

# Запрос имени пользователя и создание/получение пользователя в базе данных
username = input("Enter your name: ")
user_id = get_user_id(username)

# Создание змеи и еды
snake = Snake()
food = Food()
game_over = False

running = True
while running:
    if not game_over:
        if pygame.time.get_ticks() - food.last_spawn_time > 10000:
            food.move(snake)
        draw_grid_chess()
        game_over = snake.move()
        snake.check_collision(food)
        snake.draw()
        food.draw()

        # Отображение счета
        font_score = pygame.font.Font(None, 36)
        text = font_score.render(f" Score: {score} ", True, (0, 0, 0))
        font_score_rect = text.get_rect()
        screen.blit(text, (WIDTH - font_score_rect.w, 10))

        # Отображение уровня
        font_speed = pygame.font.Font(None, 36)
        text_speed = font_speed.render(f" Level: {lvl} ", True, (0, 0, 0))
        font_speed_rect = text_speed.get_rect()
        screen.blit(text_speed, (0, 10))

    else:
        # Экран "Game Over"
        screen.fill('red')

        font_GO = pygame.font.Font(None, 50)
        text_gameOver = font_GO.render("Game Over!", True, (255, 255, 255))
        text_rect = text_gameOver.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text_gameOver, text_rect)

        font_restart = pygame.font.Font(None, 25)
        text_restart = font_restart.render('Press "R" to Restart', True, (255, 255, 255))
        text_restart_rect = text_restart.get_rect(center=(WIDTH // 2, HEIGHT - 40))
        screen.blit(text_restart, text_restart_rect)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # P — пауза и сохранить
                conn = connect()
                cur = conn.cursor()
                cur.execute("INSERT INTO user_score (user_id, score, level) VALUES (%s, %s, %s)",
                            (user_id, score, lvl))
                conn.commit()
                cur.close()
                conn.close()
                print("The progress saved.")

        elif event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:  # Перезапуск игры
                # Сброс настроек
                FPS = FPS_START
                score = 0
                lvl = 1
                game_over = False 

                # Воссоздание змеи и еды
                snake = Snake()
                food = Food()  # Создание новой еды (сбрасывается last_spawn_time)
            snake.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
            snake.dx, snake.dy = 0, -1

        elif event.type == pygame.KEYDOWN and not game_over:
            # Управление змеей с помощью стрелок или WASD
            if event.key == pygame.K_RIGHT:
                snake.dx = 1
            elif event.key == pygame.K_LEFT:
                snake.dx = -1
            elif event.key == pygame.K_DOWN:
                snake.dy = 1
            elif event.key == pygame.K_UP:
                snake.dy = -1

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
