# Pygame include un sistema OOP potente basato su classi Sprite.

import pygame

pygame.init()

FINESTRA = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
pygame.display.set_caption('ColCollisioni con Sprite e Gruppi')

class Giocattore(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=pos)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.rect.x += 5
        if keys[pygame.K_LEFT]:  self.rect.x -= 5
        if keys[pygame.K_UP]:    self.rect.y -= 5
        if keys[pygame.K_DOWN]:  self.rect.y += 5

class Nemico(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

gio1 = Giocattore((50, 50))
nem1 = Nemico((300, 200))
nem2 = Nemico((150, 250))

grup_personaggi = pygame.sprite.Group(gio1, nem1, nem2)
nemici = pygame.sprite.Group(nem1, nem2)

loop = True
while loop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop= False
    
    gio1.update()
    
    # collisione sprite con gruppo
    if pygame.sprite.spritecollide(gio1, nemici, False):
        print("Collisione con sprite!")
    
    FINESTRA.fill((40, 40, 40))
    grup_personaggi.draw(FINESTRA)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()