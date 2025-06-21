"""Esercizio Complesso - "Torneo del Regno"
Obiettivo
Creare un gioco da terminale in cui i partecipanti si sfidano in un torneo a eliminazione. Ogni partecipante è un combattente medievale che eredita da una classe astratta e ha caratteristiche e attacchi personalizzati. Il torneo continua finché resta un solo vincitore.

 Specifiche tecniche OOP
 Classe Astratta: Combattente
Attributi protetti: nome, salute, attacco_base, difesa_base

Metodo astratto: attacca(avversario)

Metodo: subisci_danno(danno)

Metodo: è_vivo() → True/False

Metodo: stato() → stampa salute e tipo

Classi derivate:
Cavaliere: alto attacco, difesa moderata

Attacco base + 20% probabilità di “colpo potente” (danno raddoppiato)

Arciere: attacco medio, bassa difesa

30% probabilità di “attacco doppio” consecutivo

Mago: bassa difesa, attacco variabile

Ogni attacco ha danno casuale in un intervallo (es. 10–40)

Tutte sovrascrivono attacca() con la loro logica speciale (polimorfismo).

Interazione da Terminale
L’utente crea una lista di N combattenti scegliendo tipo e nome.

Il sistema li mette in scontri casuali 1 vs 1.

Ogni scontro si svolge a turni finché uno muore.

Il vincitore avanza al turno successivo.

Alla fine si proclama il campione del torneo.

Requisiti tecnici richiesti
Uso di ABC e @abstractmethod

Polimorfismo nel metodo attacca()

Incapsulamento degli attributi (_salute, get_salute(), ecc.)

Eventuali getter/setter se necessario

Funzioni per:

Creazione partecipanti

Gestione combattimento

Avanzamento torneo

Codice ordinato, separato in classi e funzioni

Estensioni facoltative:
Barra della salute visuale con █

Recupero di un po’ di salute tra i turni

Log salvataggio degli scontri su file .txt

 Output atteso
Un programma interattivo (python torneo.py) che guida l’utente nella creazione del torneo, esegue scontri automatici a turni con log su schermo e decreta un vincitore.
"""

