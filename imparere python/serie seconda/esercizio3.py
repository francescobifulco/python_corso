"""Esercizio 3: Stringhe e Metodi delle Stringhe
Obiettivo: Lavorare con le stringhe ed esplorare alcuni dei loro metodi più comuni.

Crea una variabile frase con il valore: "Python è un linguaggio di programmazione potente e versatile."
Stampa la lunghezza della frase.
Stampa la frase in maiuscolo e in minuscolo.
Conta quante volte la lettera 'o' (sia maiuscola che minuscola) appare nella frase.
Sostituisci la parola "potente" con "straordinario" nella frase e stampa la nuova frase.
Verifica se la frase inizia con "Python" e se finisce con "versatile." (Stampa True o False per entrambi).
Dividi la frase in una lista di parole e stampa la lista."""

frase = "Python è un linguaggio di programmazione potente e versatile."

print(f"la frase e: {frase}")
print(f"la lunghezza della frase e: {len(frase)}")
print(f" la frase in miniscolo: {frase.lower()}")
print(f"la fare in maiuscola: {frase.upper()}")

nuova_frase = frase.replace("potente", "straordinario")
print(f"la nuova frase: {nuova_frase}")

parola = nuova_frase.startswith("Python")
print(f"la frase inizia con 'Python'?: {parola}")

parola1 = nuova_frase.endswith("versatile")
print(f"la frase finisci con 'versatile'?: {parola1}")

lista_frase = nuova_frase.split()
print(lista_frase)