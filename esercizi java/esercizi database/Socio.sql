-- mettere in storico

drop DATABASE if EXISTS Socio;
CREATE DATABASE Socio;
use Socio;

CREATE table socio (
	n_tessera int PRIMARY KEY auto_increment not null,
	nome VARCHAR(40),
	cognome VARCHAR(40) not null,
	luog_nas VARCHAR(40) not null,
	data_nasci date not null, 
	indirizzo_resid VARCHAR(50) not null,
	comune VARCHAR(50) not null,
	data_prima_iscri date not null,
	data_ult_versamento date not null,
	quota_versata int(50) not null
);


create procedure vencoli()
begin
	select * from socio WHEN data_ult_versamento>= data_prima_iscri AND Data_nas > #01/01/1900# 
end $$


delimiter ;