"""from abc import ABC, abstractmethod
import random

class Combattente(ABC):
    def __init__(self,nome,salute=500,attacco_base=10, difesa_base=50):
        super().__init__()
        self.__nome = nome
        self.__salute = salute
        self.__attacco_base = attacco_base
        self.__difesa_base = difesa_base
        
    def get_nome(self):
        return self.__nome

    def set_nome(self, valore):
        self.__nome = valore
            
    def get_salute(self):
        return self.__salute

    def set_salute(self, valore):
        self.__salute = valore
        
    def get_attacco_base(self):
        return self.__attacco_base

    def set_attacco_base(self, valore):
        self.__attacco_base = valore
        
    def get_difesa_base(self):
        return self.__difesa_base

    def set_difesa_base(self, valore):
        self.__difesa_base = valore
        
    @abstractmethod
    def attacca(self,avversario):
        pass
        
    def subisci_danno(self,danno):
        self.__salute -= danno
        if self.__salute > 5:
            print(f"la tua salute e {self.get_salute()} puoi combatere")
        elif self.__salute > 0 and self.get_salute <= 5:
            print(f" la tua solute e {self.get_salute()} stai attento")
        elif self.__salute == 0:
            print("morto")
        elif self.__salute < 0:
            print("valore non consentito")
        
    def  e_vivo(self):
        return self.get_salute() > 0
                     
    def stato(self):
        print(f"il combatente {self.get_nome()}")
        print(f"la salute e:{self.get_salute()}")
        print(f"la difesa e:{self.get_difesa_base()}")
        print(f"l accatto e:{self.get_attacco_base()}")
        if self.e_vivo():
            print(f"e vivo {self.get_nome()}")
        else: print("e morto da eroe!")

class Cavaliere(Combattente):
    def __init__(self, nome, salute, attacco_base, difesa_base,prob_colpo_potente=0.20):
        super().__init__(nome, salute, attacco_base, difesa_base)
        self.__prob_colpo_potente = prob_colpo_potente
        
    def attacca(self,avversario):
        attacco = self.get_attacco_base()
        danno_inflitto = attacco
        
        if random.random() <= self.__prob_colpo_potente:
            attacco *=2
            print(f"{self.get_nome()} sferra un COLPO POTENTE! Danno raddoppiato! a {avversario.get_nome()}")
        else:  print(f"{self.get_nome()} attacca con un fendente normale.a {avversario.get_nome()}")
        avversario.subisci_danno(danno_inflitto)
        
    def subisci_danno(self, danno):
        super().subisci_danno(danno)

class Arciere(Combattente):
    def __init__(self, nome, salute, attacco_base, difesa_base, prob_attacco_consecutivo=0.30):
        super().__init__(nome, salute, attacco_base, difesa_base)
        self.__prob_attacco_consecutivo = prob_attacco_consecutivo        
    def attacca(self,avversario):
        attacco = self.get_attacco_base
        danno_inflitto = attacco
        
        if random.random() <= 0.30 and random.random() < self.__prob_attacco_consecutivo:
            attacco *=2
            print(f"{self.get_nome()} sferra un ATTACCO DOPPIO Danno raddoppiato! a {avversario.get_nome()}")
        else:  print(f"{self.get_nome()} sferra attacca normale. a {avversario.get_nome()}")
        avversario.subisci_danno(danno_inflitto)
        
    def subisci_danno(self, danno):
        super().subisci_danno(danno)
        
class Mago(Combattente):
    def __init__(self, nome, salute, attacco_base, difesa_base,min_danno_magico=10,max_danno_magico=40):
        super().__init__(nome, salute, attacco_base, difesa_base)
        self.__min_danno_magico = min_danno_magico
        self.__max_danno_magico = max_danno_magico
        
    def attacca(self,avversario):
        danno_inflitto = random.randint(self.__min_danno_magico, self.__max_danno_magico)
        
        print(f"{self.get_nome} sferra un ATTACCO MAGICO! a {avversario.get_nome()}")
        print(f"{self.get_nome} sferra attacca normale.")
        avversario.subisci_danno(danno_inflitto)
        
    def subisci_danno(self, danno):
        super().subisci_danno(danno)
        
def crea_partecipanti():
    combattenti = []
    num_combattenti = 0
    while num_combattenti < 2: 
        try:
            num_combattenti = int(input("Quanti combattenti parteciperanno (min. 2)? "))
            if num_combattenti < 2:
                print("Devi avere almeno 2 combattenti per il torneo.")
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")
    for i in range(num_combattenti):
        while True: 
            nome = input(f"Inserisci il nome del Combattente {i+1}: ").strip()
            tipi_validi = {"c": Cavaliere, "a": Arciere, "m": Mago}
            tipo = input("in serisci il tipo del perssonaggio [c]avaliere,[a]rciere,[m]ago: ").lower()
            if tipo == tipi_validi["c"]:
                salute1=120
                attacco =18
                difesa=8
                nuovo_combattente = Cavaliere(nome=nome, salute=salute1, attacco_base=attacco,difesa_base=difesa)
            elif tipo == tipi_validi["a"]:
                salute1=90
                attacco=22
                difesa=8
                nuovo_combattente = Arciere(nome=nome, salute=salute1, attacco_base=attacco,difesa_base=difesa)
            elif tipo == "m":
                salute1=80
                attacco=15
                difesa=5
                nuovo_combattente = Mago(nome=nome, salute=salute1, attacco_base=attacco,difesa_base=difesa)
            else:
                print("Tipo non valido. Scegli tra [C]avaliere, [A]rciere, [M]ago.")
                continue 
            combattenti.append(nuovo_combattente) 
            print(f"{nome} il {nuovo_combattente.get_tipo()} si unisce al torneo!")
   
    print("\n--- Partecipanti al Torneo ---")
    for c in combattenti:
        c.stato() 
    return combattenti 

def avanza_torneo(partecipanti):
    turno = 1
    combattenti_attivi = list(partecipanti) # Copia la lista iniziale

    while len(combattenti_attivi) > 1:
        print(f"\n--- INIZIO TURNO {turno} ---")
        print(f"Combattenti rimasti ({len(combattenti_attivi)}): {[c.get_nome() for c in combattenti_attivi]}")
        
        random.shuffle(combattenti_attivi) # Mescola i combattenti
        vincitori_turno = []
        
        # Gestione del "bye" (se numero dispari, il primo avanza senza combattere)
        if len(combattenti_attivi) % 2 != 0:
            bye_combattente = combattenti_attivi.pop(0) # Rimuove e prende il primo
            vincitori_turno.append(bye_combattente)
            print(f"{bye_combattente.get_nome()} riceve un bye e avanza al turno successivo!")

        # Svolgimento degli scontri 1 vs 1
        for i in range(0, len(combattenti_attivi), 2):
            c1 = combattenti_attivi[i]
            c2 = combattenti_attivi[i+1]

            print(f"\n----- Scontro: {c1.get_nome()} ({c1.get_tipo()}) vs {c2.get_nome()} ({c2.get_tipo()}) -----")
            
            # Combattimento a turni finché uno dei due muore
            while c1.e_vivo() and c2.e_vivo():
                c1.attacca(c2)
                if not c2.e_vivo(): # Se c2 muore, c1 vince
                    break 
                c2.attacca(c1)
            
            # Determina e annuncia il vincitore dello scontro
            if c1.e_vivo():
                vincitore = c1
            else:
                vincitore = c2
            
            print(f"\n{vincitore.get_nome()} ha vinto lo scontro!")
            vincitori_turno.append(vincitore) # Aggiunge il vincitore alla lista per il prossimo turno

        combattenti_attivi = vincitori_turno # I vincitori diventano i partecipanti del prossimo turno
        turno += 1
        
    # Annuncio del campione
    if combattenti_attivi:
        campione = combattenti_attivi[0]
        print("\n\n#############################################")
        print(f"IL CAMPIONE DEL TORNEO È: {campione.get_nome()} il {campione.get_tipo()}!!! 🏆")
        print("#############################################")
        campione.stato()
    else:
        print("\nIl torneo è terminato senza un vincitore (qualcosa non ha funzionato).")

# --- Funzione Principale per Avviare il Gioco ---
def main():
    print("Benvenuti al Torneo del Regno!")
    combattenti_iniziali = crea_partecipanti() 
    
    if len(combattenti_iniziali) >= 2: 
        avanza_torneo(combattenti_iniziali) # Avvia il torneo
    else:
        print("Non ci sono abbastanza combattenti per iniziare il torneo (minimo 2).")

main()"""

