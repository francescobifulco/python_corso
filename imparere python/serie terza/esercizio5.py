#Crea una lista di 5 colori a tua scelta.

colori = ['blu','arangione','rosso','verde','giallo']
for indice in len(colori):
    print(indice)

#Aggiungi un nuovo colore alla fine della lista.

colori.append('bianco')
print(f'la lista dei colori con un elemento un piu: {colori}')

#Rimuovi il secondo elemento della lista.

colori.remove('rosso')
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

#Modifica l'anno del libro.

#Stampa tutte le chiavi e poi tutti i valori del dizionario.

#Verifica se la chiave "editore" esiste nel dizionario.



#Crea una tupla che contenga i nomi dei giorni della settimana.

#Accedi al terzo elemento della tupla.

#Tenta di modificare un elemento della tupla (vedrai che non è possibile).

#Conta quante volte "Sabato" appare nella tupla.



#Crea due set di numeri: set1 e set2.

#Trova l'unione, l'intersezione e la differenza tra i due set. Stampa i risultati.

#Aggiungi un elemento a set1.

#Rimuovi un elemento da set2.

