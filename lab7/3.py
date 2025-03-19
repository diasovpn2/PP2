import pygame


pygame.init()

BACKGROUND_COLOR = (255, 255, 255) 
STEP = 20  

ball_x = 500 // 2
ball_y = 500 // 2




screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Ball")

running = True
while running:
    pygame.time.delay(50) 
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
 
    keys = pygame.key.get_pressed()
    
   
    if keys[pygame.K_LEFT] and ball_x - 25 - STEP >= 0:
        ball_x -= STEP
    if keys[pygame.K_RIGHT] and ball_x + 25 + STEP <= 500:
        ball_x += STEP
    if keys[pygame.K_UP] and ball_y - 25 - STEP >= 0:
        ball_y -= STEP
    if keys[pygame.K_DOWN] and ball_y + 25 + STEP <= 500:
        ball_y += STEP
    
  
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, ((255, 0, 0)), (ball_x, ball_y), 25)
    pygame.display.update()


pygame.quit()