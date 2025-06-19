-- Impossibile creare la tabella `ballo`.`corso` (errno: 150 "Foreign key constraint is incorrectly formed")

drop DATABASE if EXISTS Ballo;
CREATE DATABASE Ballo;
use Ballo;

CREATE table Corso (
	nome_cor VARCHAR(40) PRIMARY KEY not null,
	orario DATE not NULL,
	data_avv date not null,
	istruttore VARCHAR(20) not null,
	FOREIGN key(istruttore) REFERENCES Istruttore(matricola)
);

CREATE table Istruttore (
	matricola VARCHAR() PRIMARY KEY not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null,
	tell int(40) not null,
	data_assunzione date not null
);

CREATE table Iscritto (
	num_tessera int(40) PRIMARY KEY not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null,
	tell int(40) not null
);

CREATE table Iscrizioni (
	num_tesse int(40) not null,
	nome_cors VARCHAR(40),
	data_Iscrizione DATE not null,
	FOREIGN key(nome_cors) REFERENCES Corso(nome_cor),
	FOREIGN key(num_tesse) REFERENCES Iscritto(num_tessera)
);