"""## **TEST FINALE OOP - "La Battaglia dei Regni"**

### **Obiettivo**

Realizza un **gioco a turni da terminale** in cui il **giocatore** e una **IA** si sfidano con eserciti medievali. Ogni giocatore ha un **budget** iniziale per acquistare soldati. Gli eserciti combattono in più **round**, e dopo ogni battaglia si ricevono nuove risorse da spendere. Vince chi elimina tutte le unità nemiche.

---

###  **Requisiti strutturali (OOP)**

#### 🔹 **Classe Astratta: `Soldato`**

* Attributi protetti: `_nome`, `_costo`, `_attacco`, `_difesa`, `_salute`
* Metodo astratto: `attacca(avversario)`
* Metodi comuni:

  * `difenditi(danno)`
  * `è_vivo() → bool`
  * `stato() → stampa salute e ruolo`

#### **Classi Derivate:**

Ciascuna classe implementa il metodo `attacca()` con logiche **diverse** (polimorfismo):

1. **Cavaliere**

   * Alto costo, alta difesa, attacco medio
   * 20% di possibilità di **colpo critico** (attacco × 2)

2. **Arciere**

   * Costo medio, attacco alto, bassa difesa
   * Attacca **per primo** in ogni scontro 1v1

3. **Guaritore**

   * Costo medio, bassa difesa e attacco
   * Invece di attaccare, **cura un alleato vivo random**

4. **Mago**

   * Costo alto, attacco variabile (10–40), difesa bassa
   * 25% di chance di **saltare il turno** per stanchezza

---

### **Sistema di gioco**

### **Fase iniziale: Preparazione**

* Ogni giocatore ha un **budget iniziale di 1000 monete**
* Può acquistare soldati scegliendo nome e tipo
* I soldati vanno salvati in una lista `esercito`

#### **Ciclo di gioco: Round**

* Ogni round:

  1. I soldati vivi si scontrano in ordine (es. primo contro primo)
  2. I danni sono calcolati in base agli attacchi e difese
  3. I caduti vengono rimossi dall'esercito
* Alla fine del round:

  * Ogni giocatore riceve **+300 monete**
  * Può **acquistare nuovi soldati**
* Il gioco termina quando **uno dei due eserciti è vuoto**

#### **Vittoria**

Mostrare messaggio finale con:

* Vincitore
* Numero di round giocati
* Numero di soldati rimasti

---

### **Requisiti tecnici obbligatori**

 Uso di `ABC` e `@abstractmethod`
 Incapsulamento corretto (`__attributi` e proprietà dove necessario)
 Override del metodo `attacca()` in ciascuna sottoclasse
 Gestione delle liste e scontri in funzioni
 Interfaccia da **terminali** con menu e input controllati
 Buona **organizzazione del codice**: classi, funzioni, pulizia

---









 Bonus Avanzati (non obbligatori)
 

 1. Abilità Speciali Uniche (Polimorfismo Avanzato)
Aggiungi un metodo astratto usa_abilità_speciale() in Soldato e implementalo in ogni sottoclasse.

Esempi:

Cavaliere: assorbe metà del danno ricevuto per 1 turno

Arciere: attacca tutti i nemici contemporaneamente con danno ridotto

Guaritore: rianima un alleato caduto con metà salute (solo una volta per partita)

Mago: evoca una creatura fantasma (soldato temporaneo con 1 vita, attacco alto)

Puoi permettere una sola attivazione per round o per soldato.

 2. Posizionamento Tattico (Gestione Avanzata della Lista)
Permetti al giocatore di riordinare il proprio esercito prima del combattimento, influenzando l’ordine degli scontri. Es:

1. Sposta un soldato in alto
2. Sposta un soldato in basso
3. Conferma schieramento

Questo introduce la strategia di prima linea / seconda linea, utile per proteggere guaritori o maghi.

 3. Attacchi ad Area e Critici Multipli

Aggiungi un tipo di soldato avanzato:

Catapulta: attacco ad area → colpisce fino a 3 soldati nemici con danno 15 ciascuno

Implementa un loop per far sì che attacca() coinvolga più bersagli

 4. Effetti Status e Turni Persistenti
Implementa effetti di stato:

Avvelenamento: toglie 5 HP per 2 turni

Stordimento: salta il turno successivo

Benedizione: aumenta difesa del 50% per 1 turno"""

from abc import ABC,abstractmethod
import random

class Soldato(ABC):
    def __init__(self,nome,costo,attacco=30,difesa=60,salute=250):
        super().__init__()
        self.__nome = nome
        self.__attacco = attacco
        self.__costo = costo
        self.__difesa = difesa
        self.__salute = salute
    
    @abstractmethod
    def attacca(avversario):
        pass
    
    def difenditi(self,danno):
        danno_effettivo = max(0, danno - self.__difesa) 
        self.__salute -= danno_effettivo
        
        print(f"{self.__nome} subisce {danno_effettivo} danni. Salute: {self.__salute}")
        
        if not self.e_vivo():
            print(f"{self.__nome} è stato sconfitto!")
            
    def e_vivo(self):
        return self.__salute > 0
    
    def stato(self):
        print(f"--- STATO DI {self.__nome} ---")
        print(f"  Salute: {self.__salute}")
        print(f"  Attacco Base: {self.__attacco}")
        print(f"  Difesa Base: {self.__difesa}")
        print(f"il costo e di {self.__costo}")
        if self.e_vivo():
            print(f"  STATO: Vivo")
        else: 
            print(f"  STATO: Caduto da eroe!")

