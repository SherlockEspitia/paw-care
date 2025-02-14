CREATE DATABASE IF NOT EXISTS appet;

USE appet;

-- 
-- Tabla propietario
-- 
CREATE TABLE IF NOT EXISTS `appet`.`propietario` (
    `IDpropietario` BIGINT(12) NOT NULL AUTO_INCREMENT,
    `nombres` VARCHAR(45) NOT NULL,
    `apellidos` VARCHAR(45) NOT NULL,
    `correo_electronico_propietario` VARCHAR(75) NOT NULL,
    `telefono_propietario` VARCHAR(45) NOT NULL,
    `direccion_propietario` VARCHAR(45) NOT NULL,
    `ciudad_propietario` VARCHAR(45) NOT NULL,
    PRIMARY KEY (`IDpropietario`),
    UNIQUE INDEX `idpropietario_UNIQUE` (`IDpropietario` ASC) VISIBLE,
    UNIQUE INDEX `telefono_propietario_UNIQUE` (`telefono_propietario` ASC) VISIBLE
) ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `appet`.`mascota`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appet`.`mascota` (
  `IDmascota` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `nombre_mascota` VARCHAR(45) NOT NULL,
  `especie` VARCHAR(45) NOT NULL,
  `raza` VARCHAR(45) NULL,
  `fecha_nacimiento_mascota` VARCHAR(45) NULL,
  `IDpropietario` BIGINT(12) NOT NULL,
  PRIMARY KEY (`IDmascota`, `IDpropietario`),
  INDEX `fk_mascota_propietario_idx` (`IDpropietario` ASC) VISIBLE,
  CONSTRAINT `fk_mascota_propietario`
    FOREIGN KEY (`IDpropietario`)
    REFERENCES `appet`.`propietario` (`IDpropietario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `appet`.`servicio`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appet`.`servicio` (
  `IDservicio` BIGINT(12) NOT NULL,
  `IDcuidador` BIGINT(12) NOT NULL,
  `descripcion_servicio` TEXT(250) NULL,
  `precio` DECIMAL NULL,
  `IDmascota` BIGINT(12) NOT NULL,
  `IDpropietario` BIGINT(12) NOT NULL,
  `tipo_servicio` VARCHAR(45) NULL,
  PRIMARY KEY (`IDservicio`, `IDcuidador`, `IDmascota`, `IDpropietario`),
  INDEX `fk_servicio_mascota1_idx` (`IDmascota` ASC, `IDpropietario` ASC) VISIBLE,
  INDEX `fk_servicio_cuidador1_idx` (`IDcuidador` ASC) VISIBLE,
  CONSTRAINT `fk_servicio_mascota1`
    FOREIGN KEY (`IDmascota` , `IDpropietario`)
    REFERENCES `appet`.`mascota` (`IDmascota` , `IDpropietario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_servicio_cuidador1`
    FOREIGN KEY (`IDcuidador`)
    REFERENCES `appet`.`cuidador` (`IDcuidador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `appet`.`Agenda`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appet`.`Agenda` (
  `IDagenda` INT NOT NULL,
  `fecha` DATE NULL,
  `hora_inicio` TIME NULL,
  `hora_fin` TIME NULL,
  `IDservicio` BIGINT(12) NOT NULL,
  `IDmascota` BIGINT(12) NOT NULL,
  `IDpropietario` BIGINT(12) NOT NULL,
  PRIMARY KEY (`IDagenda`, `IDservicio`, `IDmascota`, `IDpropietario`),
  INDEX `fk_Agenda_servicio1_idx` (`IDservicio` ASC, `IDmascota` ASC, `IDpropietario` ASC) VISIBLE,
  CONSTRAINT `fk_Agenda_servicio1`
    FOREIGN KEY (`IDservicio` , `IDmascota` , `IDpropietario`)
    REFERENCES `appet`.`servicio` (`IDservicio` , `IDmascota` , `IDpropietario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `appet`.`cuidador`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `appet`.`cuidador` (
  `IDcuidador` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `nombre_cuidador` VARCHAR(45) NOT NULL,
  `correo_electronico_cuidador` VARCHAR(45) NOT NULL,
  `telefono_cuidador` VARCHAR(45) NOT NULL,
  `tipo_cuidador` ENUM('paseador', 'entrenador', 'guarderia') NOT NULL, -- Tipo de cuidador
  `experiencia` INT NULL, -- Solo para paseadores y entrenadores
  `tarifas` DECIMAL(10, 2) NULL, -- Solo para paseadores
  `especialidad` VARCHAR(45) NULL, -- Solo para entrenadores
  `certificaciones` TEXT NULL, -- Solo para entrenadores
  `direccion` VARCHAR(125) NULL, -- Solo para guarderías
  `capacidad` INT NULL, -- Solo para guarderías
  PRIMARY KEY (`IDcuidador`)
) ENGINE = InnoDB;
