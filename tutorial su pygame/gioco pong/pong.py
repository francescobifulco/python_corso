import pygame
import random

# Inizializzazione pygame: attiva tutti i moduli necessari
pygame.init()

# Colori RGB
bianco = (255, 255, 255)
azzurro = (0, 189, 132)

# Creazione finestra di gioco 
larghezza = 800
altezza = 600

# Crea la finestra con le dimensioni specificate
finestra = pygame.display.set_mode((larghezza, altezza))

# Imposta il titolo della finestra
pygame.display.set_caption('Pong')

# Controllo del frame rate (FPS = fotogrammi al secondo)
clock = pygame.time.Clock()
fps = 60

# Creazione delle racchette
larghezza_r = 15
altezza_r = 100
velocita_r = 5

# Racchetta sinistra (Rect(x, y, larghezza, altezza))
racchetta_s = pygame.Rect(50, altezza // 2 - altezza_r // 2,
                          larghezza_r, altezza_r)

# Racchetta destra (Rect(x, y, larghezza, altezza))
racchetta_d = pygame.Rect(larghezza -50 - larghezza_r, altezza // 2 - altezza_r // 2,
                          larghezza_r, altezza_r)

# Creazione della palla
dimensione_p = 20
velocita_p_x = 5
velocita_p_y = 5

palla = pygame.Rect(larghezza // 2 - dimensione_p // 2,
                    altezza // 2 - dimensione_p // 2,
                    dimensione_p, dimensione_p)

# Punteggio 
punteggio = 0
# Caricamento font per il testo (nome, dimensione, bold, italic)
font = pygame.font.SysFont('Arial', 60, bold=True, italic=False)

# Funzione per disegnare gli oggetti sullo schermo 
def oggetti():
    finestra.fill(azzurro) # Riempie lo schermo con il colore di sfondo
    
     # Disegna le racchette
    pygame.draw.rect(finestra, bianco, racchetta_s)
    pygame.draw.rect(finestra, bianco, racchetta_d)
    
    # Disegna la palla
    pygame.draw.ellipse(finestra, bianco, palla)
    
    # Renderizza il punteggio come superficie di testo
    testo = font.render(str(punteggio), True , bianco)
    
    # Disegna il punteggio al centro dello schermo
    finestra.blit(testo, (larghezza // 2 - testo.get_width() // 2, 60))
                  
# ------ CICLO DI GIOCO PRINCIPALE ------

while True:
    # Gestione eventi (chiusura finestra)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
            
    oggetti()
    
    # Movimento degli oggetti
    # pygame.key.get_pressed() restituisce una 
    # lista booleana con i tasti premuti
    tasti = pygame.key.get_pressed()
    if tasti[pygame.K_w]:      # W → muovi la racchetta sinistra in alto
        racchetta_s.y -= velocita_r
    if tasti[pygame.K_s]:      # S → muovi la racchetta sinistra in basso
        racchetta_s.y += velocita_r
    if tasti[pygame.K_UP]:     # Freccia su → racchetta destra in alto
        racchetta_d.y -= velocita_r
    if tasti[pygame.K_DOWN]:   # Freccia giù → racchetta destra in basso
        racchetta_d.y += velocita_r
    
    # Movimento della palla 
    palla.x += velocita_p_x
    palla.y += velocita_p_y
    
    # La palla collide con i bordi verticali
    if palla.top <= 0 or palla.bottom >= altezza:
        velocita_p_y = -velocita_p_y # Inverte direzione verticale
    
    # La palla collide con i bordi orizzontali
    if palla.left <= 0 or palla.right >= larghezza:
        # Il giocatore perde
        palla.x = larghezza // 2 - dimensione_p // 2
        palla.y = larghezza // 2 - dimensione_p // 2
        
        # Imposta una nuova direzione casuale
        velocita_p_x = random.choice([-5, 5])
        velocita_p_y = random.choice([-5, 5])
        
        # Reimposta il punteggio
        punteggio = 0
        
    # La palla collide con le racchette
    # Rect.colliderect() → True se due rettangoli si toccano
    if palla.colliderect(racchetta_s) or palla.colliderect(racchetta_d):
        velocita_p_x = -velocita_p_x  # Inverte la direzione orizzontale
        punteggio += 1                # Aumenta punteggio
               
    # Aggiorna il display con tutto ciò che è stato disegnato
    pygame.display.update()
    
    # Mantiene il gioco alla velocità di 60 FPS
    clock.tick(fps)