import random
from abc import ABC, abstractmethod
import math # Necessario per math.ceil per la barra della salute

class Combattente(ABC):
    # Ho aggiunto __salute_massima qui
    def __init__(self, nome, salute, attacco_base, difesa_base):
        self.__nome = nome
        self.__salute_massima = salute # Memorizza la salute massima iniziale
        self.__salute = salute
        self.__attacco_base = attacco_base
        self.__difesa_base = difesa_base
        self.__tipo = self.__class__.__name__ # Ottiene il nome della classe (Cavaliere, Arciere, Mago)
        
    def get_nome(self):
        return self.__nome

    def set_nome(self, valore):
        self.__nome = valore
            
    def get_salute(self):
        return self.__salute

    def set_salute(self, valore):
        # Assicura che la salute non superi la massima e non scenda sotto zero
        if valore > self.__salute_massima:
            self.__salute = self.__salute_massima
        elif valore < 0:
            self.__salute = 0
        else:
            self.__salute = valore
            
    def get_salute_massima(self):
        return self.__salute_massima

    def get_attacco_base(self):
        return self.__attacco_base

    def set_attacco_base(self, valore):
        self.__attacco_base = valore
            
    def get_difesa_base(self):
        return self.__difesa_base

    def set_difesa_base(self, valore):
        self.__difesa_base = valore
    
    def get_tipo(self):
        return self.__tipo
            
    @abstractmethod
    def attacca(self, avversario):
        pass
            
    def subisci_danno(self, danno):
        danno_effettivo = max(0, danno - self.get_difesa_base()) 
        self.set_salute(self.get_salute() - danno_effettivo) 
        
        print(f"  ({self.get_nome()} il {self.get_tipo()}) subisce {danno_effettivo} danni. Salute: {self.get_salute()}/{self.get_salute_massima()} {self.barra_salute()}")
        
        if not self.e_vivo():
            print(f"  💀 {self.get_nome()} è stato sconfitto!")
            
    def e_vivo(self):
        return self.get_salute() > 0
                             
    def stato(self):
        print(f"--- STATO DI {self.get_nome()} ({self.get_tipo()}) ---")
        print(f"  Salute: {self.get_salute()}/{self.get_salute_massima()} {self.barra_salute()}")
        print(f"  Attacco Base: {self.get_attacco_base()}")
        print(f"  Difesa Base: {self.get_difesa_base()}")
        if self.e_vivo():
            print(f"  STATO: Vivo")
        else: 
            print(f"  STATO: Caduto da eroe!")

    def barra_salute(self):
        lunghezza_barra = 20
        salute_attuale = self.get_salute()
        salute_max = self.get_salute_massima()
        
        blocchi_pieni = math.ceil((salute_attuale / salute_max) * lunghezza_barra) if salute_max > 0 else 0
        blocchi_vuoti = lunghezza_barra - blocchi_pieni
        
        barra = "█" * blocchi_pieni + "░" * blocchi_vuoti 
        return f"[{barra}]"

