import pygame

pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('final project')


walkRight = [pygame.image.load('pygame_right_1.png'),
             pygame.image.load('pygame_right_2.png'),
             pygame.image.load('pygame_right_3.png'),
             pygame.image.load('pygame_right_4.png'),
             pygame.image.load('pygame_right_5.png'),
             pygame.image.load('pygame_right_6.png')]

walkLeft = [pygame.image.load('pygame_left_1.png'),
            pygame.image.load('pygame_left_2.png'),
            pygame.image.load('pygame_left_3.png'),
            pygame.image.load('pygame_left_4.png'),
            pygame.image.load('pygame_left_5.png'),
            pygame.image.load('pygame_left_6.png')]

playerStand = pygame.image.load('pygame_idle.png')
bg = pygame.image.load('pygame_bg.jpg')


clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 10
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.hitbox = (self.x + 20, self.y, 28, 60)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not (self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 5], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox,2)


class projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel =12 * facing

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'),
                 pygame.image.load('R2E.png'),
                 pygame.image.load('R3E.png'),
                 pygame.image.load('R4E.png'),
                 pygame.image.load('R5E.png'),
                 pygame.image.load('R6E.png'),
                 pygame.image.load('R7E.png'),
                 pygame.image.load('R8E.png'),
                 pygame.image.load('R9E.png'),
                 pygame.image.load('R10E.png'),
                 pygame.image.load('R11E.png')]

    walkLeft = [pygame.image.load('L1E.png'),
                pygame.image.load('L2E.png'),
                pygame.image.load('L3E.png'),
                pygame.image.load('L4E.png'),
                pygame.image.load('L5E.png'),
                pygame.image.load('L6E.png'),
                pygame.image.load('L7E.png'),
                pygame.image.load('L8E.png'),
                pygame.image.load('L9E.png'),
                pygame.image.load('L10E.png'),
                pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 20, self.y, 28, 60)


    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 33:
             self.walkCount = 0
        if self.vel > 0:
            win.blit(self.walkRight[self.walkCount // 5], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.walkLeft[self.walkCount // 5], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x + 20, self.y, 28, 60)
        pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0


def redrawGameWindow():
    win.blit(bg, (0, 0))
    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)

    pygame.display.update()


goblin = enemy(40, 440, 64, 64, 450)
man = player(100, 430, 60, 71)
bullets = []
run = True
while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1
        else:
            facing = 1

        if len(bullets) < 6:
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height // 2), 6, (0,0,0), facing))

    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.vel - man.width:
        man.x += man.vel
        man.left = False
        man.right = True
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not man.isJump:
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()


pygame.quit()
