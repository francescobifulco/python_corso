-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Universita
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Universita
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Universita` DEFAULT CHARACTER SET utf8 ;
USE `Universita` ;

-- -----------------------------------------------------
-- Table `Universita`.`Studenti`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Universita`.`Studenti` (
  `Matricola` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Cognome` VARCHAR(45) NOT NULL,
  `Data_Nascite` DATE NOT NULL,
  `Indirizzo_Studi` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Matricola`),
  UNIQUE INDEX `Matricola_UNIQUE` (`Matricola` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Universita`.`Corsi`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Universita`.`Corsi` (
  `Id_Corso` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `CFU` INT NOT NULL,
  PRIMARY KEY (`Id_Corso`),
  UNIQUE INDEX `Id_Corso_UNIQUE` (`Id_Corso` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Universita`.`Docenti`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Universita`.`Docenti` (
  `Id_Docente` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Cognome` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Id_Docente`),
  UNIQUE INDEX `Id_Docente_UNIQUE` (`Id_Docente` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Universita`.`Esami`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Universita`.`Esami` (
  `Id_Esame` INT NOT NULL AUTO_INCREMENT,
  `FK_Id_Docente` INT NOT NULL,
  `FK_Matricola` INT NOT NULL,
  `FK_Id_Corso` INT NOT NULL,
  `Data_Esame` DATE NOT NULL,
  `Voto` INT NOT NULL,
  `Corsi_Id_Corso` INT NOT NULL,
  `Studenti_Matricola` INT NOT NULL,
  `Docenti_Id_Docente` INT NOT NULL,
  PRIMARY KEY (`Id_Esame`, `Corsi_Id_Corso`, `Studenti_Matricola`, `Docenti_Id_Docente`),
  UNIQUE INDEX `Id_Esame_UNIQUE` (`Id_Esame` ASC) VISIBLE,
  INDEX `fk_Esami_Corsi1_idx` (`Corsi_Id_Corso` ASC) VISIBLE,
  INDEX `fk_Esami_Studenti1_idx` (`Studenti_Matricola` ASC) VISIBLE,
  INDEX `fk_Esami_Docenti1_idx` (`Docenti_Id_Docente` ASC) VISIBLE,
  CONSTRAINT `fk_Esami_Corsi1`
    FOREIGN KEY (`Corsi_Id_Corso`)
    REFERENCES `Universita`.`Corsi` (`Id_Corso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Esami_Studenti1`
    FOREIGN KEY (`Studenti_Matricola`)
    REFERENCES `Universita`.`Studenti` (`Matricola`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Esami_Docenti1`
    FOREIGN KEY (`Docenti_Id_Docente`)
    REFERENCES `Universita`.`Docenti` (`Id_Docente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Universita`.`Corsi_has_Docenti`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Universita`.`Corsi_has_Docenti` (
  `Corsi_Id_Corso` INT NOT NULL,
  `Docenti_Id_Docente` INT NOT NULL,
  PRIMARY KEY (`Corsi_Id_Corso`, `Docenti_Id_Docente`),
  INDEX `fk_Corsi_has_Docenti_Docenti1_idx` (`Docenti_Id_Docente` ASC) VISIBLE,
  INDEX `fk_Corsi_has_Docenti_Corsi_idx` (`Corsi_Id_Corso` ASC) VISIBLE,
  CONSTRAINT `fk_Corsi_has_Docenti_Corsi`
    FOREIGN KEY (`Corsi_Id_Corso`)
    REFERENCES `Universita`.`Corsi` (`Id_Corso`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Corsi_has_Docenti_Docenti1`
    FOREIGN KEY (`Docenti_Id_Docente`)
    REFERENCES `Universita`.`Docenti` (`Id_Docente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
