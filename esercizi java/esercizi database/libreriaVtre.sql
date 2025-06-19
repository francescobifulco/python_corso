drop DATABASE if EXISTS libreriaVtre;
CREATE DATABASE libreriaVtre;
use libreriaVtre;

-- costruisco lo schema della tabella Utenti 
create table Libro(
autore varchar(50) not null,
isbn varchar(50) primary key, 
titolo varchar(100) not null,
prezzo int not null
);

CREATE TABLE IF BluRay (
  codice CHAR(20) NOT NULL,
  titolo VARCHAR(255) NULL DEFAULT NULL,
  prezzo DOUBLE NOT NULL,
 );

INSERT into Libro Values ('Leopardi','123','I promessi sposi',12);
INSERT into Libro Values ('Dante Alighieri','456','La divina Commedia',12);
INSERT into Libro Values ('Pio piscitelli','678','Pensavo fosse amore,invece era Higuain',12);
INSERT into Libro Values ('Raphael Leao','238','Stasera non Passo',12);