class Cavaliere(Soldato):
    def __init__(self, nome, costo=150, attacco=30, difesa=60, salute=250,colpo_critico=0.20):
        super().__init__(nome, costo, attacco, difesa, salute)
        self.__colpo_critico = colpo_critico
        
    def attacca(self,avversario):
         attacco_potenziato = self._attacco
         danno_inflitto = attacco_potenziato

         print(f"{self._nome} attacca {avversario._nome}!")
        
         if random.random() < self.__colpo_critico:
            danno_inflitto *= 2
            print(f"{self.__nome} sferra un **COLPO POTENTE**! Infligge {danno_inflitto} danni.")
         else:
            print(f"  {self.__nome} sferra un fendente normale, infliggendo {danno_inflitto} danni.")
        
         avversario.difenditi(danno_inflitto)
    
    def stato(self):
        return super().stato()
         
class Mago(Soldato):
    def __init__(self, nome, costo=50, attacco=30, difesa=60, salute=250,min_danno_magico = 10,max_danno_magico = 40,salta_turno = 0.25 ):
        super().__init__(nome, costo, attacco, difesa, salute)
        self.__min_danno_magico = min_danno_magico 
        self.__max_danno_magico = max_danno_magico
        self.__salta_turno = salta_turno
    
    def attacca(self, avversario):
        danno_inflitto = random.randint(self.__min_danno_magico, self.__max_danno_magico)
        print(f"{self._nome} lancia un incantesimo su {avversario.__nome}!")
        print(f"  L'incantesimo infligge {danno_inflitto} danni.")
        avversario.difenditi(danno_inflitto)
    
    def stato(self):
        return super().stato()    
    
    
"""def salta_turno1(self):
    mago_corrente = Mago("",0,0,0,0,0,0,0)
    if random.random() < mago_corrente:
        print(f"Il Mago {mago_corrente.__nome} è troppo stanco e salta il suo turno!")
    else:
          print(f"Il Mago {mago_corrente._nome} si prepara ad attaccare!")
          mago_corrente.attacca(avversario)"""
          
class Arciere(Soldato):
    def __init__(self, nome, costo=250, attacco=30, difesa=60, salute=250):
        super().__init__(nome, costo, attacco, difesa, salute)
    
    def attacca(self,avversario):
         danno_inflitto = self.__attacco
         print(f"{self.__nome} (Arciere) scocca una freccia verso {avversario.__nome}!")
         print(f"Infligge {danno_inflitto} danni.")
         avversario.difenditi(danno_inflitto)
    
    def stato(self):
        super().stato()
    
class Guaritore(Soldato):
    def __init__(self, nome, costo=130, attacco=30, difesa=60, salute=250,cura=50):
        super().__init__(nome, costo, attacco, difesa, salute)
        self.__cura = cura
    
    def attacca(self, alleati):
        alleati_curabili = [s for s in alleati if s.è_vivo() and s != self]
        if not alleati_curabili:
            print(f"{self.__nome} (Guaritore) non ha alleati da curare!")
            return
        bersaglio_cura = random.choice(alleati_curabili)
        cura_effettiva = self.__cura
        bersaglio_cura.__salute += cura_effettiva 
        print(f"{self.__nome} (Guaritore) cura {bersaglio_cura.__nome} per {cura_effettiva} punti salute!")
        print(f"Salute attuale di {bersaglio_cura.__nome}: {bersaglio_cura.__salute}")
    
    def stato(self):
        return super().stato()


#-----Sistema di gioco------#

