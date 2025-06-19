-- qui di seguito lo script per creare 
-- un DB che rappreseenta una biblioteca

drop DATABASE if EXISTS Memorizzare;
CREATE DATABASE Memorizzare;
use Memorizzare;

-- costruisco lo schema della tabella Utenti 
CREATE table utente (
	id int PRIMARY key auto_increment not null,
	nome VARCHAR(40) not null,
	cognome VARCHAR(40) not null,
	email VARCHAR(40) not null,
	Password VARCHAR(255) not NULL
);