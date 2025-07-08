#Mostra tutte le colonne di tutti i clienti.
select * from clienti;

#Mostra solo il NomeProdotto e il Prezzo di tutti i prodotti.
select NomeProdotto,Prezzo from prodotti;

#Trova tutti i clienti che risiedono a 'Roma'.
select * from clienti where Citta = 'Roma';

#Elenca tutti i prodotti la cui QuantitaInMagazzino è inferiore a 20.
select * from prodotti where QuantitaInMagazzino < 20;

#Visualizza tutti gli ordini, ordinati dal più recente al meno recente.
select * from ordini order by DataOrdine desc;

#Trova il NomeProdotto e il Prezzo dei 3 prodotti più costosi.
select NomeProdotto,prezzo from prodotti order by Prezzo limit 3;

#Trova tutti i clienti che vivono a Roma o Milano.
select * from clienti where citta = 'roma' or citta = 'milano';

#Elenca tutti i prodotti della categoria Elettronica che hanno un prezzo superiore a 100 euro.
select * from prodotti where Categoria = 'elettronica' and Prezzo > 100