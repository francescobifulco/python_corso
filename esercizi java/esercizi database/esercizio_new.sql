-- Il nome di tutte le sale di Pisa 
 select Città 
 from sale 
 where Città='Pisa';
 
 -- Il titolo dei film di F. Fellini prodotti dopo il 1960. 
 select titolo,Anno_Produzione,regista 
 from film 
 where Regista= 'F. Fellini' 
 AND  Anno_Produzione > 1960;
 
-- Il titolo e la durata dei film di fantascienza giapponesi o francesi prodotti dopo il 1990
SELECT f.titolo, p.Data_Proiezione
FROM film f
JOIN proiezioni p 
ON f.Cod_Film = p.Film_Cod_Film
WHERE f.genere = 'fantascienza'
  AND (f.nazionalità = 'Giapponessi' OR f.nazionalità = 'Francese')
  AND f.anno_produzione > 1990;
  
-- Il titolo dei film di fantascienza giapponesi prodotti dopo il 1990 oppure francesi 
SELECT titolo
FROM film 
WHERE genere = 'fantascienza' 
  AND (nazionalità = 'Giapponessi' OR nazionalità = 'Francese')
  AND anno_produzione > 1990;
  
-- I titolo dei film dello stesso regista di “Casablanca”
select titolo, regista 
from film 
where regista = 'Michael Curtiz';

-- Il titolo ed il genere dei film proiettati il giorno di Natale 2004 
select f.titolo, f.genere, p.data_proiezione
from film f
join proiezioni p
ON f.Cod_Film = p.Film_Cod_Film
where p.Data_Proiezione = '2004-12-25';

-- Il titolo ed il genere dei film proiettati a Napoli il giorno di Natale 2004
select f.titolo, f.genere, p.data_proiezione, s.Città, s.Nome
from film f
join proiezioni p
ON f.Cod_Film = p.Film_Cod_Film
join sale s
ON p.Sale_Cod_Sala = s.Cod_Sala
where p.Data_Proiezione = '2004-12-25'
AND s.Città = 'Napoli';

-- I nomi delle sale di Napoli in cui il giorno di Natale 2004 è stato proiettato un film con R.Williams
SELECT s.nome, s.Città
FROM sale s
JOIN proiezioni p ON s.Cod_Sala = p.Sale_Cod_Sala
JOIN film f ON f.Cod_Film = p.Sale_Cod_Sala
JOIN recita r ON f.Cod_Film = r.Film_Cod_Film
JOIN attori a ON a.Cod_Attore = r.Attori_Cod_Attore
WHERE p.Data_Proiezione = '2004-12-25'
  AND a.Nome = 'robin williams'
  AND s.Città = 'Napoli';


