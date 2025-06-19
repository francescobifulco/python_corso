-- qui di seguito lo script per creare 
-- un DB che rappreseenta una Memorizzare informazione degli utenti

drop DATABASE if EXISTS Memorizzare;
CREATE DATABASE Memorizzare;
use Memorizzare;

-- costruisco lo schema della tabella Utenti 
CREATE table utenti (
	id int PRIMARY key auto_increment not null,
	nome VARCHAR(40) not null,
	cognome VARCHAR(40) not null,
	email VARCHAR(40) not null,
	Password VARCHAR (255) not NULL
);

