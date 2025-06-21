"""creare una classe base Veicolo con attributi comuni a tutti i veicoli e metodi per operazioni comuni come l'accensione e lo spegnimento. Derivando questa classe, creeranno specifiche classi per Auto, Furgone e Motocicletta, aggiungendo caratteristiche uniche per ciascun tipo di veicolo. Infine, dovranno implementare una classe GestoreParcoVeicoli per amministrare l'insieme dei veicoli.

Classe Veicolo:
Attributi privati:
_marca (stringa)
_modello (stringa)
_anno (intero)
_accensione (booleano)
Metodi:
accendi(): cambia lo stato di _accensione a vero.
spegni(): cambia lo stato di _accensione a falso.
Classi Derivate:
Auto:
Attributi aggiuntivi come _numero_porte
Metodo specifico come suona_clacson()
Furgone:
Attributi per _capacità_carico
Metodo per carica() e scarica()
Motocicletta:
Attributo per _tipo (e.g., sportiva, touring)
Metodo per esegui_wheelie() se il tipo è sportivo
Classe GestoreParcoVeicoli:
Attributi:
_veicoli: lista di tutti i veicoli.
Metodi:
aggiungi_veicolo(veicolo): aggiunge un veicolo alla lista.
rimuovi_veicolo(marca, modello): rimuove un veicolo specifico dalla lista.
lista_veicoli(): stampa un elenco di tutti i veicoli nel parco."""

class Veicolo:
    def __init__(self, _marca, _modello, _anno, _accensione):
        self._marca = _marca
        self._modello = _modello
        self._anno = _anno
        self._accensione = _accensione

    def accendi(self):
        # CORRETTO: Modifica l'attributo _accensione
        if not self._accensione:
            self._accensione = True
            print(f"Il veicolo {self._marca} {self._modello} è acceso.")
        else:
            print(f"Il veicolo {self._marca} {self._modello} è già acceso.")

    def spegni(self):
        # CORRETTO: Modifica l'attributo _accensione
        if self._accensione:
            self._accensione = False
            print(f"Il veicolo {self._marca} {self._modello} è spento.")
        else:
            print(f"Il veicolo {self._marca} {self._modello} è già spento.")

    def __str__(self):
        stato = "acceso" if self._accensione else "spento"
        return f"Veicolo: {self._marca} {self._modello} ({self._anno}), Stato: {stato}"

    def get_marca(self):
        return self._marca

    def get_modello(self):
        return self._modello

    def is_accensione(self):
        return self._accensione

    def get_anno(self):
        return self._anno


class Auto(Veicolo):
    def __init__(self, _marca, _modello, _anno, _accensione, _numero_porte):
        super().__init__(_marca, _modello, _anno, _accensione)
        self._numero_porte = _numero_porte

    def suona_clacson(self):
        print("Il suono del clacson: BEEEP! BEEEP!")

    def __str__(self):
        return f"Auto: {self._marca} {self._modello} ({self._anno}), Porte: {self._numero_porte}, Stato: {'acceso' if self._accensione else 'spento'}"

    def get_numero_porte(self):
        return self._numero_porte


class Furgone(Veicolo):
    def __init__(self, _marca, _modello, _anno, _accensione, _capacita_carico):
        super().__init__(_marca, _modello, _anno, _accensione)
        self._capacita_carico = _capacita_carico
        self._batteria_carica = False # NUOVO ATTRIBUTO per lo stato della batteria

    def carica(self): # CORRETTO: Rimosso 'batteria' come parametro
        risposta = input("La batteria del furgone è [s]carica o [c]arica? (c/s): ").lower()
        if risposta == "c":
            if not self._batteria_carica:
                self._batteria_carica = True
                print("La batteria del furgone è ora carica.")
            else:
                print("La batteria del furgone è già carica.")
        elif risposta == "s":
            print("Hai detto che è scarica, quindi non la carico.")
        else:
            print("Input non valido.")
        return self._batteria_carica # Ritorna lo stato dell'attributo

    def scarica(self): # CORRETTO: Rimosso 'batteria' come parametro
        risposta = input("La batteria del furgone è [s]carica o [c]arica? (c/s): ").lower()
        if risposta == "s":
            if self._batteria_carica:
                self._batteria_carica = False
                print("La batteria del furgone è ora scarica.")
            else:
                print("La batteria del furgone è già scarica.")
        elif risposta == "c":
            print("Hai detto che è carica, quindi non la scarico.")
        else:
            print("Input non valido.")
        return self._batteria_carica # Ritorna lo stato dell'attributo

    def __str__(self):
        # CORRETTO: Usa self._batteria_carica
        stato_batteria = "carica" if self._batteria_carica else "scarica"
        return f"Furgone: {self._marca} {self._modello} ({self._anno}), Carico: {self._capacita_carico}, Batteria: {stato_batteria}, Stato: {'acceso' if self._accensione else 'spento'}"

    def get_capacita_carico(self):
        return self._capacita_carico