class Cavaliere(Combattente):
    def __init__(self, nome, salute=120, attacco_base=18, difesa_base=12): 
        super().__init__(nome, salute, attacco_base, difesa_base)
        self.__prob_colpo_potente = 0.20 
        
    def attacca(self, avversario):
        attacco_power = self.get_attacco_base()
        danno_inflitto = attacco_power

        print(f"\n⚔️ {self.get_nome()} attacca {avversario.get_nome()}!")
        
        if random.random() < self.__prob_colpo_potente:
            danno_inflitto *= 2
            print(f"  🗡️ {self.get_nome()} sferra un **COLPO POTENTE**! Infligge {danno_inflitto} danni.")
        else:
            print(f"  {self.get_nome()} sferra un fendente normale, infliggendo {danno_inflitto} danni.")
        
        avversario.subisci_danno(danno_inflitto)

class Arciere(Combattente):
    def __init__(self, nome, salute=90, attacco_base=22, difesa_base=8): 
        super().__init__(nome, salute, attacco_base, difesa_base)
        self.__prob_attacco_doppio = 0.30 
        
    def attacca(self, avversario):
        print(f"\n🏹 {self.get_nome()} attacca {avversario.get_nome()}!")
        
        self._esegui_singolo_attacco_arciere(avversario)

        if self.e_vivo() and avversario.e_vivo() and random.random() < self.__prob_attacco_doppio:
            print(f"  🎯 {self.get_nome()} ottiene un **ATTACCO DOPPIO** consecutivo!")
            self._esegui_singolo_attacco_arciere(avversario)

    def _esegui_singolo_attacco_arciere(self, avversario):
        danno_base = self.get_attacco_base() 
        print(f"  {self.get_nome()} scocca una freccia infliggendo {danno_base} danni.")
        avversario.subisci_danno(danno_base)
        
class Mago(Combattente):
    def __init__(self, nome, salute=80, attacco_base=15, difesa_base=5): 
        super().__init__(nome, salute, attacco_base, difesa_base)
        self.__min_danno_magico = 10 
        self.__max_danno_magico = 40
        
    def attacca(self, avversario):
        danno_inflitto = random.randint(self.__min_danno_magico, self.__max_danno_magico)
        
        print(f"\n✨ {self.get_nome()} lancia un incantesimo su {avversario.get_nome()}!")
        print(f"  L'incantesimo infligge {danno_inflitto} danni.")
        
        avversario.subisci_danno(danno_inflitto)

        
