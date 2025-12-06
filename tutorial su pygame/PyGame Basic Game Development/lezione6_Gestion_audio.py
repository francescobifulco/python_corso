import pygame

pygame.init()

ALTEZZA = 800
LARGHEZZA = 400
TITOLO = 'La gestione del Audio'

NERO = (0, 0, 0)
BIANCO = (255, 255, 255)

FINESTRA = pygame.display.set_mode((ALTEZZA, LARGHEZZA))
pygame.display.set_caption(TITOLO)
FINESTRA.fill(NERO)

clock = pygame.time.Clock()

if not pygame.mixer.get_init():
    exit(1)
    
pygame.mixer.music.load('suono.ogg')
pygame.mixer.music.play(loops=-1)

click = pygame.mixer.Sound('Click.ogg')

loop = True
while loop:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False
        if event.type == pygame.KEYDOWN:
            print('lettera ' + str(event.key) + ' aka ' + pygame.key.name(event.key) + " down")
            click.play() # mettere un suono
        if event.type == pygame.KEYUP:
            print('lettera ' + str(event.key) + ' aka ' + pygame.key.name(event.key) + " up")
    
    
    pygame.display.update()
    
    clock.tick_busy_loop(60)

pygame.quit()
pygame.mixer.quit()