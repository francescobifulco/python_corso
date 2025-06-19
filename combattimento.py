"""Progetto Python: "Duello tra Eroi" (Gioco di Ruolo a Turni Semplice)

Obiettivo: Creare un gioco di ruolo testuale a turni dove due "eroi" si sfidano in una battaglia, usando diverse abilità e strategie.

Concetti Python che coprirai:

Variabili e Tipi di Dati: Numeri interi (HP, danno), stringhe (nomi), booleani (stato del gioco).
Input/Output: input() per le scelte del giocatore, print() per visualizzare le informazioni.
Strutture Condizionali: if, elif, else per la logica di gioco (es. scegliere un'azione, verificare la vittoria).
Cicli: while per il ciclo di gioco principale (i turni continuano finché un eroe non vince), for (potrebbe essere usato per iterare su liste di abilità).
Funzioni: Organizzare il codice in blocchi riutilizzabili (es. attacca(), usa_pozione(), mostra_stato()).
Liste e Dizionari: Liste di abilità, inventario, o attributi di un personaggio. Dizionari per definire le proprietà di un eroe o di un'abilità.
Classi e Oggetti (Programmazione Orientata agli Oggetti - OOP): Rappresentare gli "eroi" come oggetti con propri attributi (HP, attacco, difesa) e metodi (azioni che possono compiere). Questo è un passo più avanzato ma fondamentale.
Gestione delle Eccezioni (Opzionale ma consigliato): try, except per gestire input non validi da parte dell'utente.
Moduli (Base): Importare moduli standard (es. random per tiri di dado o casualità).
Fasi del Progetto (Passo dopo Passo):

Fase 1: Configurazione Base e Variabili

Inizia il tuo file Python.
Definisci le statistiche degli eroi:
Pensa a due eroi. Per ognuno, definisci variabili per:
Nome (stringa)
Punti Vita (HP) iniziali (intero)
Attacco base (intero)
Difesa base (intero)
(Opzionale) Energia o Mana per abilità speciali (intero)
Suggerimento: Puoi usare variabili separate per ora, ma pensa già a come potresti raggrupparle in futuro (liste o dizionari).
Visualizza le statistiche iniziali: Usa print() per mostrare ai giocatori lo stato iniziale dei due eroi.
Argomenti trattati: Variabili, Tipi di dati (stringhe, interi), Input/Output (print).

Fase 2: Il Ciclo di Gioco Principale

Implementa il ciclo di gioco: Il gioco deve continuare finché uno degli eroi non ha 0 HP o meno.
Usa un ciclo while la cui condizione controlla i Punti Vita di entrambi gli eroi.
All'interno del ciclo, dovrà succedere un "turno".
Gestione dei turni:
Decidi chi attacca per primo (es. Eroe 1, poi Eroe 2).
All'inizio di ogni turno, visualizza lo stato attuale di entrambi gli eroi (HP rimanenti).
Argomenti trattati: Cicli (while), Strutture condizionali (per la condizione del ciclo).

Fase 3: Azioni Base dei Giocatori

Scelta dell'azione:
Chiedi all'eroe di turno quale azione vuole compiere. Usa input() per ottenere la scelta del giocatore (es. "1 per Attacco", "2 per Difesa", "3 per Usa Oggetto").
Usa if, elif, else per eseguire il codice appropriato in base alla scelta.
Implementa l'azione "Attacco":
Quando un eroe attacca, calcola il danno inflitto. Un semplice calcolo potrebbe essere danno = attacco_attaccante - difesa_difensore. Assicurati che il danno non sia negativo (se l'attacco è minore della difesa, il danno minimo è 0 o 1).
Sottrai il danno dai Punti Vita del difensore.
Stampa un messaggio che descrive l'azione e il danno inflitto.
Implementa l'azione "Difesa" (Opzionale):
Se un eroe sceglie "Difesa", la sua difesa per il prossimo turno potrebbe aumentare temporaneamente. Ricorda di resettarla o diminuirla nel turno successivo.
Argomenti trattati: Input/Output (input), Strutture condizionali (if/elif/else), Operatori aritmetici.

Fase 4: Funzioni per Organizzare il Codice

Refactoring con Funzioni:
Identifica blocchi di codice che si ripetono o che svolgono un compito specifico.
Crea funzioni per questi blocchi:
mostra_stato(eroe1_hp, eroe2_hp): per visualizzare i PV correnti.
calcola_danno(attacco, difesa): per calcolare il danno effettivo.
turno_eroe(eroe_che_attacca, eroe_che_difende): una funzione che gestisce tutte le azioni di un singolo turno per un eroe.
Chiama queste funzioni all'interno del ciclo di gioco principale.
Argomenti trattati: Funzioni (definizione, chiamata, parametri, valori di ritorno).

Fase 5: Miglioramenti e Complessità (Liste, Dizionari, Modulo Random)

Abilità Speciali:
Crea una lista di abilità per ogni eroe. Ogni abilità potrebbe essere un dizionario con: nome, costo_mana, danno_base, effetto_speciale.
Quando il giocatore sceglie un'azione, potrebbe anche scegliere di usare un'abilità.
Implementa il consumo di Mana/Energia.
Elementi Casuali:
Importa il modulo random.
Usa random.randint() per aggiungere un po' di casualità:
Critici: Una piccola percentuale di possibilità di fare il doppio del danno.
Schivata: Una piccola percentuale di possibilità di evitare completamente il danno.
Variazione del danno: Il danno non è fisso ma varia leggermente.
Inventario/Pozioni:
Crea una lista (o un dizionario) per l'inventario di ogni eroe.
Aggiungi un'azione "Usa Oggetto" che permetta di usare una pozione per ripristinare HP. Ricorda di rimuovere la pozione dall'inventario una volta usata.
Argomenti trattati: Liste, Dizionari, Moduli (random), Funzioni più complesse, Condizioni annidate.

Fase 6: Programmazione Orientata agli Oggetti (OOP) - Il Passaggio Cruciale

Questa è la fase più importante per un progetto che copre "quasi tutti gli argomenti".

Definisci una classe Eroe:
La classe Eroe dovrebbe avere un metodo __init__ per inizializzare gli attributi di un eroe (nome, hp, attacco, difesa, mana, inventario, ecc.).
Trasforma le variabili e le strutture dati che hai creato finora in attributi di questa classe.
Trasforma le funzioni che agiscono su un singolo eroe (o su due eroi) in metodi della classe Eroe. Esempi:
prendi_danno(self, danno)
attacca(self, bersaglio)
usa_abilita(self, abilita_scelta, bersaglio)
mostra_info(self)
Crea istanze degli eroi: Invece di eroe1_hp, eroe2_hp, ecc., creerai due oggetti Eroe: eroe1 = Eroe("Artù", 100, 15, 5) e eroe2 = Eroe("Morgana", 90, 18, 4).
Riscrivi il ciclo di gioco e le funzioni: Ora, invece di passare molte variabili alle funzioni, passerai gli oggetti Eroe e userai i loro metodi. Ad esempio, eroe1.attacca(eroe2).
Argomenti trattati: Classi, Oggetti, Metodi, self, __init__, Incapsulamento.

Fase 7: Gestione delle Eccezioni e Interfaccia Utente Migliorata

Gestione degli errori dell'utente:
Cosa succede se l'utente digita "xyz" invece di "1" per la scelta dell'azione?
Usa blocchi try e except per catturare errori come ValueError (se int(input()) fallisce) e guidare l'utente a inserire un input valido.
Interfaccia Utente (UI) testuale più chiara:
Usa stringhe f-string o .format() per presentare le informazioni in modo più leggibile.
Aggiungi separatori (es. ---) tra un turno e l'altro.
Chiari messaggi di vittoria/sconfitta.
Argomenti trattati: Gestione delle eccezioni (try/except), Formattazione stringhe.

Considerazioni Finali e Suggerimenti per l'Apprendimento:

Pensa prima di codificare: Prima di scrivere il codice per ogni fase, pensa a come dovrebbe funzionare e a quali dati ti servono.
Testa spesso: Dopo aver implementato una piccola parte, esegui il codice per vedere se funziona come previsto.
Non scoraggiarti: È normale commettere errori. Debuggare fa parte del processo di apprendimento.
Ricerca: Se ti blocchi su un concetto o una funzione specifica, cerca su Google o nella documentazione di Python.
Commenta il tuo codice: Spiega cosa fa ogni parte del tuo codice. Questo ti aiuterà a capire il tuo stesso lavoro in futuro e sarà utile se mostri il progetto ad altri.
Itera e migliora: Una volta che hai una versione funzionante, pensa a come potresti espanderla o migliorarla (più eroi, più abilità, un sistema di livelli, ecc.)."""
import random

