import pygame
import sys

pygame.init()

WIDTH,HEIGHT = 640,480
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("最初のゲーム")

WHITE = (255,255,255,)
BLUE = (50,100,255)

player_size = 50
player_x = WIDTH // 2
player_y = HEIGHT // 2
speed = 5

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    screen.fill(WHITE)

    pygame.draw.rect(screen,BLUE,(player_x,player_y,player_size,player_size))

    pygame.display.flip()

    clock.tick(60)
