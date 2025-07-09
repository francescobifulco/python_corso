#Chiedi all'utente una frase. Stampa la frase in maiuscolo e in minuscolo.

frase = str(input("inseriscicuna frase: "))
print(f"maiuscolo: {frase.upper()}")
print(f"minuscolo: {frase.lower()}")

#Conta quante volte la lettera 'a' (maiuscola o minuscola) appare nella frase.

conta = frase.lower().count('a')
print(f"la lettera 'a' compare: {conta}")

#Sostituisci tutte le occorrenze della parola "Python" con "Java" (se presente) nella frase. Stampa la frase modificata.
if "Python" in frase:
    nuova_frase = frase.replace('Python','Java')
    print(nuova_frase)
else: print("la parola 'Python' non presente")

#Verifica se la frase inserita dall'utente inizia con "Ciao" e finisce con un punto esclamativo "!".

print(frase.startswith("ciao")) 
print(frase.endswith("!"))