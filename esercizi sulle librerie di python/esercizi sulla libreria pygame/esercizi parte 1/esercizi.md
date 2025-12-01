### **16. Applicare gravità a un oggetto**

Simula la caduta libera: un rettangolo cade verso il basso con accelerazione costante. Impedisci che esca dallo schermo.

### **17. Salto semplice con gravità**

Aggiungi la possibilità di far saltare l’oggetto con la barra spaziatrice. Impedisci salti multipli mentre è in aria.

### **18. Salto doppio (double jump)**

Come sopra, ma con un massimo di due salti concessi prima di toccare il suolo.

### **19. Movimento con scorrimento della telecamera**

Simula una telecamera laterale: il giocatore rimane vicino al centro, ma lo sfondo scorre verso sinistra o destra.

### **20. Movimento diagonale realistico**

Assicurati che muovere il personaggio in diagonale non sia più veloce che in orizzontale/verticale. Normalizza il vettore di movimento.

---

## 🎯 **SEZIONE 3 — GRAFICA E ANIMAZIONE (21–30)**

### **21. Animazione sprite a 4 frame**

Carica 4 immagini di un personaggio che cammina e alternale durante il movimento. Quando si ferma, passa al frame idle.

### **22. Animazione basata sul tempo**

Modifica l’esercizio precedente in modo che il frame cambi solo dopo un certo tempo trascorso, non ogni frame del gioco.

### **23. Caricare e mostrare uno sfondo complesso**

Carica un’immagine di sfondo più grande della finestra e permetti al giocatore di spostarsi su di essa tramite scrolling.

### **24. Effetto parallax scrolling**

Implementa almeno tre livelli di sfondo che scorrono a velocità diverse per simulare profondità.

### **25. Effetto fade-in e fade-out**

Crea una transizione in cui lo schermo diventa gradualmente più luminoso (fade-in) e poi nerissimo (fade-out).

### **26. Barra della vita animata**

Crea una barra della vita che diminuisce gradualmente quando premi un tasto e torna a crescere premendone un altro.

### **27. Sprite che segue il mouse**

Un’immagine deve inseguire il mouse, muovendosi con una velocità massima per frame.

### **28. Sistema di particelle base**

Quando il giocatore preme un tasto, genera particelle che si muovono e svaniscono gradualmente.

### **29. Ombra sotto un personaggio**

Disegna un’ombra ellittica sotto un personaggio, la cui dimensione varia in base alla sua “altezza”.

### **30. Flash allo sparo**

Ogni volta che premi un tasto di sparo, mostra un breve flash (1–3 frame) davanti al giocatore.

---

## 🎯 **SEZIONE 4 — OGGETTI, GESTIONE E LOGICA (31–40)**

### **31. Gestione di oggetti tramite classi**

Crea una classe `Player` con attributi posizione, velocità e un metodo `update()` e `draw()`. Usa un’istanza nel loop principale.

### **32. Più oggetti gestiti in una lista**

Crea una classe `Ball` e genera 20 palline. Ogni pallina deve muoversi in una direzione casuale e rimbalzare contro i muri.

### **33. Generazione casuale di nemici**

Genera nemici in posizioni casuali a intervalli regolari. Fai in modo che si muovano verso il giocatore.

### **34. Timer personalizzato**

Crea un timer che, ogni 3 secondi, esegue una funzione (es. generare un nemico). Non usare `pygame.time.set_timer()`: implementa un timer manuale.

### **35. Sparo di proiettili**

Premendo la barra spaziatrice, genera proiettili che viaggiano in avanti. Cancellali quando escono dallo schermo.

### **36. Sparo con direzione del mouse**

Fai sparare proiettili verso il puntatore del mouse calcolando la direzione tramite trigonometria.

### **37. Spostamento nemici a zig-zag**

Crea nemici che si muovono verso il giocatore, ma con un movimento sinusoidale orizzontale.

### **38. Area di raccolta oggetti**

Genera collezionabili che scompaiono se il giocatore entra in un’area circolare attorno ad essi.

### **39. Punteggio con visualizzazione a schermo**

Ogni oggetto raccolto incrementa lo score. Disegna il punteggio in alto a sinistra.

### **40. Menu di pausa**

Implementa un menu che compare quando premi “P”, mostrando opzioni come “Resume” e “Quit”.

---

## 🎯 **SEZIONE 5 — COLLISIONI (41–45)**

### **41. Collisione rettangolo-rettangolo (AABB)**

Crea due rettangoli: uno controllato dal giocatore e uno statico. Implementa un sistema che rilevi quando si sovrappongono usando il metodo AABB (Axis-Aligned Bounding Box). Quando collidono, cambia colore.

### **42. Collisione cerchio-cerchio**

Crea due cerchi. Uno è controllato dal mouse. Quando i cerchi si toccano (distanza dei centri ≤ somma dei raggi), cambia il colore dello sfondo.

### **43. Collisione proiettile-nemico**

Usa una lista di nemici e una di proiettili. Rimuovi sia il proiettile che il nemico quando si toccano. Aggiungi un effetto di esplosione.

### **44. Rimbalzo tramite normale della superficie**

Crea una palla che rimbalza sulle pareti, invertendo la velocità correttamente. Aggiungi superfici diagonali che modificano il vettore di rimbalzo.

### **45. Collisione avanzata con penetrazione minima**

Crea un platformer semplice:

* un player che cammina e salta
* piattaforme di varie dimensioni
* rilevamento collisioni
* correzione della penetrazione (pushback)
* riconoscimento collisione laterale, superiore e inferiore

46 Esercizio Pygame: "Evita il nemico!"
Obiettivo

Creare una finestra di gioco in cui:

il giocatore può muovere un quadrato con le frecce della tastiera;

un nemico si muove automaticamente da sinistra a destra;

quando il giocatore collide con il nemico, il gioco stampa “Collisione!” e si chiude.

Concetti coinvolti

inizializzazione di Pygame

gestione degli input da tastiera

aggiornamento della posizione degli oggetti

rilevamento delle collisioni con colliderect

ciclo principale del gioco
