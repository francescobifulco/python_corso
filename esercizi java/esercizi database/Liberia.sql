
drop DATABASE if EXISTS Libreria;
CREATE DATABASE Libreria;
use Libreria;

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
    id int PRIMARY key auto_increment not null,
	isbn VARCHAR(40) not null,
	titolo VARCHAR(40) not null,
	autoro VARCHAR(40) not null,
	disponibilita VARCHAR (255) not NULL
);