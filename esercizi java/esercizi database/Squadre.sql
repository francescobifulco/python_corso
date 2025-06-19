-- Impossibile creare la tabella `squadre`.`squadre` (errno: 150 "Foreign key constraint is incorrectly formed")

drop DATABASE if EXISTS Squadre;
CREATE DATABASE Squadre;
use Squadre;

CREATE table Squadre (
	nome_sqa VARCHAR(40) PRIMARY KEY not null,
	anno_fon DATE not NULL,
	citt VARCHAR(40) not null,
	serie VARCHAR(40) not null,
	FOREIGN key(citt) REFERENCES Citta(cittta),
	FOREIGN key(serie) REFERENCES Serie(categorie)
);

CREATE table Citta (
	cittta VARCHAR(40) PRIMARY KEY not null
);

CREATE table Giocatore (
	num_tess int(40) PRIMARY KEY not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null,
	anno_nas DATE not NULL,
	squadr VARCHAR(40) not NULl,
	FOREIGN key(squadr) REFERENCES Squadre(nome_sqa)
);

CREATE table Serie (
	categorie VARCHAR(40) PRIMARY KEY not null,
);