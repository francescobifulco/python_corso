"""creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di 
pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi 
di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla 
classe base.

Classe MetodoPagamento:
Metodi:
effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
Classi Derivate:
CartaDiCredito:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
PayPal:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
BonificoBancario:
Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
GestorePagamenti:
Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del 
metodo di pagamento.
"""

class MetodoPagamento:
    def effettua_pagamento(self,importo):
        pass
    
class CartaDiCredito(MetodoPagamento):
    def __init__(self,numero_carta,data_scadenza,cvv):
        super().__init__()
        self.numero_carta = numero_carta
        self.data_scadenza = data_scadenza
        self.cvv = cvv
        
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        if importo <= 0:
            print("L'importo del pagamento deve essere positivo.")
            return False
        print(f"Pagamento con Carta di Credito di {importo}€ effettuato.")
        return True
    def __str__(self):
        return f"Carta di Credito (finale {self.numero_carta[-4:]})"
    
class PayPal(MetodoPagamento):
    def __init__(self,email,account):
        super().__init__()
        self.email = email
        self.account = account
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        if importo <= 0:
            print("L'importo del pagamento deve essere positivo.")
            return False
        print(f"Pagamento con PayPal di {importo}€ effettuato. con {self.email} e del account {self.account}")
    def __str__(self):
        return f"PayPal (email: {self.email})"
    
class BonificoBancario(MetodoPagamento):
    def __init__(self,beneficiario,iban):
        super().__init__()
        self.beneficiario = beneficiario
        self.iban = iban 
    def effettua_pagamento(self, importo):
        super().effettua_pagamento(importo)
        if importo <= 0:
            print("L'importo del pagamento deve essere positivo.")
            return False
        print(f"Pagamento con Bonifico Bancario di {importo}€ effettuato. dal bonifico {self.beneficiario} del ibam {self.iban}")
    def __str__(self):
        return f"Bonifico Bancario (IBAN: {self.iban})"

class GestorePagamenti:
    def __init__(self):
        self.metodi_di_pagamento_registrati = [
            CartaDiCredito("4111-2222-3333-4444", "12/28", "123"),
            PayPal("utente.generico@example.com", "ID_XYZ789"),
            BonificoBancario("Azienda Alpha", "IT60X0542811101000000123456")
        ]
    def aggiungi_metodo(self, nuovo_metodo):
        if isinstance(nuovo_metodo, MetodoPagamento):
            self.metodi_di_pagamento_registrati.append(nuovo_metodo)
            print(f"Metodo '{str(nuovo_metodo)}' aggiunto.")
        else:
            print("Errore: Non è un metodo di pagamento valido.")
    
    def mostra_metodi_disponibili(self):
        print("\n--- Metodi di Pagamento Disponibili ---")
        if not self.metodi_di_pagamento_registrati:
            print("Nessun metodo di pagamento configurato.")
            return
        for i, metodo in enumerate(self.metodi_di_pagamento_registrati):
            print(f"{i + 1}. {str(metodo)}") # Stampa l'opzione numerata
        print("---------------------------------------")
    
    def elabora_pagamento(self, importo, scelta_utente_metodo):
        if not self.metodi_di_pagamento_registrati:
            print("Nessun metodo di pagamento disponibile.")
            return False
        try:
            indice_scelto = int(scelta_utente_metodo) - 1             
            if not (0 <= indice_scelto < len(self.metodi_di_pagamento_registrati)):
                print("Scelta non valida: numero metodo non trovato.")
                return False
        except ValueError:
            print("Input non valido: inserisci un numero per il metodo.")
            return False
        metodo_selezionato = self.metodi_di_pagamento_registrati[indice_scelto]
        print(f"\nProvando a pagare {importo:.2f}€ con: {str(metodo_selezionato)}")
        return metodo_selezionato.effettua_pagamento(importo)


while True: 
    mio_cassiere = GestorePagamenti() 
    mio_cassiere.mostra_metodi_disponibili() 
    print("\nCosa desideri fare?")
    print("1. Effettuare un pagamento")
    print("2. Uscire dal negozio")
    scelta_menu = input("Scegli un'opzione: ")
    if scelta_menu == '1':
        try:
            importo_str = input("Quanto vuoi pagare? ")
            importo = float(importo_str) 
            if importo <= 0:
                print("L'importo deve essere positivo.")
                continue
            metodo_scelto = input("Scegli il numero del metodo di pagamento (es. 1, 2, 3): ")
            pagamento_riuscito = mio_cassiere.elabora_pagamento(importo, metodo_scelto)
            if pagamento_riuscito:
                print("--- Pagamento completato! ---")
            else: print("--- Pagamento NON riuscito. ---")
        except ValueError: print("Input non valido per l'importo. Inserisci un numero.")    
    elif scelta_menu == '2':
        print("Grazie e arrivederci!")
        break 
    else:print("Opzione non valida. Riprova.")