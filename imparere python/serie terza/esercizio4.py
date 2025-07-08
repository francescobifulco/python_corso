#Chiedi all'utente una frase. Stampa la frase in maiuscolo e in minuscolo.

frase = str(input("inseriscicuna frase: "))
print(f"maiuscolo: {frase.upper()}")
print(f"minuscolo: {frase.lower()}")

#Conta quante volte la lettera 'a' (maiuscola o minuscola) appare nella frase.

conta = frase.count('a')
print(f"la lettera 'a' compare: {conta}")

#Sostituisci tutte le occorrenze della parola "Python" con "Java" (se presente) nella frase. Stampa la frase modificata.

#Verifica se la frase inserita dall'utente inizia con "Ciao" e finisce con un punto esclamativo "!".