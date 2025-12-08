# Quando i tuoi sprite non sono perfettamente 
# rettangolari, usare Rect non basta. Serve 
# una collisione precisa basata sui pixel 
# NON trasparenti.

import pygame

pygame.init()

FINESTRA = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('Collisioni Pixel Perfect con Mask')

class Object(pygame.sprite.Sprite):
    def __init__(self, img_path, pos):
        super().__init__()
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

class Giocattore(Object):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.rect.x += 4
        if keys[pygame.K_LEFT]:  self.rect.x -= 4

gio1 = Giocattore("player.png", (100, 200))
rock   = Object("rock.png", (350, 200))

grup_personaggi = pygame.sprite.Group(gio1, rock)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
    
    gio1.update()
    
    if pygame.sprite.collide_mask(gio1, rock):
        print("Collisione pixel-perfect!")
    
    FINESTRA.fill((10, 10, 10))
    grup_personaggi.draw(FINESTRA)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()