CREATE DATABASE UNIVERSIDAD

USE UNIVERSIDAD
CREATE TABLE ALUMNO(
rut varchar(20) PRIMARY KEY NOT NULL,
nombre varchar(20) NOT NULL,
apellido varchar(25) NOT NULL,
fecha_nacimiento date NOT NULL,
teléfono varchar(15), 
correo varchar(50) NOT NULL,
dirección varchar(200) NOT NULL,
)

CREATE TABLE CARRERA(
código_carrera int PRIMARY KEY NOT NULL, 
duración int NOT NULL, 
nombre varchar(60) NOT NULL, 
cupos int NOT NULL, 
encargado varchar(80) NOT NULL,
)

CREATE TABLE ASIGNATURA(
codigo_asignatura int PRIMARY KEY NOT NULL,
duracion int NOT NULL,
nombre varchar(70),
)

CREATE TABLE DOCENTE(
rut varchar(20) PRIMARY KEY NOT NULL,
nombre varchar(20) NOT NULL, 
apellido varchar(25) NOT NULL,
fecha_nacimiento date NOT NULL, 
telefono varchar(15) NOT NULL,
correo varchar(50) NOT NULL,
direccion varchar(200) NOT NULL,
especialidad varchar(60) NOT NULL,
codigo_asignatura_designada int FOREIGN KEY REFERENCES ASIGNATURA(codigo_asignatura)
)

ALTER TABLE DOCENTE ADD codigo_asignatura_designada int FOREIGN KEY REFERENCES ASIGNATURA(codigo_asignatura)


