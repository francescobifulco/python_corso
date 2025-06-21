"""Generatore di Password Sicure
Un programma che crea password casuali basate sulle 
preferenze dell'utente (lunghezza, inclusione di maiuscole, 
minuscole, numeri, simboli).
Concetti Utilizzati:
Stringhe: Utilizzare diverse stringhe predefinite per 
caratteri minuscoli, maiuscoli, numeri e simboli. 
Concatenazione di stringhe per il pool di caratteri.
Collezioni: Liste o tuple per definire i set di caratteri da 
cui scegliere.
Funzioni: Per generare la password, per validare la 
lunghezza, e per gestire le opzioni dell'utente.
Moduli: random per scegliere caratteri casuali e string per 
accedere facilmente a set di caratteri predefiniti 
(es. string.ascii_letters, string.digits, 
string.punctuation).
Cicli for: Per costruire la password carattere per 
carattere.
Input Utente: Richiedere all'utente le preferenze per la 
password.
Funzionalità:
Chiedi Preferenze: Domanda all'utente la lunghezza 
desiderata della password e se includere lettere maiuscole, 
minuscole, numeri e simboli.
Genera Password: Basandosi sulle preferenze, costruisci un 
"pool" di caratteri possibili e seleziona casualmente i 
caratteri per creare la password.
Mostra Password: Visualizza la password generata.
Genera Multiple Password: Opzione per generare più password 
in una volta.
Requisiti Minimi: Assicurati che la password generata 
contenga almeno un carattere di ogni tipo richiesto, 
se applicabile (ad esempio, se l'utente vuole numeri, 
assicurati che almeno un numero sia presente)."""

import random
import string

class Password:
    def chiedi(self):
        lunghezza = int(input("Inserisci la lunghezza della stringa: "))
        maiuscole = input("Vuoi includere anche le maiuscole? (s/n): ").lower() == "s"
        minuscole = input("Vuoi includere anche le minuscole? (s/n): ").lower() == "s"
        numeri = input("Vuoi includere anche i numeri? (s/n): ").lower() == "s"
        simboli = input("Vuoi includere anche i simboli? (s/n): ").lower() == "s"
        return lunghezza, maiuscole, minuscole, numeri, simboli

    def pool(self, maiuscole, minuscole, numeri, simboli):
        caratteri = ""
        if maiuscole:
            caratteri += string.ascii_uppercase
        if minuscole:
            caratteri += string.ascii_lowercase
        if numeri:
            caratteri += string.digits
        if simboli:
            caratteri += string.punctuation
        return caratteri

    def genera_password(self, lunghezza, caratteri):
        if not caratteri:
            print("Devi selezionare almeno un tipo di carattere!")
            return ""
        return ''.join(random.choice(caratteri) for _ in range(lunghezza))

    def mostra(self, pwd):
        print(f"La password generata è: {pwd}")

genera = Password()
lunghezza, maiuscole, minuscole, numeri, simboli = genera.chiedi()
caratteri = genera.pool(maiuscole, minuscole, numeri, simboli)
pwd = genera.genera_password(lunghezza, caratteri)
genera.mostra(pwd)
        