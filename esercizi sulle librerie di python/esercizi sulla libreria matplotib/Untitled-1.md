### **6. Personalizzazione marcatori**

Crea uno scatter plot in cui ogni punto ha un marcatore diverso, dimensioni variabili e bordo colorato.

### **7. Grafico a barre semplice**

Plotta un grafico a barre con altezza di 6 categorie, includendo etichette, rotazione delle categorie e titolo.

### **8. Barre orizzontali**

Riproduci l'esercizio precedente ma usa barre orizzontali e personalizza i colori.

### **9. Grafico a torta**

Crea un grafico a torta di 5 categorie con percentuali reali, creando anche un effetto “explode” su una categoria.

### **10. Error bars**

Crea un grafico lineare con barre di errore, simulando misurazioni con deviazione standard casuale.

---

## **Sezione 2 — Subplot, layout e figure (11–18)**

### **11. Subplot 2x2**

Crea una figure con 4 subplot (2x2).
In ogni subplot disegna una funzione diversa: lineare, quadratica, cubica ed esponenziale.

### **12. Condivisione degli assi**

Crea una figure con 3 grafici sovrapposti con `sharex=True` e compara tre dataset temporali diversi.

### **13. Griglia di subplot complessa**

Crea una figure con:

* un grafico grande centrale
* due piccoli grafici in basso
* un grafico verticale a destra

Usa `GridSpec`.

### **14. Multiple figure**

Crea due finestre separate, una con un grafico a barre e una con un grafico a torta.

### **15. Modifica dimensioni e DPI**

Disegna un grafico con dimensioni personalizzate (ad esempio 12×8 pollici) e DPI=200.

### **16. Aggiungere testo ad una figura**

Crea un grafico e aggiungi testo in posizioni specifiche con font personalizzati.

### **17. Annotazioni con frecce**

Disegna un grafico di una funzione e aggiungi un’annotazione che indica il massimo locale usando arrowprops.

### **18. Twin axes**

Crea un grafico con due assi: uno per temperatura (°C) e uno per umidità (%), condividendo la stessa ascissa temporale.

---

## **Sezione 3 — Grafici statistici e avanzati (19–28)**

### **19. Histogramma con bins personalizzati**

Genera 10000 valori normali e plottali con diversi intervalli di bins.

### **20. Histogramma + Curva di densità**

Plotta un istogramma di dati casuali e sovrapponi una curva di densità gaussiana.

### **21. Boxplot**

Genera 4 dataset diversi e rappresentali in un boxplot multiplo.

### **22. Violin plot**

Ripeti l’esercizio precedente usando un violin plot e confronta visivamente i risultati.

### **23. Heatmap**

Crea una matrice 20×20 con valori casuali e rappresentala con una heatmap con colorbar.

### **24. Immagine 2D (imshow)**

Carica un'immagine esistente o crea una matrice 256×256 con gradiente e visualizzala con colormap personalizzata.

### **25. Grafico 3D — superficie**

Usa `Axes3D` per creare una superficie 3D della funzione z = sin(x)*cos(y).

### **26. Grafico 3D — scatter**

Genera 500 punti casuali in 3D e plottali con dimensioni e colori variabili.

### **27. Contour plot**

Disegna un contour plot e un contour fill della funzione z = x² + y².

### **28. Grafico polare**

Crea un grafico polare della funzione r = 1 + cos(θ).

---

## **Sezione 4 — Stili e colori (29–36)**

### **29. Usare stili Matplotlib**

Riproduci un grafico usando tre stili diversi:

* ggplot
* seaborn
* classic

### **30. Colormap**

Plotta uno scatter con colorazione dei punti basata sulla distanza dal centro, usando diverse colormap.

### **31. Ciclo dei colori personalizzato**

Imposta un ciclo di colori usando `plt.rcParams['axes.prop_cycle']`.

### **32. Creare un tema personalizzato**

Modifica i parametri globali (rcParams) per creare uno stile personale (font, colori, dimensioni, griglia).

### **33. Grafico trasparente**

Crea un grafico con sfondo trasparente e salva l'immagine in PNG con `transparent=True`.

### **34. Linee con gradienti**

Crea una linea colorata con un gradiente lungo il percorso utilizzando LineCollection.

### **35. Bar plot con gradienti**

Crea un grafico a barre con gradienti verticali personalizzati.

### **36. Custom colormap**

Crea una colormap personalizzata usando `LinearSegmentedColormap`.

---

## **Sezione 5 — Matplotlib per applicazioni reali (37–46)**

### **37. Timeline storica**

Crea una timeline con eventi storici distribuiti su un asse orizzontale.

### **38. Gantt chart semplificato**

Crea un grafico con barre orizzontali che rappresentano attività, durata e categorie.

### **39. Visualizzazione dati temporali**

Carica un dataset temporale (o generane uno) e crea:

* grafico lineare
* grafico con rolling mean
* evidenzia zone con `axvspan`

### **40. Mappe (basiche) con imshow**

Scarica o genera dati geografici in una matrice e visualizzali come mappa con colormap adeguata.

### **41. Gauge chart (indicatore)**

Simula un tachimetro usando plot polare e forme geometriche.

### **42. Matplotlib + Pandas**

Carica un DataFrame e crea grafici multipli (linee, barre, boxplot).

### **43. Dashboard con subplots complessi**

Crea una mini dashboard con:

* linea temporale
* istogramma
* barra comparativa
* tabella con valori

Usa `gridspec`.

### **44. Annotazioni complesse su dati reali**

Carica dati reali (o generati) e aggiungi:

* annotazioni
* evidenziazione punti importanti
* frecce
* testo dinamico

### **45. Interattività di base**

Usa Matplotlib per:

* zoom
* passaggio del mouse su un punto (eventi)
* clic del mouse per leggere coordinate

### **46. Creazione di una funzione wrapper**

Scrivi una funzione Python che prende un dataset e crea automaticamente un grafico completo con:

* dimensioni dinamiche
* legenda
* colori automatici
* titolo e sottotitolo
* salvataggio in file

---
crea 46 esercizi sulla libreria matplotib in modo progressivo gli esercizi devono essere lunghi e deve comprendere tutti i concetti della libreria di matplotib
