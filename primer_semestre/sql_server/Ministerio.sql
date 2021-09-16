CREATE DATABASE MINISTERIO;

USE MINISTERIO;

CREATE TABLE HOSPITAL
(
codigo int PRIMARY KEY NOT NULL,
nombre varchar(50) NOT NULL,
direccion varchar(200) NOT NULL,
telefono varchar(15) NOT NULL,
cantidad_camas int NOT NULL
)

CREATE TABLE LABORATORIO
(
codigo int PRIMARY KEY NOT NULL,
nombre varchar(50) NOT NULL,
direccion varchar(200) NOT NULL,
telefono varchar(15) NOT NULL
)

CREATE TABLE SALA
(
codigo int PRIMARY KEY NOT NULL,
codigo_hospital int FOREIGN KEY REFERENCES HOSPITAL(codigo),
nombre varchar(30) NOT NULL,
cantidad_camas int NOT NULL
)

CREATE TABLE MEDICO
(
rut varchar(15) PRIMARY KEY NOT NULL,
codigo_hospital int FOREIGN KEY REFERENCES HOSPITAL(codigo),
nombre varchar(50) NOT NULL,
especialidad varchar(50)
)

CREATE TABLE PACIENTE
(
rut varchar(15) PRIMARY KEY NOT NULL,
codigo_sala int FOREIGN KEY REFERENCES SALA(codigo),
numero_registro int NOT NULL,
numero_cama int NOT NULL,
nombre varchar(50) NOT NULL,
direccion varchar(200) NOT NULL,
fecha_nacimiento date NOT NULL,
sexo varchar(10) NOT NULL
)

CREATE TABLE DIAGNOSTICO
(
codigo int PRIMARY KEY NOT NULL,
rut_paciente varchar(15) FOREIGN KEY REFERENCES PACIENTE(rut),
tipo varchar(40) NOT NULL,
complicaciones varchar(150),
fecha date NOT NULL
)

CREATE TABLE [TRABAJO DIAGNOSTICO]
(
codigo_hospital int FOREIGN KEY REFERENCES HOSPITAL(codigo),
codigo_laboratorio int FOREIGN KEY REFERENCES LABORATORIO(codigo),
descripcion varchar(100) NOT NULL,
fecha date NOT NULL
)

CREATE TABLE [ATENCION MEDICA]
(
rut_paciente varchar(15) FOREIGN KEY REFERENCES PACIENTE(rut),
rut_medico varchar(15) FOREIGN KEY REFERENCES MEDICO(rut),
fecha date NOT NULL
)