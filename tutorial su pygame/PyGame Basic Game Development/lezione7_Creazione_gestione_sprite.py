import pygame

pygame.init()

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)

class sprite(pygame.sprite.Sprite):
    def __init__(self, game, colore, size, position=(0, 0)):
        super().__init__()
        
        self._game = game
        
        self.image = pygame.Surface(size)
        self.image.fill(colore)
        
        self._position = position
        
        self.rect = self.image.get_rect(topleft=position)
    
    def display_rect(self):
        pygame.draw.rect(self._game.finestra, (255, 0, 0),
                         self.rect, 1)
   
    def update(self):
        self._game.finestra.blit(self.image, self._posizione)
                
class Game():
    def __init__(self):
        self._loop = True
        self._size = (800, 400)
        self.titolo = pygame.display.set_caption("Le gestione e la creazione dei sprite")
        self.finestra = pygame.display.set_mode(self._size)
        self._clock = pygame.time.Clock()
        self.m_posizione = (0, 0)
        
        self._all = pygame.sprite.Group()
        self._targets = pygame.sprite.Group()
        self._user_group = pygame.sprite.GroupSingle()
        
        self.user = sprite(self, BIANCO, (50, 50))
        self._user_group.add(self._user) # controllare
        self._all.add(self._user)
        
        for x in range(0, 20):
            size = (30, 30)
            
            block = sprite(self, BIANCO, size)
        
    def run(self):
        while self._loop:
            self.finestra.fill(NERO)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._loop = False
                elif event.type == pygame.MOUSEMOTION:
                    self.m_posizione = pygame.mouse.get_pos()
            
            self._clock.tick(60)
            self._player.update()
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    game = Game()
    game.run()
    pygame.quit()