-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS appet;
USE appet;

-- 1. Tabla propietario
CREATE TABLE IF NOT EXISTS `appet`.`propietario` (
  `IDpropietario` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `nombres` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `correo_electronico_propietario` VARCHAR(75) NOT NULL,
  `telefono_propietario` VARCHAR(45) NOT NULL,
  `direccion_propietario` VARCHAR(45) NOT NULL,
  `ciudad_propietario` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`IDpropietario`),
  UNIQUE INDEX `telefono_propietario_UNIQUE` (`telefono_propietario`)
) ENGINE = InnoDB;

-- 2. Tabla mascota (clave primaria simple)
CREATE TABLE IF NOT EXISTS `appet`.`mascota` (
  `IDmascota` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `nombre_mascota` VARCHAR(45) NOT NULL,
  `especie` VARCHAR(45) NOT NULL,
  `raza` VARCHAR(45) NULL,
  `fecha_nacimiento_mascota` DATE NULL,
  `IDpropietario` BIGINT(12) NOT NULL,
  PRIMARY KEY (`IDmascota`), -- Clave primaria simple
  INDEX `fk_mascota_propietario_idx` (`IDpropietario`),
  CONSTRAINT `fk_mascota_propietario` 
    FOREIGN KEY (`IDpropietario`) 
    REFERENCES `appet`.`propietario` (`IDpropietario`)
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- 3. Tabla cuidador
CREATE TABLE IF NOT EXISTS `appet`.`cuidador` (
  `IDcuidador` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `nombre_cuidador` VARCHAR(45) NOT NULL,
  `correo_electronico_cuidador` VARCHAR(45) NOT NULL,
  `telefono_cuidador` VARCHAR(45) NOT NULL,
  `tipo_cuidador` ENUM('paseador', 'entrenador', 'guarderia') NOT NULL,
  `experiencia` INT NULL,
  `tarifas` DECIMAL(10, 2) NULL,
  `especialidad` VARCHAR(45) NULL,
  `certificaciones` TEXT NULL,
  `direccion` VARCHAR(125) NULL,
  `capacidad` INT NULL,
  PRIMARY KEY (`IDcuidador`)
) ENGINE = InnoDB;

-- 4. Tabla servicio (con índices y claves foráneas corregidas)
CREATE TABLE IF NOT EXISTS `appet`.`servicio` (
  `IDservicio` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `IDcuidador` BIGINT(12) NOT NULL,
  `descripcion_servicio` TEXT NULL,
  `precio` DECIMAL(10, 2) NULL,
  `IDmascota` BIGINT(12) NOT NULL,
  `IDpropietario` BIGINT(12) NOT NULL,
  `tipo_servicio` VARCHAR(45) NULL,
  PRIMARY KEY (`IDservicio`),
  INDEX `fk_servicio_mascota_idx` (`IDmascota`),
  INDEX `fk_servicio_propietario_idx` (`IDpropietario`),
  INDEX `fk_servicio_cuidador_idx` (`IDcuidador`),
  CONSTRAINT `fk_servicio_mascota` 
    FOREIGN KEY (`IDmascota`) 
    REFERENCES `appet`.`mascota` (`IDmascota`)
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_servicio_propietario` 
    FOREIGN KEY (`IDpropietario`) 
    REFERENCES `appet`.`propietario` (`IDpropietario`)
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_servicio_cuidador` 
    FOREIGN KEY (`IDcuidador`) 
    REFERENCES `appet`.`cuidador` (`IDcuidador`)
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- 5. Tabla Agenda
CREATE TABLE IF NOT EXISTS `appet`.`Agenda` (
  `IDagenda` INT NOT NULL AUTO_INCREMENT,
  `fecha` DATE NULL,
  `hora_inicio` TIME NULL,
  `hora_fin` TIME NULL,
  `IDservicio` BIGINT(12) NOT NULL,
  PRIMARY KEY (`IDagenda`),
  INDEX `fk_Agenda_servicio_idx` (`IDservicio`),
  CONSTRAINT `fk_Agenda_servicio` 
    FOREIGN KEY (`IDservicio`) 
    REFERENCES `appet`.`servicio` (`IDservicio`)
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla historial_servicio (para registrar servicios completados)
CREATE TABLE IF NOT EXISTS `appet`.`historial_servicio` (
  `IDhistorial` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `IDservicio` BIGINT(12) NOT NULL,
  `fecha_inicio` DATETIME NOT NULL, -- Cuándo comenzó el servicio
  `fecha_fin` DATETIME NULL, -- Cuándo finalizó (puede ser NULL si está en progreso)
  `estado` ENUM('completado', 'cancelado', 'en_progreso') NOT NULL,
  `notas` TEXT NULL, -- Observaciones adicionales
  PRIMARY KEY (`IDhistorial`),
  INDEX `fk_historial_servicio1_idx` (`IDservicio`),
  CONSTRAINT `fk_historial_servicio1` 
    FOREIGN KEY (`IDservicio`) 
    REFERENCES `appet`.`servicio` (`IDservicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;

-- Tabla calificacion_cuidador (para puntuar y comentar servicios)
CREATE TABLE IF NOT EXISTS `appet`.`calificacion_cuidador` (
  `IDcalificacion` BIGINT(12) NOT NULL AUTO_INCREMENT,
  `IDpropietario` BIGINT(12) NOT NULL, -- Quién califica
  `IDcuidador` BIGINT(12) NOT NULL, -- A quién se califica
  `IDservicio` BIGINT(12) NOT NULL, -- Servicio relacionado
  `puntuacion` TINYINT NOT NULL CHECK (puntuacion BETWEEN 1 AND 5), -- Ej: 1-5 estrellas
  `comentario` TEXT NULL,
  `fecha_calificacion` DATETIME DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`IDcalificacion`),
  INDEX `fk_calificacion_propietario1_idx` (`IDpropietario`),
  INDEX `fk_calificacion_cuidador1_idx` (`IDcuidador`),
  INDEX `fk_calificacion_servicio1_idx` (`IDservicio`),
  CONSTRAINT `fk_calificacion_propietario1` 
    FOREIGN KEY (`IDpropietario`) 
    REFERENCES `appet`.`propietario` (`IDpropietario`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_calificacion_cuidador1` 
    FOREIGN KEY (`IDcuidador`) 
    REFERENCES `appet`.`cuidador` (`IDcuidador`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_calificacion_servicio1` 
    FOREIGN KEY (`IDservicio`) 
    REFERENCES `appet`.`servicio` (`IDservicio`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;