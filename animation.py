import pygame

pygame.init()
display_width = 480
display_height = 270

screen = pygame.display.set_mode((display_width, display_height))
animated_text = pygame.image.load('images/Animation/animation.png')
fpsClock = pygame.time.Clock()
imageX = 100
imageY = 20
running = True
Black = (0, 0, 0)

while (running):
    imageY += 10
    screen.fill(Black)
    screen.blit(animated_text, (imageX, imageY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    pygame.display.update()
    fpsClock.tick(2)

pygame.quit()