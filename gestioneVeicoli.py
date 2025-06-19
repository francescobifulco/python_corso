"""Esercizio 1: Gestione di un Veicolo (Classi e Incapsulamento)
Obiettivo: Creare una classe Veicolo che incapsuli le sue proprietà e fornisca metodi per interagire con esse.

Specifiche:

Crea una classe chiamata Veicolo.
Il costruttore (__init__) dovrebbe accettare marca, modello e velocita_attuale. La velocita_attuale dovrebbe essere inizializzata a 0.
Utilizza l'incapsulamento per le proprietà marca, modello e velocita_attuale, rendendole private (usando un singolo underscore come convenzione, es. _marca).
Fornisci metodi "getter" (es. get_marca(), get_modello(), get_velocita_attuale()) per accedere a queste proprietà.
Fornisci un metodo accelera(incremento) che aumenti la velocita_attuale di incremento. Assicurati che la velocità non diventi negativa.
Fornisci un metodo frena(decremento) che diminuisca la velocita_attuale di decremento. Assicurati che la velocità non diventi negativa.
Fornisci un metodo visualizza_info() che stampi tutte le informazioni del veicolo.
Suggerimento: Ricorda che l'incapsulamento in Python è più una convenzione che una vera restrizione. L'uso del singolo underscore _ suggerisce che l'attributo è inteso per uso interno alla classe."""

class Veicolo:
    def __init__(self,marca, modello, velocita_attuale):
        self._marca = marca
        self._modello = modello
        self._velocita_attuale = 0
    
    def get_marca(self):
        return self._marca
    def get_modello(self):
        return self._modello
    def get_velocita_attuale(self):
        return self._velocita_attuale
    
    def frena(self,decremento):
        if self._velocita_attuale > 0:
            self._velocita_attuale - decremento
    