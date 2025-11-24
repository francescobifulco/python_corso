#                  IMPORTAZIONE LIBRERIE
import pygame
import random

#                  INIZIALIZZAZIONE PYGAME
pygame.init()

#                  CARICAMENTO IMMAGINI
sfondo = pygame.image.load('immagini/sfondo.png')
uccello = pygame.image.load('immagini/uccello.png')
base = pygame.image.load('immagini/base.png')
gameover = pygame.image.load('immagini/gameover.png')
tubo_giu = pygame.image.load('immagini/tubo.png')
tubo_su = pygame.transform.flip(tubo_giu, False, True)  # tubo ruotato

# Titolo finestra
pygame.display.set_caption('flappy bird')

#                  COSTANTI GLOBALI
SCHERMO = pygame.display.set_mode((500, 500))  # finestra
FPS = 50 # Starto gli FPS a 50
VEL_AVANZ = 3 # velocità movimento tubi/base
FONT = pygame.font.SysFont('Comic Sans MS', 50, bold=True)

#                  CLASSE: GESTIONE TUBI
class Tubi:
    """Gestisce posizione, movimento, disegno e collisioni dei tubi."""
    def __init__(self):
        # Posizione iniziale fuori dallo schermo
        self.x = 300
        # Altezza random per creare gap diversi
        self.y = random.randint(-75,150)

    def avanza(self):
        """Muove i tubi verso sinistra e li disegna."""
        self.x -= VEL_AVANZ
        SCHERMO.blit(tubo_giu, (self.x, self.y + 210))   # tubo inferiore
        SCHERMO.blit(tubo_su, (self.x, self.y - 210))    # tubo superiore

    def collisione(self, uccello, uccellox, uccelloy):
        """Controlla se l'uccello collide con uno dei due tubi."""
        tolleranza = 5

        # Lati dell'uccello
        uccello_lato_d = uccellox + uccello.get_width() - tolleranza
        uccello_lato_s = uccellox + tolleranza
        uccello_lato_su = uccelloy + tolleranza
        uccello_lato_giu = uccelloy + uccello.get_height() - tolleranza

        # Lati dei tubi
        tubo_lato_d = self.x + tubo_giu.get_width()
        tubo_lato_s = self.x
        tubo_lato_su = self.y + 110
        tubo_lato_giu = self.y + 210

        # Collisione orizzontale
        if uccello_lato_d > tubo_lato_s and uccello_lato_s < tubo_lato_d:
            # Collisione verticale
            if uccello_lato_su < tubo_lato_su or uccello_lato_giu > tubo_lato_giu:
                hai_perso()

    def fra_tubi(self, uccello, uccellox):
        """Controlla se l'uccello è in mezzo ai tubi (per calcolare i punti)."""
        tolleranza = 5
        uccello_lato_d = uccellox + uccello.get_width() - tolleranza
        uccello_lato_s = uccellox + tolleranza
        tubo_lato_d = self.x + tubo_giu.get_width()
        tubo_lato_s = self.x

        # Se l'uccello è allineato orizzontalmente ai tubi → è "dentro"
        if uccello_lato_d > tubo_lato_s and uccello_lato_s < tubo_lato_d:
            return True
        return False

#                  FUNZIONI DI DISEGNO E AGGIORNAMENTO
def disegna_oggetti():
    """Disegna sfondo, tubi, uccello, base e punteggio."""
    SCHERMO.blit(sfondo, (0, 0))
    SCHERMO.blit(uccello, (uccellox, uccelloy))

    SCHERMO.blit(base, (basex, 400))

    # Disegna ciascun tubo
    for t in tubi:
        t.avanza()

    # Disegna punteggio
    punti_r = FONT.render(str(punti), True, (255, 255, 255))
    SCHERMO.blit(punti_r, (144, 0))

def aggiorna():
    """Aggiorna lo schermo e imposta il framerate."""
    pygame.display.update()
    pygame.time.Clock().tick(FPS)

#                  INIZIALIZZAZIONE VARIABILI DI GIOCO
def inizializza():
    """Reimposta tutte le variabili per una nuova partita."""
    global uccellox, uccelloy, uccello_vely
    global basex
    global tubi
    global punti
    global dentro_tubi

    dentro_tubi = False
    punti = 0
    uccellox, uccelloy = 60, 150
    uccello_vely = 0
    basex = 0

    # Lista dei tubi (inizialmente uno solo)
    tubi = [Tubi()]

#                  FUNZIONE GAME OVER
def hai_perso():
    """Mostra la schermata di game over e attende il tasto per ricominciare."""
    SCHERMO.blit(gameover, (50, 180))
    aggiorna()

    ricomincia = False
    while not ricomincia:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                inizializza()
                ricomincia = True
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

#                  START DEL GIOCO
inizializza()

#                  CICLO DI GIOCO PRINCIPALE
while True:
    # ------------------- Movimento Base ---------------------
    basex -= VEL_AVANZ
    if basex < -45:
        basex = 0

    # ------------------ Gravità Uccello ---------------------
    uccello_vely += 1
    uccelloy += uccello_vely

    # ---------------------- Controlli ------------------------
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            uccello_vely = -10
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # ------------------- Generazione Tubi --------------------
    max_tubix = max(t.x for t in tubi)
    if max_tubix < 150:
        tubi.append(Tubi())

    # ----------------- Collisioni Uccello/Tubi ---------------
    for t in tubi:
        t.collisione(uccello, uccellox, uccelloy)

    # ---------------------- Calcolo Punti --------------------
    if not dentro_tubi:
        for t in tubi:
            if t.fra_tubi(uccello, uccellox):
                dentro_tubi = True
                break
    if dentro_tubi:
        dentro_tubi = False
        for t in tubi:
            if t.fra_tubi(uccello, uccellox):
                dentro_tubi = True
                break
        if not dentro_tubi:
            punti += 1

    # ----------------- Collisione con il Suolo ---------------
    if uccelloy > 380:
        hai_perso()

    # ---------------- Disegno degli Oggetti -----------------
    disegna_oggetti()
    aggiorna()
