#Crea una lista di 5 colori a tua scelta.

colori = ['blu','arancione','rosso','verde','giallo']
for indice in colori:
    print(indice)

#Aggiungi un nuovo colore alla fine della lista.

colori.append('bianco')
print(f'la lista dei colori con un elemento un piu: {colori}')

#Rimuovi il secondo elemento della lista.

del colori[1]
print(f'la lista dei colori senza un elemento: {colori}')

#Ordina la lista in ordine alfabetico e stampala.

colori.sort()
print(f'la lista dei colori ordinata: {colori}')

#Crea una seconda lista di numeri. Concatena le due liste e stampa il risultato.

numeri = [1,2,3,4,5,6,7,8,9]
lista = colori + numeri
print(f'la lista unita: {lista}')

#Crea un dizionario che rappresenti un libro, con chiavi come "titolo", "autore", "anno" e "genere".

libro = {'titolo':'ciao a tutti', 
         'autore':'pepino',
         'anno':'04/06/2000',
         'genere':'fantasy'
         }

#Aggiungi una nuova coppia chiave-valore "prezzo" al dizionario.

libro['prezzo'] = 15
print(f'il dizionario con una nuova coppia di valori: {libro}')

#Modifica l'anno del libro.

libro['anno'] = '04/10/2010'
print(f'il dizionario con anno modificato: {libro}')

#Stampa tutte le chiavi e poi tutti i valori del dizionario.

for chiave in libro.keys():
    print(f'tutte le chiavi {chiave}')

print()

for valori in libro.values():
    print(f'tutti i valori: {valori}')
    
#Verifica se la chiave "editore" esiste nel dizionario.

if 'editore' in libro:
    print('esiste')
else: 
    print('non esiste')

#Crea una tupla che contenga i nomi dei giorni della settimana.

giorni = ('lunedi','martedi','mercoledi','giovedi','venerdi','sabato','domenica')
print(f'i giorni della settimana: {giorni}')

#Accedi al terzo elemento della tupla.

print(f'il terzo elemento: {giorni[2]}')

#Tenta di modificare un elemento della tupla (vedrai che non è possibile).

#giorni[3] = 'ciao'

#Conta quante volte "Sabato" appare nella tupla.

conta = giorni.count('sabato')
print(f'il numero di sabato presenti: {conta}')

#Crea due set di numeri: set1 e set2.

set1 = {1,2,3,4,4,5,6,5,5,3,4}
set2 = {2,2,2,3,3,4,4,4,5,5,6,7,7,8,9,9,10}
print(f'il primo set: {set1}')
print(f'il secondo set: {set2}')

#Trova l'unione, l'intersezione e la differenza tra i due set. Stampa i risultati.
print(f'unione dei set: {set1.union(set2)}')
print(f'lunione, lintersezione: {set1.intersection(set2)}')
print(f'la differenza tra i due set: {set1.difference(set2)}')

#Aggiungi un elemento a set1.

set1.add(7)
print(f'il set1 con un elemento in piu: {set1}')

#Rimuovi un elemento da set2.

set2.remove(10)
print(f'il set2 con un elemento in meno: {set2}')