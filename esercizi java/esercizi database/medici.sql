-- codice, cognome, nome,
-- data e luogo di nascita; di ogni paziente devono essere registrati codice fiscale, cognome,
-- nome, data e luogo di nascita, indirizzo. 

drop DATABASE if EXISTS Medici;
CREATE DATABASE Medici;
use Medici;

CREATE table medici (
	codice int PRIMARY KEY auto_increment not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null,
	luog_nas VARCHAR(40) not null,
	data_nasci date not null
);

CREATE table paziente (
	cod_fisc int PRIMARY KEY auto_increment not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null,
	luog_nas VARCHAR(40) not null,
	data_nasci date not null, 
	comune VARCHAR(50) not null,
	indirizzo_resid VARCHAR(50) not null,
	cod_med int not null,
	FOREIGN key(cod_med) REFERENCES medici(codice)
);