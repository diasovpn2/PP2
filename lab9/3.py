import pygame

def main():
    pygame.init()  
    screen = pygame.display.set_mode((640, 480)) 
    clock = pygame.time.Clock()  # Создаёт объект для ограничения FPS

    radius = 15  # Радиус кисти
    mode = 'blue'  # Начальный цвет — синий
    points = []  # Список для хранения координат мыши
    shape = 1  # Параметр формы: 1 — круг, 0 — квадрат, 2 — прямоугольник, 3 — равносторонний треугольник, 4 — ромб
    erase_mode = False  # Режим ластика (по умолчанию выключен)

    # Основной игровой цикл
    while True:
        pressed = pygame.key.get_pressed()

        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]

        for event in pygame.event.get():
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
                    mode = 'red'  
                elif event.key == pygame.K_g:
                    mode = 'green'  
                elif event.key == pygame.K_b:
                    mode = 'blue'  
                elif event.key == pygame.K_y:
                    mode = 'yellow'  
                elif event.key == pygame.K_c:
                    mode = 'cyan'  
                elif event.key == pygame.K_p:
                    mode = 'pink'  

                # Включение режима ластика
                if event.key == pygame.K_3:
                    erase_mode = True

                # Переключение формы
                if event.key == pygame.K_1:
                    shape = 1  # Круг
                elif event.key == pygame.K_2:
                    shape = 0  # Квадрат
                elif event.key == pygame.K_4:
                    shape = 2  # Прямоугольник
                elif event.key == pygame.K_5:
                    shape = 3  # Равносторонний треугольник
                elif event.key == pygame.K_6:
                    shape = 4  # Ромб

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  
                    radius = min(200, radius + 1)
                elif event.button == 3:  
                    radius = max(1, radius - 1)

            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]  

        screen.fill((0, 0, 0))

        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode, shape)
            i += 1

        if erase_mode:
            screen.fill((0, 0, 0))  
            points = []  
            erase_mode = False  

        pygame.display.update()  
        clock.tick(60)  

# Функция для рисования линий

def drawLineBetween(screen, index, start, end, width, color_mode, shape):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))

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

    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))

    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        if shape == 1:
            pygame.draw.circle(screen, color, (x, y), width)
        elif shape == 0:
            pygame.draw.rect(screen, color, (x, y, width, width))
        elif shape == 2:
            pygame.draw.rect(screen, color, (x, y, width * 2, width))
        elif shape == 3:
            pygame.draw.polygon(screen, color, [(x, y), (x - width, y + width * 2), (x + width, y + width * 2)])
        elif shape == 4:
            pygame.draw.polygon(screen, color, [(x, y - width), (x - width, y), (x, y + width), (x + width, y)])

main()
