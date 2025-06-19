
drop DATABASE if EXISTS libreria;
CREATE DATABASE libreria;
use libreria;

-- costruisco lo schema della tabella Utenti 
CREATE table utenti (
	id int PRIMARY key auto_increment not null,
	nome VARCHAR(40) not null,
	cognome VARCHAR(40) not null,
	email VARCHAR(40) not null,
	Password VARCHAR (255) not NULL
);

-- costruisco lo schema della tabella Utenti 
CREATE table libri (
    isbn VARCHAR(40) PRIMARY key not null,
	titolo VARCHAR(40) not null,
	autore VARCHAR(40) not null,
	genere VARCHAR (40) not null,
	disponibilita VARCHAR (255) not NULL
);

INSERT into libri Values ('123','I promessi sposi','Leopardi',12,'si');
INSERT into libri Values ('124','La divina Commedia','Dante Alighieri',12,'no');
INSERT into libri Values ('125','Pensavo fosse amore,invece era Higuain','Pio piscitelli',12,'no');
INSERT into libri Values ('126','Stasera non Passo','Raphael Leao',12,'si');