# --- Funzione per la Creazione dei Partecipanti ---
def crea_partecipanti():
    combattenti = [] 
    print("\n--- CREAZIONE DEI PARTECIPANTI AL TORNEO ---")
    
    num_combattenti = 0
    while num_combattenti < 2: 
        try:
            num_combattenti = int(input("Quanti combattenti parteciperanno (min. 2)? "))
            if num_combattenti < 2:
                print("Devi avere almeno 2 combattenti per il torneo.")
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")

    tipi_validi = {"c": "Cavaliere", "a": "Arciere", "m": "Mago"}
    print("Tipi di combattenti disponibili: [C]avaliere, [A]rciere, [M]ago")

    for i in range(num_combattenti):
        while True: 
            nome = input(f"Inserisci il nome del Combattente {i+1}: ").strip()
            if not nome:
                print("Il nome non può essere vuoto. Riprova.")
                continue
            if any(c.get_nome().lower() == nome.lower() for c in combattenti):
                print(f"Il nome '{nome}' è già stato preso. Scegli un altro nome.")
                continue
            break 
            
        while True: 
            tipo_input = input(f"Scegli il tipo per {nome} ([C]avaliere/[A]rciere/[M]ago): ").strip().lower()
            
            nuovo_combattente = None
            if tipo_input == "c":
                nuovo_combattente = Cavaliere(nome, salute=120, attacco_base=18, difesa_base=12)
            elif tipo_input == "a":
                nuovo_combattente = Arciere(nome, salute=90, attacco_base=22, difesa_base=8)
            elif tipo_input == "m": 
                nuovo_combattente = Mago(nome, salute=80, attacco_base=15, difesa_base=5) 
            else:
                print("Tipo non valido. Scegli tra [C]avaliere, [A]rciere, [M]ago.")
                continue
            
            combattenti.append(nuovo_combattente) 
            print(f"🎉 {nome} il {nuovo_combattente.get_tipo()} si unisce al torneo!")
            break 
    
    print("\n--- Partecipanti al Torneo ---")
    for c in combattenti:
        c.stato() 
    return combattenti 

# --- Funzione del Torneo Semplificata ---
def avanza_torneo(partecipanti):
    turno = 1
    combattenti_attivi = list(partecipanti) # Copia la lista iniziale

    while len(combattenti_attivi) > 1:
        print(f"\n--- INIZIO TURNO {turno} ---")
        print(f"Combattenti rimasti ({len(combattenti_attivi)}): {[c.get_nome() for c in combattenti_attivi]}")
        
        random.shuffle(combattenti_attivi) # Mescola i combattenti
        vincitori_turno = []
        
        # Gestione del "bye" (se numero dispari, il primo avanza senza combattere)
        if len(combattenti_attivi) % 2 != 0:
            bye_combattente = combattenti_attivi.pop(0) # Rimuove e prende il primo
            vincitori_turno.append(bye_combattente)
            print(f"📢 {bye_combattente.get_nome()} riceve un bye e avanza al turno successivo!")

        # Svolgimento degli scontri 1 vs 1
        for i in range(0, len(combattenti_attivi), 2):
            c1 = combattenti_attivi[i]
            c2 = combattenti_attivi[i+1]

            print(f"\n----- Scontro: {c1.get_nome()} ({c1.get_tipo()}) vs {c2.get_nome()} ({c2.get_tipo()}) -----")
            
            # Combattimento a turni finché uno dei due muore
            while c1.e_vivo() and c2.e_vivo():
                c1.attacca(c2)
                if not c2.e_vivo(): # Se c2 muore, c1 vince
                    break 
                c2.attacca(c1)
            
            # Determina e annuncia il vincitore dello scontro
            if c1.e_vivo():
                vincitore = c1
            else:
                vincitore = c2
            
            print(f"\n🎉 {vincitore.get_nome()} ha vinto lo scontro!")
            vincitori_turno.append(vincitore) # Aggiunge il vincitore alla lista per il prossimo turno

        combattenti_attivi = vincitori_turno # I vincitori diventano i partecipanti del prossimo turno
        turno += 1
        
    # Annuncio del campione
    if combattenti_attivi:
        campione = combattenti_attivi[0]
        print("\n\n#############################################")
        print(f"🏆 IL CAMPIONE DEL TORNEO È: {campione.get_nome()} il {campione.get_tipo()}!!! 🏆")
        print("#############################################")
        campione.stato()
    else:
        print("\nIl torneo è terminato senza un vincitore (qualcosa non ha funzionato).")

# --- Funzione Principale per Avviare il Gioco ---
def main():
    print("Benvenuti al Torneo del Regno!")
    combattenti_iniziali = crea_partecipanti() 
    
    if len(combattenti_iniziali) >= 2: 
        avanza_torneo(combattenti_iniziali) # Avvia il torneo
    else:
        print("Non ci sono abbastanza combattenti per iniziare il torneo (minimo 2).")

if __name__ == "__main__":
    main()