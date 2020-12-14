import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caprion('final game')

x = 50
y = 50
widht = 40
height = 40
speed = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False

    pygame.draw.rect(win, (0,0,255), (x, y, widht, height))
    pygame.display.update()

pygame.quit()
