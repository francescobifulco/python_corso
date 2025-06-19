SELECT * FROM universita.studenti;

TRUNCATE TABLE Studenti;

SELECT * FROM universita.studenti;

INSERT INTO Studenti (Matricola, Nome, Cognome, Data_Nascite, Indirizzo_Studi) VALUES
(1, '', 'Rossi', '2000-01-15', 'Informatica'),
(2, 'Anna', 'Bianchi', '2001-03-22', 'Ingegneria'),
(3, 'Luca', 'Verdi', '1999-07-08', 'Economia'),
(4, 'Giulia', 'Neri', '2002-11-30', 'Medicina'),
(5, 'Marco', 'Ferrari', '2000-05-19', 'Giurisprudenza'),
(6, 'Sara', 'Esposito', '1998-12-01', 'Architettura'),
(7, 'Francesco', 'Romano', '2001-09-10', 'Scienze Politiche'),
(8, 'Laura', 'Ricci', '1999-04-14', 'Psicologia'),
(9, 'Davide', 'Moretti', '2000-02-21', 'Matematica'),
(10, 'Martina', 'Lombardi', '2002-08-25', 'Fisica'),
(11, 'Alessandro', 'Gallo', '1998-06-13', 'Filosofia'),
(12, 'Chiara', 'Fontana', '2001-10-29', 'Chimica'),
(13, 'Matteo', 'Colombo', '1999-03-05', 'Biologia'),
(14, 'Elisa', 'Greco', '2000-07-17', 'Storia dell\'Arte'),
(15, 'Federico', 'Conti', '2002-01-26', 'Letteratura'),
(16, 'Alice', 'Rizzo', '1998-11-09', 'Sociologia'),
(17, 'Leonardo', 'Ferraro', '2001-05-03', 'Ingegneria Meccanica'),
(18, 'Valentina', 'Marchetti', '1999-02-18', 'Informatica'),
(19, 'Tommaso', 'Sartori', '2000-10-22', 'Economia'),
(20, 'Francesca', 'Barbieri', '1998-08-07', 'Medicina'),
(21, 'Alessandro', 'Esposito', '1998-05-12', 'Informatica'),
(22,'Francesca', 'Russo', '1999-08-24', 'Biologia'),
(23, 'Giorgio', 'Ferrari', '2000-03-15', 'Ingegneria Informatica');

INSERT INTO Studenti (Matricola, Nome, Cognome, Data_Nascite, Indirizzo_Studi) VALUES
(24, 'Laura', 'Conti', '1997-11-05', 'Teologia'),
(25, 'Paolo', 'Ricci', '2001-12-10', 'Teologia');

SELECT * FROM universita.studenti;