-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema cinema_database_new
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cinema_database_new
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cinema_database_new` DEFAULT CHARACTER SET utf8mb3 ;
USE `cinema_database_new` ;

-- -----------------------------------------------------
-- Table `cinema_database_new`.`Attori`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cinema_database_new`.`Attori` ;

CREATE TABLE IF NOT EXISTS `cinema_database_new`.`Attori` (
  `Cod_Attore` INT NOT NULL AUTO_INCREMENT,
  `Nome` VARCHAR(45) NOT NULL,
  `Anno_Nascita` INT NOT NULL,
  `Nazionalità` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Attore`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cinema_database_new`.`Film`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cinema_database_new`.`Film` ;

CREATE TABLE IF NOT EXISTS `cinema_database_new`.`Film` (
  `Cod_Film` INT NOT NULL AUTO_INCREMENT,
  `Titolo` VARCHAR(45) NOT NULL,
  `Anno_Produzione` INT NOT NULL,
  `Nazionalità` VARCHAR(45) NOT NULL,
  `Regista` VARCHAR(45) NOT NULL,
  `Genere` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Film`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cinema_database_new`.`Recita`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cinema_database_new`.`Recita` ;

CREATE TABLE IF NOT EXISTS `cinema_database_new`.`Recita` (
  `Attori_Cod_Attore` INT NOT NULL,
  `Film_Cod_Film` INT NOT NULL,
  PRIMARY KEY (`Attori_Cod_Attore`, `Film_Cod_Film`),
  INDEX `fk_Recita_Film1_idx` (`Film_Cod_Film` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cinema_database_new`.`Sale`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cinema_database_new`.`Sale` ;

CREATE TABLE IF NOT EXISTS `cinema_database_new`.`Sale` (
  `Cod_Sala` INT NOT NULL AUTO_INCREMENT,
  `Posti` INT NOT NULL,
  `Nome` VARCHAR(45) NOT NULL,
  `Città` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`Cod_Sala`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cinema_database_new`.`Proiezioni`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `cinema_database_new`.`Proiezioni` ;

CREATE TABLE IF NOT EXISTS `cinema_database_new`.`Proiezioni` (
  `Cod_Proiezione` INT NOT NULL AUTO_INCREMENT,
  `Incasso` INT NOT NULL,
  `Data_Proiezione` DATETIME NOT NULL,
  `Film_Cod_Film` INT NOT NULL,
  `Sale_Cod_Sala` INT NOT NULL,
  PRIMARY KEY (`Cod_Proiezione`, `Film_Cod_Film`, `Sale_Cod_Sala`),
  INDEX `fk_Proiezioni_Film1_idx` (`Film_Cod_Film` ASC) VISIBLE,
  INDEX `fk_Proiezioni_Sale1_idx` (`Sale_Cod_Sala` ASC) VISIBLE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
