import pygame
screen = pygame.display.set_mode((1140,740))
clock = pygame.time.Clock()         
player = pygame.image.load('odamcha.png').convert()
# entity = pygame.image.load('zombi.png').convert()
background = pygame.image.load('fon.jpg')
screen.blit(background, (0, 0))
pygame.display.set_caption("Center")
objects = []

class GameObject:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image  
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0
p = GameObject(player, 10, 3) 
p.move()         
# for x in range(10):                    
#     o = GameObject(entity, x*40, x)
#     objects.append(o)
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)

    screen.blit(p.image, p.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)