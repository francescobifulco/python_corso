-- qui di seguito lo script per creare 
-- un DB che rappreseenta una Memorizzare informazione dei dipendenti


use Dipendenti;

CREATE table dipendenti (
	idDipendente int PRIMARY KEY auto_increment not null,
	nome VARCHAR(40) not null,
	cognome VARCHAR(40) not null,
	anni_servizio int (30) not null,
	Stipendio int (10) not null
);

INSERT into dipendenti values 
	(1, 'alessandro','manzoni','30','1500'),
	(2,'dino','buzzati','40','1800');
	
	delimiter $$

create procedure ordina_cognome()
begin
	select cognome from dipendenti ORDER BY cognome ASC ;
end $$

delimiter ;