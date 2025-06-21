"""creare una classe ContoBancario che incapsula le informazioni di un conto e fornisce metodi per gestire il saldo in modo sicuro. L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
titolare (stringa che rappresenta il nome del titolare del conto)
saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota)."""

class ContoBancario:
    def __init__(self,titolare,saldo):
        self.__titolare = titolare
        self.__saldo = saldo
    def deposita(self,importo):
        if importo > 0:
            self.__saldo += importo
            print("importo aggiornato")
        else: print("importo non aggiornato perche e negativo")
    def visualizza_saldo(self):
        print(f"Saldo attuale: {self.__saldo}")
    def preleva(self,importo):
        if importo < self.__saldo:
            print("puoi prevelare")
            if importo > 0:
                self.__saldo -= importo
                print("importo aggiornato")
            else: print("importo non aggiornato perche e negativo")
        else: print("non ci sono fonti sei povero")
    def get_titolare(self):
        return self.__titolare

    def set_titolare(self, titolare):
        if isinstance(titolare, str) and titolare.strip():
            self.__titolare = titolare
        if not titolare: print("la stringa non deve essere vuoto")
        
titolare = str(input("inserisci il nome del titolare: "))
banca = ContoBancario(titolare=titolare,saldo = int(input("inserisci il saldo di base: ")))
banca.set_titolare(titolare)
banca.deposita(importo = int(input("inserisci importo: ")))
banca.visualizza_saldo()
banca.preleva(importo= int(input("inserisci importo da prevelare: ")))
banca.visualizza_saldo()