class Motocicletta(Veicolo):
    def __init__(self, _marca, _modello, _anno, _accensione, _tipo):
        super().__init__(_marca, _modello, _anno, _accensione)
        self._tipo = _tipo

    def esegui_wheelie(self):
        if self._tipo.lower() == "sportivo":
            print("Hai una bella moto sportiva! Esegui il wheelie con stile!")
        else:
            # CORRETTO: Messaggio più neutrale
            print("Il tipo di moto non è sportivo, potresti non essere adatto a un wheelie... Attenzione!")

    def __str__(self):
        return f"Motocicletta: {self._marca} {self._modello} ({self._anno}), Tipo: {self._tipo}, Stato: {'acceso' if self._accensione else 'spento'}"

    def get_tipo(self):
        return self._tipo

class GestoreParcoVeicoli:
    def __init__(self):
        self._veicoli = []

    def aggiungi_veicolo(self, veicolo):
        if isinstance(veicolo, Veicolo):
            self._veicoli.append(veicolo)
            print(f"Veicolo {veicolo.get_marca()} {veicolo.get_modello()} aggiunto con successo al parco!") # Usiamo i getter
        else:
            print("Errore: Puoi aggiungere solo oggetti di tipo Veicolo al parco.")

    def rimuovi_veicolo(self, marca, modello):
        veicolo_trovato = None
        for veicolo in self._veicoli:
            if veicolo.get_marca() == marca and veicolo.get_modello() == modello: # Usiamo i getter
                veicolo_trovato = veicolo
                break

        if veicolo_trovato:
            self._veicoli.remove(veicolo_trovato)
            print(f"Veicolo {marca} {modello} è stato eliminato con successo!")
            return True
        else:
            print(f"Errore: Veicolo {marca} {modello} non trovato nel parco.")
            return False

    def lista_veicoli(self):
        print("\n--- Lista di tutti i veicoli nel parco ---")
        if not self._veicoli:
            print("Il parco veicoli è vuoto.")
            return
        for veicol in self._veicoli:
            print(f"- {veicol}") # Il metodo __str__ di ogni veicolo verrà usato
        print("------------------------------")


# --- Sezione di Test Migliorata ---

print("---Veicoli---")
marca = "fiat 500"
modello = "500 si vola"
anno = 1999
accensione = True # Inizialmente acceso
veic = Veicolo(_marca=marca, _modello=modello, _anno=anno, _accensione=accensione)
veic.accendi() # Sarà "già acceso"
veic.spegni() # Ora si spegne
print(f"Stato finale Veicolo: {veic}")

print("\n---Auto---")
marca = "lambogo v33"
modello = "ricchi da ricchi"
anno = 2023
accensione = False # Inizialmente spenta
porte = 4
aut = Auto(_marca=marca, _modello=modello, _anno=anno, _accensione=accensione, _numero_porte=porte)
aut.accendi() # Ora si accende
aut.spegni() # Ora si spegne
aut.suona_clacson()
print(f"Stato finale Auto: {aut}")

print("\n---Furgone---")
marca = "fugone e via 2000"
modello = "limone signoraaaaaa"
anno = 3000
accensione = False
capacita_carico = "limone"
fugo = Furgone(_marca=marca, _modello=modello, _anno=anno, _accensione=accensione, _capacita_carico=capacita_carico)
fugo.spegni() # Sarà "già spento"
fugo.accendi() # Ora si accende
fugo.carica() # Chiede input per caricare la batteria
fugo.scarica() # Chiede input per scaricare la batteria
print(f"Stato finale Furgone: {fugo}")


print("\n---Motocicleta---")
marca = "sto fisico bestiale"
modello = "che guardi povero"
anno = 2000
accensione = True
tipo1 = "sportiva"
tipo2 = "touring"
moto = Motocicletta(_marca=marca, _modello=modello, _anno=anno, _accensione=accensione, _tipo=tipo1)
moto1 = Motocicletta(_marca=marca, _modello=modello, _anno=anno, _accensione=accensione, _tipo=tipo2)
moto.accendi() # Sarà "già accesa"
moto.esegui_wheelie()
moto.spegni() # Ora si spegne
print(f"Stato finale Moto (tipo1): {moto}")
print(f"Stato finale Moto (tipo2): {moto1}")

print("\n---Gestore del Parco dei Veicoli---")
gest = GestoreParcoVeicoli() # Nessun argomento, corretto!
gest.aggiungi_veicolo(veic)
gest.aggiungi_veicolo(aut)
gest.aggiungi_veicolo(fugo)
gest.aggiungi_veicolo(moto)
gest.aggiungi_veicolo(moto1)

gest.lista_veicoli() # Questa chiamata dovrebbe ora stampare i veicoli!

# Test rimozione
print("\n--- Rimozione di un veicolo ---")
gest.rimuovi_veicolo(marca="sto fisico bestiale", modello="che guardi povero") # Tenterà di rimuovere la moto 'moto'
gest.lista_veicoli() # Dovrebbe mostrare la lista aggiornata senza la moto rimossa

print("\n--- Tentativo di rimuovere un veicolo inesistente ---")
gest.rimuovi_veicolo(marca="MarcaInesistente", modello="ModelloInesistente")
gest.lista_veicoli()

print("\n--- Fine del programma ---")