class Giocatore:
    def __init__(self,nome):
        self.__nome = nome
        self.__lista_esercito = []
        self.__budget = 1000
        
    @property
    def nome(self):
        return self.__nome
    
    @property
    def budget(self):
        return self.__budget
    
    @budget.setter 
    def budget(self, valore):
        self.__budget = valore

    @property
    def esercito(self):
        return self.__lista_esercito
    
    def inserimento(self):
       self.__nome = input("inserisci il nome del giocatore: ")
       print(f"il nome del giocatore e {self.__nome}")
       return self.__nome
    COSTI_SOLDATI = {"Cavaliere": 150, "Arciere": 250,"Guaritore": 130,"Mago": 50}
    def menu_acquisto(self):
        print(f"i soldati a disposizione sono Cavaliere costo di  {Giocatore.COSTI_SOLDATI['Cavaliere']}, Arciere il costo e di  {Giocatore.COSTI_SOLDATI['Arciere']} , Guaritore il cost e di  {Giocatore.COSTI_SOLDATI['Guaritore']}, Mago il costo e di  {Giocatore.COSTI_SOLDATI['Mago']}")
        while True:
             
             scegli = input("inserisci [c]avaliere, [a]rciere, [g]uaritore, [m]ago, [e]sci: ").lower()
             if scegli == "c":
                if self.__budget > Giocatore.COSTI_SOLDATI['Cavaliere']:
                    nome_soldato_input = input("Inserisci il nome del tuo Cavaliere: ")
                    nuovo_soldato = Cavaliere(nome_soldato_input)
                    self.__lista_esercito.append(nuovo_soldato)
                    self.__budget-= Giocatore.COSTI_SOLDATI['Cavaliere']
                    print(f"il tuo soldato {nome_soldato_input} e staato aggiunto alla tua lista")
                else: 
                    print(f"non hai abbastanza soldi, ti rimangono {self.__budget}")
             elif scegli == "a":
                if self.__budget > Giocatore.COSTI_SOLDATI['Arciere']:
                    nome_soldato_input = input("Inserisci il nome del tuo Arciere: ")
                    nuovo_soldato = Arciere(nome_soldato_input)
                    self.__lista_esercito.append(nuovo_soldato)
                    self.__budget -=  Giocatore.COSTI_SOLDATI['Arciere']
                    print(f"il tuo soldato {nome_soldato_input} e staato aggiunto alla tua lista")
                else: print(f"non hai abbastanza soldi, ti rimangono {self.__budget}")
             elif scegli == "g":
                if self.__budget > Giocatore.COSTI_SOLDATI['Guaritore']:
                    nome_soldato_input = input("Inserisci il nome del tuo Guaritore: ")
                    nuovo_soldato = Guaritore(nome_soldato_input)
                    self.__lista_esercito.append(nuovo_soldato)
                    self.__budget -=  Giocatore.COSTI_SOLDATI['Guaritore']
                    print(f"il tuo soldato {nome_soldato_input} e staato aggiunto alla tua lista")
                else: print(f"non hai abbastanza soldi, ti rimangono {self.__budget}")
             elif scegli == "m":
                if self.__budget > Giocatore.COSTI_SOLDATI['Mago']:
                    nome_soldato_input = input("Inserisci il nome del tuo Mago: ")
                    nuovo_soldato = Mago(nome_soldato_input)
                    self.__lista_esercito.append(nuovo_soldato)
                    self.__budget -=  Giocatore.COSTI_SOLDATI['Mago']
                    print(f"il tuo soldato {nome_soldato_input} e staato aggiunto alla tua lista")
                else: print(f"non hai abbastanza soldi, ti rimangono {self.__budget}")
             elif scegli == "e":
                break
             else:
                print(f"Scelta non valida. Riprova.")
    
    def mostra_esercito(self):
        if not self.__lista_esercito:
            print(f"L'esercito di {self.__nome} è vuoto!")
            return

        print(f"\n--- Esercito di {self.__nome} ({len(self.__lista_esercito)} soldati) ---")
        for i, soldato in enumerate(self.__lista_esercito):
            print(f"\nSoldato {i+1}:")
            soldato.stato()
        print("---------------------------------------")
    def menu_acquisto_ia(self,tipi_soldato_disponibili):
         print(f"{self.__nome} sta acquistando rinforzi...")
         tentativi_acquisti = random.randint(1, 3)
         for indice in range(tentativi_acquisti):
             tipo_scelto = random.choice(list(tipi_soldato_disponibili.keys()))
             costo_soldato = tipi_soldato_disponibili[tipo_scelto]
             if self.budget >= costo_soldato:
                 if tipo_scelto == "Cavaliere":
                     nuovo_soldato = Cavaliere(f"IA Cavaliere {random.randint(1, 999)}")
                 elif tipo_scelto == "Arciere":
                     nuovo_soldato = Arciere(f"IA Arciere {random.randint(1, 999)}")
                 elif tipo_scelto == "Guaritore":
                     nuovo_soldato = Guaritore(f"IA Guaritore {random.randint(1, 999)}")
                 elif tipo_scelto == "Mago":
                     nuovo_soldato = Mago(f"IA Mago {random.randint(1, 999)}")
                 self.esercito.append(nuovo_soldato) 
                 self.budget -= costo_soldato
                 print(f"  {self.__nome} ha acquistato un {tipo_scelto}!")
             else:
                print(f"{self.__nome} ha terminato gli acquisti. Budget rimanente: {self.budget}")

#----Fine----#

#---Raund---#

turno = 0
giocatore_umano = Giocatore("")
ia_gio = Giocatore("IA Nemica")
ia_gio.menu_acquisto_ia()
giocatore_umano.menu_acquisto()
ia_gio.mostra_esercito()

while len(giocatore_umano.esercito) > 0 and len(ia_gio.esercito) > 0:
    turno += 1
    print(f"inizio un nuovo raund {turno}")
    