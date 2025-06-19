-- qui di seguito lo script per creare 
-- un DB che rappreseenta una biblioteca

drop DATABASE if EXISTS biblioteca;
CREATE DATABASE biblioteca;
use biblioteca;

-- costruisco lo schema della tabella autore 
CREATE table autore (
	id int PRIMARY KEY auto_increment not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null
);

-- costruisco lo schema della tabella casa_editrice
CREATE table casa_editrice (
	id int PRIMARY key auto_increment not null,
	nome VARCHAR(40) not null
);

-- costruisco lo schema della tabella libro 
CREATE table libro (
	id int PRIMARY key auto_increment not null,
	titolo VARCHAR(40) not null,
	id_auto int not null,
	id_casa_editrice int not null,
	FOREIGN key(id_auto) REFERENCES autore(id),
	FOREIGN key(id_casa_editrice) REFERENCES casa_editrice(id)
);

-- inizio del blocco di definizione di proecedure e funzioni
delimiter $$

create procedure tutti_i_libri()
begin
	select * from libro;
end $$

create procedure quanti_libri_per_autore(in param_autore int, out conteggio int)
begin
	select count(*) into conteggio from libro where id_auto = param_autore;
end $$

delimiter ;
-- -------------------------------------------------------

-- inserimento dei dati nella tabella degli autori
INSERT into autore values 
	(1, 'alessandro','manzoni'),
	(2,'dino','buzzati');

-- inserimento dei dati nella tabella della case editrici 
INSERT into casa_editrice VALUES
	(1, 'casa paperino'),
	(2, 'casa pluto');

-- inserimento dei dati nella tabella dei libri
INSERT into libro values 
	(1,'i promessi sposi', 1, 1),
	(2, 'il conte di carmagnola', 1, 1),
	(3, 'deserto dei tartari', 2, 2);