class Eroe:
    def __init__(self,nome,punti_vita,attacco_b,difesa_b,mana):
        self.__nome = nome
        self.__punti_vita = punti_vita
        self.__attacco_b = attacco_b
        self.__difesa_b = difesa_b
        self.__mana = mana
        self.__inventario = []
        
    def get_nome(self):
        return self.__nome

    def set_nome(self, valore):
        self.__nome = valore
            
    def get_punti_vita(self):
        return self.__punti_vita

    def set_punti_vita(self, valore):
        self.__punti_vita = valore

    def get_attacco_b(self):
        return self.__attacco_b

    def set_attacco_b(self, valore):
        self.__attacco_b = valore
            
    def get_difesa_b(self):
        return self.__difesa_b

    def set_difesa_b(self, valore):
        self.__difesa_b = valore
    
    def get_mana(self):
        return self.__mana
    
    def set_mana(self, valore):
        self.__mana = valore

    def prendi_danno(self, danno):
        danno_effettivo = max(0, danno - self.get_difesa_b()) 
        self.set_punti_vita(self.get_punti_vita() - danno_effettivo) 
        print(f"{self.get_nome()} subisce {danno_effettivo} danni. Salute: {self.get_punti_vita()}")
    
    def attacca(self, bersaglio):
        attacco = self.get_attacco_b()
        danni = attacco
        danno_inflitto = max(1, self.get_attacco_b() - bersaglio.get_difesa_b())
        bersaglio.prendi_danno(danno_inflitto)
        print(f"il giocatore {self.get_nome()} danni inflitti {danno_inflitto}")
        if self.get_mana() > 0:
            costo_mana = 5
            self.set_mana(self.get_mana() - costo_mana)
        else: print("mana non sufficiente")
    
    def usa_abilita(self, abilita_scelta, bersaglio):
        abilita_costi_mana = {
    "Palla di Fuoco": 10,
    "Curare Ferite": 15,
    "Scudo Energetico": 8,
    "Fulmine a Catena": 25,
    "Attacco Potente": 5
        }
   
    def mostra_info(self):
        return (f"il giocato {self.get_nome()} ha punti vita {self.get_punti_vita()}, il suo attacco e {self.get_attacco_b()} e la sua difisa e {self.get_difesa_b()} il suo mano e di {self.get_mana()}")
    
    def inserimento(self):
        self.set_nome(input("inserisci il nome: "))
        self.set_punti_vita(int(input("inserisci i HP: ")))
        self.set_attacco_b (int(input("inserisci i punti di attacco: ")))
        self.set_difesa_b(int(input("inserisci i punti di difesa: ")))
        self.set_mana(int(input("inserisci i punti mana: ")))
        #oggetto = Eroe("",0,0,0,0)
        ogge = int(input("inserisci il numero dei oggetti nel tuo inventario: "))
        for i in range(ogge):
            oggetto = input("inserisci un oggetto nel tuo inventario: ")
            self.__inventario.append(oggetto)
    
def combatti():
    turno = 0
    gio1 = Eroe("",0,0,0,0)
    gio2 = Eroe("",0,0,0,0) 
    gio1.inserimento()
    gio2.inserimento()
    while gio1.get_punti_vita() > 0 and gio2.get_punti_vita() > 0:
        turno += 1
        print(f"\n--- INIZIO TURNO {turno + 1} ---")
        print(f"HP del giocatore 1 {gio1}")
        print(f"HP del giocatore 2 {gio2}")
        
## ----MEIN----##

combatti()

        