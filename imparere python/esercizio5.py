"""Esercizio 5: Funzioni
Obiettivo: Definire e chiamare funzioni per organizzare il codice.

Definisci una funzione chiamata calcola_area che accetta due argomenti: lunghezza e larghezza. Dovrebbe restituire l'area di un rettangolo.
Definisci una funzione chiamata saluta che accetta un argomento: nome. Dovrebbe stampare "Ciao, [Nome]!".
Chiama entrambe le funzioni con argomenti appropriati."""

def calcola_area(lunghezza, larghezza):
    area = lunghezza * larghezza
    print(f"area del rerrangolo e: {area}")
    
calcola_area(34,32)

def saluta(nome):
    print(f"Ciao, {nome}!")

nome = input("il tuo nome: ")
saluta(nome)