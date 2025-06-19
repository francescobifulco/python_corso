-- creazione della tabella cliente
create table clienti (
Id_Cliente int PRIMARY KEY,
Nome VARCHAR(100),
Cognome VARCHAR(100),
Data_Nascita datetime,
Codice_Fiscale VARCHAR(16)
);