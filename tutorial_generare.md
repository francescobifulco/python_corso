Ecco **un mini–corso completo, dettagliato e progressivo sulle collisioni in Pygame**, strutturato in **4 lezioni**, ciascuna con spiegazioni approfondite ed esempi di codice completi e funzionanti.

---

# 🎮 **Corso Pygame — Collisioni (4 Lezioni Complete e Approfondite)**

## **Indice**

1. **Lezione 1 — Collisioni con i rettangoli (Rect)**
2. **Lezione 2 — Collisioni tra sprite con `pygame.sprite`**
3. **Lezione 3 — Collisioni pixel–perfect (mask & hitmask)**
4. **Lezione 4 — Gestione avanzata delle collisioni (risoluzione, rimbalzi, piattaforme)**

---

# 🧱 **Lezione 1 — Collisioni con i Rect**

Le collisioni più semplici in Pygame utilizzano gli oggetti **`pygame.Rect`**, che rappresentano rettangoli con posizione e dimensioni.

### ✔️ Metodo fondamentale:

* `rect1.colliderect(rect2)` → ritorna **True** se i due rettangoli si sovrappongono.

---

## 🔹 Esempio Classico: collisione tra giocatore e oggetto

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 50, 50)
enemy = pygame.Rect(300, 150, 60, 60)

vel = 5

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: player.x += vel
    if keys[pygame.K_LEFT]:  player.x -= vel
    if keys[pygame.K_UP]:    player.y -= vel
    if keys[pygame.K_DOWN]:  player.y += vel

    # --- Collisione ---
    if player.colliderect(enemy):
        print("Collisione!")

    screen.fill((30, 30, 30))
    pygame.draw.rect(screen, (0, 255, 0), player)
    pygame.draw.rect(screen, (255, 0, 0), enemy)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### 🧠 Cosa hai imparato

* Creare e usare rettangoli.
* Rilevare collisioni con `.colliderect()`.
* Disegnare rettangoli per debugging.

---

# 🧱 **Lezione 2 — Collisioni con Sprite e Gruppi**

Pygame include un sistema OOP potente basato su classi **Sprite**.

### Perché usare Sprite?

✔ gestiscono:

* immagine
* rettangolo
* aggiornamento
* collisioni con gruppi

---

## 🔹 Metodi importanti:

* `pygame.sprite.spritecollide(sprite, group, dokill)`
* `pygame.sprite.collide_rect(sprite1, sprite2)`
* `pygame.sprite.collide_circle(sprite1, sprite2)`
  (richiede attributo `radius`)

---

## 🔹 Esempio completo con Sprite e Gruppi

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
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

class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=pos)

player = Player((50, 50))
enemy  = Enemy((300, 200))

all_sprites = pygame.sprite.Group(player, enemy)
enemies = pygame.sprite.Group(enemy)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    # collisione sprite con gruppo
    if pygame.sprite.spritecollide(player, enemies, False):
        print("Collisione con sprite!")

    screen.fill((40, 40, 40))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

---

# 🖼 **Lezione 3 — Collisioni Pixel Perfect con Mask**

Quando i tuoi sprite **non sono perfettamente rettangolari**, usare `Rect` non basta.

→ Serve una collisione precisa basata sui pixel NON trasparenti.

---

## ✔ Funzioni fondamentali:

* `pygame.mask.from_surface(surface)`
* `pygame.sprite.collide_mask(sprite1, sprite2)`

---

## 🔹 Esempio: collisione pixel-perfect

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

class Object(pygame.sprite.Sprite):
    def __init__(self, img_path, pos):
        super().__init__()
        self.image = pygame.image.load(img_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.image)

class Player(Object):
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]: self.rect.x += 4
        if keys[pygame.K_LEFT]:  self.rect.x -= 4

player = Player("player.png", (100, 200))
rock   = Object("rock.png", (350, 200))

all_sprites = pygame.sprite.Group(player, rock)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.update()

    if pygame.sprite.collide_mask(player, rock):
        print("Collisione pixel-perfect!")

    screen.fill((10, 10, 10))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### 🧠 Cosa hai imparato

* Creare una maschera per la collisione.
* Rilevare collisioni precise.

---

# 🧱 **Lezione 4 — Collisioni Avanzate (Piattaforme, Rimbalzi, Risoluzione)**

Finora abbiamo rilevato collisioni.
Ora vediamo **come gestirle**, cioè impedire compenetrazione, far rimbalzare oggetti, ecc.

---

## 🔹 Esempio: Giocatore che non attraversa muri

Tecnica standard:

1. muovi il giocatore sugli assi separatamente
2. controlla la collisione
3. risolvi “spingendo” il giocatore fuori dal rettangolo del muro

---

## 🔹 Codice completo (collisione fisica con muro)

```python
import pygame
pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

player = pygame.Rect(50, 50, 40, 40)
wall = pygame.Rect(200, 150, 200, 40)

vel = 5

def move_and_collide(rect, dx, dy, obstacle):
    # movimento separato su x
    rect.x += dx
    if rect.colliderect(obstacle):
        if dx > 0:
            rect.right = obstacle.left
        if dx < 0:
            rect.left = obstacle.right

    # movimento separato su y
    rect.y += dy
    if rect.colliderect(obstacle):
        if dy > 0:
            rect.bottom = obstacle.top
        if dy < 0:
            rect.top = obstacle.bottom

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dx = dy = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]: dx =  vel
    if keys[pygame.K_LEFT]:  dx = -vel
    if keys[pygame.K_UP]:    dy = -vel
    if keys[pygame.K_DOWN]:  dy =  vel

    move_and_collide(player, dx, dy, wall)

    screen.fill((50, 50, 50))
    pygame.draw.rect(screen, (0, 200, 0), player)
    pygame.draw.rect(screen, (200, 0, 0), wall)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
```

### 🧠 Cosa hai imparato

* Movimento basato sugli assi (indispensabile per platformer).
* Risoluzione della collisione.
* Bloccare il passaggio del giocatore.

---

# 🎉 **Conclusione del Corso**

Hai imparato:

### ✔ Le collisioni base con `Rect`

### ✔ Le collisioni con sprite e gruppi

### ✔ Le collisioni pixel-perfect con maschere

### ✔ Le collisioni fisiche per giochi platform

---

# 📘 **Vuoi lezioni aggiuntive?**

Posso aggiungere:

✅ Lezione 5 — Rimbalzi realistici (fisica 2D)
✅ Lezione 6 — Tilemap e collisioni tile-based
✅ Lezione 7 — Hitbox personalizzate e gestione dei danni
✅ Lezione 8 — Collisioni circolari e bounding shapes avanzate

Basta chiedere!
