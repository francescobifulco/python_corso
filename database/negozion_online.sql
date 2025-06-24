#create database negozio_online;

-- Creazione della tabella Clienti
CREATE TABLE Clienti (
    IDCliente INT PRIMARY KEY,
    Nome VARCHAR(50),
    Cognome VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Citta VARCHAR(50),
    DataRegistrazione DATE
);

-- Inserimento dati di esempio nella tabella Clienti
INSERT INTO Clienti (IDCliente, Nome, Cognome, Email, Citta, DataRegistrazione) VALUES
(1, 'Mario', 'Rossi', 'mario.rossi@email.com', 'Roma', '2023-01-15'),
(2, 'Laura', 'Bianchi', 'laura.bianchi@email.com', 'Milano', '2023-02-20'),
(3, 'Giulia', 'Verdi', 'giulia.verdi@email.com', 'Napoli', '2023-03-10'),
(4, 'Luca', 'Gialli', 'luca.gialli@email.com', 'Roma', '2023-04-05'),
(5, 'Anna', 'Neri', 'anna.neri@email.com', 'Firenze', '2023-05-01'),
(6, 'Paolo', 'Blu', 'paolo.blu@email.com', 'Milano', '2024-01-22'),
(7, 'Elena', 'Marrone', 'elena.marrone@email.com', 'Roma', '2024-02-14'),
(8, 'Marco', 'Arancio', 'marco.arancio@email.com', 'Torino', '2023-11-30');

-- Creazione della tabella Prodotti
CREATE TABLE Prodotti (
    IDProdotto INT PRIMARY KEY,
    NomeProdotto VARCHAR(100),
    Categoria VARCHAR(50),
    Prezzo DECIMAL(10, 2),
    QuantitaInMagazzino INT
);

-- Inserimento dati di esempio nella tabella Prodotti
INSERT INTO Prodotti (IDProdotto, NomeProdotto, Categoria, Prezzo, QuantitaInMagazzino) VALUES
(101, 'Laptop X1', 'Elettronica', 1200.00, 15),
(102, 'Mouse Wireless', 'Elettronica', 25.50, 50),
(103, 'Penna a sfera', 'Cancelleria', 1.20, 200),
(104, 'Quaderno A4', 'Cancelleria', 3.50, 150),
(105, 'Smartphone Z', 'Elettronica', 800.00, 25),
(106, 'Cuffie Bluetooth', 'Elettronica', 75.00, 30),
(107, 'Tastiera Meccanica', 'Elettronica', 99.99, 10),
(108, 'Risma Carta A4', 'Cancelleria', 8.99, 80);


-- Creazione della tabella Ordini
CREATE TABLE Ordini (
    IDOrdine INT PRIMARY KEY,
    IDCliente INT,
    IDProdotto INT,
    Quantita INT,
    DataOrdine DATE,
    FOREIGN KEY (IDCliente) REFERENCES Clienti(IDCliente),
    FOREIGN KEY (IDProdotto) REFERENCES Prodotti(IDProdotto)
);

-- Inserimento dati di esempio nella tabella Ordini
INSERT INTO Ordini (IDOrdine, IDCliente, IDProdotto, Quantita, DataOrdine) VALUES
(1001, 1, 101, 1, '2023-01-16'),
(1002, 2, 103, 5, '2023-02-21'),
(1003, 1, 102, 2, '2023-03-01'),
(1004, 3, 104, 3, '2023-03-11'),
(1005, 4, 105, 1, '2023-04-06'),
(1006, 5, 103, 10, '2023-05-02'),
(1007, 1, 107, 1, '2024-01-20'),
(1008, 6, 106, 1, '2024-02-01'),
(1009, 7, 102, 1, '2024-02-15'),
(1010, 8, 108, 2, '2023-12-01'),
(1011, 2, 101, 1, '2024-03-01'),
(1012, 3, 103, 2, '2024-03-05');