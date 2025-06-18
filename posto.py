"""Classe Posto:
Attributi privati:
_numero (intero: numero del posto)
_fila (stringa: fila in cui si trova il posto)
_occupato (booleano: stato del posto, se è occupato o meno)
Metodi:
prenota(): prenota il posto se non è già occupato.
libera(): libera il posto se è occupato.
Getter per numero e fila, e uno stato che indica se il posto è occupato.
Classi Derivate:
PostoVIP:
Aggiunge un attributo per servizi_extra (e.g., accesso al lounge, servizio in posto).
Sovrascrive il metodo prenota() per includere la gestione dei servizi extra.
PostoStandard:
Potrebbe avere un costo aggiuntivo per la prenotazione online o altri servizi meno esclusivi.
Classe Teatro:
Attributi:
_posti: lista di tutti i posti nel teatro.
Metodi:
prenota_posto(numero, fila): trova e prenota un posto specifico.
stampa_posti_occupati(): mostra tutti i posti occupati.
"""

class Posto:
    def __init__(self,_numero,_fila,_occupato=False):
        self._numero = _numero
        self._fila = _fila
        self._occupato = _occupato
    def prenota(self):
        #prenota_posto = int(input("inserisci il numero di posto:"))
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato.")
            return True
        else:
            print(f"Il posto {self._fila}{self._numero} è già occupato.")
            return False
        
    def libera(self):
        if self._occupato:
            self._occupato = False
            print("il posto si e liberato")
            return True
        else: print("il posto e gia libero")
        return False
    
    def get_numero(self):
        return self._numero
    def get_fila(self):
        return self._fila
    def is_occupato(self):
        return self._occupato

class PostoVIP(Posto):
    def __init__(self, _numero, _fila, _occupato,servizi_extra):
        super().__init__(_numero, _fila, _occupato)
        self.servizi_extra = servizi_extra
    def prenota(self):
        super().prenota()
        print("i servizi extra sono accesso lounge, drink, servizio in posto")
class PostoStandard(Posto):
     def __init__(self, _numero, _fila, _occupato,costo_base=10.0, commissione_online=1.0):
         super().__init__(_numero, _fila, _occupato)
         self.costo_base = costo_base
         self.commissione_online = commissione_online
     def prenota(self,prenotazione_online=False): 
         if super().prenota():
             if not self._occupato:
                 self._occupato = True
                 prezzo_totale = self.costo_base
                 if prenotazione_online:
                     prezzo_totale += self.commissione_online
                     print(f"Posto Standard {self._fila}{self._numero} prenotato con costo online. Totale: {prezzo_totale}€")
                 else:
                     print(f"Posto Standard {self._fila}{self._numero} prenotato. Totale: {prezzo_totale}€")
                 return True
         else:
            print(f"Il posto {self._fila}{self._numero} è già occupato.")
            return False

class Teatro(Posto):
    def __init__(self, _numero, _fila, _occupato=False):
        super().__init__(_numero, _fila, _occupato)
        self._posti = []
    
    def prenota_posto(self,numero, fila):
        posto_trovato = None
        for posto in self._posti:
            if posto._numero == numero and posto._fila == fila:
                posto_trovato = posto 
                break
        if posto_trovato:
            if isinstance(posto_trovato, PostoStandard):
                return posto_trovato.prenota(prenotazione_online=True)
            else:
                return posto_trovato.prenota()
        else:
            print(f"Errore: Posto {fila}{numero} non trovato nel teatro.")
            return False
    def stampa_posti_occupati(self):
         print("\n--- Posti Occupati nel Teatro ---")
         occupato = False
         for posto in self._posti:
            if posto.is_occupato():
                print(f"Posto {posto.get_fila()}{posto.get_numero()} - Occupato")
                occupato = True
         if not occupato:
            print("Nessun posto è attualmente occupato.")
         print("------------------------------")
                

numero=input("numero di posti: ")
fila=input("numero fila: ")
occupato=True
teatro = Posto(numero,fila ,occupato)
teatro.prenota()
teatro.libera()
servizi_extra = input("")
vip = PostoVIP(numero, fila,occupato,servizi_extra)
vip.libera()
vip.prenota()

base = 30
online = 39
prenota=False
standart = PostoStandard(numero, fila,occupato,base,online)
standart.libera()
standart.prenota(prenota)

terzo = Teatro(numero,fila ,occupato)
terzo.prenota_posto(numero, fila)
terzo.stampa_posti_occupati()
