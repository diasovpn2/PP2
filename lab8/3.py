import pygame
def main():
    pygame.init()  
    screen = pygame.display.set_mode((640, 480)) 
    clock = pygame.time.Clock()  # Создаёт объект для ограничения FPS

    radius = 15  # Радиус кисти
    x = 0
    y = 0
    mode = 'blue'  # Начальный цвет — синий
    points = []  # Список для хранения координат мыши
    shape = 1  # Параметр формы: 1 — круг, 0 — квадрат
    erase_mode = False  # Режим ластика (по умолчанию выключен)

    # Основной игровой цикл
    while True:
        # Проверка нажатых клавиш
        pressed = pygame.key.get_pressed()

        # Проверка нажатия специальных клавиш
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        # Переключение формы (1 — квадрат, 2 — круг)
        rect_held = pressed[pygame.K_1]
        circle_held = pressed[pygame.K_2]

        # Проверка событий
        for event in pygame.event.get():

            # Выход из программы по нажатию "X", Ctrl+W или Alt+F4
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return

                # Изменение цвета по нажатию клавиш
                if event.key == pygame.K_r:
                    mode = 'red'  # Красный
                elif event.key == pygame.K_g:
                    mode = 'green'  # Зелёный
                elif event.key == pygame.K_b:
                    mode = 'blue'  # Синий
                elif event.key == pygame.K_y:
                    mode = 'yellow'  # Жёлтый
                elif event.key == pygame.K_c:
                    mode = 'cyan'  # Голубой
                elif event.key == pygame.K_p:
                    mode = 'pink'  # Розовый

                # Включение режима ластика
                if event.key == pygame.K_3:
                    erase_mode = True

                # Переключение формы
                if event.key == pygame.K_1:
                    shape = 1  # Круг
                elif event.key == pygame.K_2:
                    shape = 0  # Квадрат

            # Управление размером кисти (колесо мыши)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка — увеличить размер
                    radius = min(200, radius + 1)
                elif event.button == 3:  # Правая кнопка — уменьшить размер
                    radius = max(1, radius - 1)

            # Добавление координат в список при движении мыши
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]  # Хранение только последних 256 точек

        # Очистка экрана (фон — черный)
        screen.fill((0, 0, 0))

        # Отрисовка линий между всеми точками
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, shape)
            i += 1

        # Если активирован режим ластика
        if erase_mode:
            screen.fill((0, 0, 0))  # Очистка экрана
            points = []  # Удаление всех точек
            erase_mode = False  # Выключение режима ластика

        pygame.display.update()  
        clock.tick(60)  

# Функция для рисования линий
def drawLineBetween(screen, index, start, end, width, color_mode, shape):
    #изменение цвета
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

    # цвета в зависимости от выбранного режима
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    elif color_mode == 'yellow':
        color = (c2, c2, c1)
    elif color_mode == 'cyan':
        color = (c1, c2, c2)
    elif color_mode == 'pink':
        color = (c2, c1, c2)

    #количества итераций для линии
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    # рисование линии
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if shape:
            pygame.draw.circle(screen, color, (x, y), width)  # Круг
        else:
            pygame.draw.rect(screen, color, (x, y, width, width))  # Квадрат
main()
