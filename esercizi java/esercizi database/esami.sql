SELECT * FROM universita.esami;

INSERT INTO Esami (Id_Esame, FK_Id_Docente, FK_Matricola, FK_Id_Corso, Data_Esame, Voto) VALUES
(1, 1, 1, 1, '2024-06-15', 28),
(2, 2, 2, 2, '2024-06-18', 30),
(3, 3, 3, 3, '2024-06-20', 27);

SELECT * FROM universita.esami;

INSERT INTO Esami (Id_Esame, FK_Id_Docente, FK_Matricola, FK_Id_Corso, Data_Esame, Voto) VALUES
(4, 4, 4, 4, '2024-06-22', 29),
(5, 5, 5, 5, '2024-06-25', 30);

INSERT INTO Esami (Id_Esame, FK_Id_Docente, FK_Matricola, FK_Id_Corso, Data_Esame, Voto) VALUES
(6, 6, 6, 6, '2024-06-30', 26);

SELECT * FROM universita.esami;