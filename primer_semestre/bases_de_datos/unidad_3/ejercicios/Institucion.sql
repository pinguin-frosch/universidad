CREATE DATABASE INSTITUCION;

USE INSTITUCION;

CREATE TABLE PARTICIPANTE
(
rut varchar(15) PRIMARY KEY NOT NULL,
nombre varchar(20) NOT NULL,
domicilio varchar(200),
telefono varchar(15),
banco varchar(50) NOT NULL,
numero_cuenta int NOT NULL
)

CREATE TABLE TIPO_PAGO
(
codigo int PRIMARY KEY NOT NULL,
nombre varchar(40) NOT NULL
)

CREATE TABLE CLIENTE
(
rut varchar(15) PRIMARY KEY NOT NULL,
telefono varchar(15) NOT NULL,
domicilio varchar(200),
razon_social varchar(200) NOT NULL
)

CREATE TABLE PAGO
(
numero_pago int PRIMARY KEY NOT NULL,
rut_participante varchar(15) FOREIGN KEY REFERENCES PARTICIPANTE(rut),
codigo_tipo_pago int FOREIGN KEY REFERENCES TIPO_PAGO(codigo),
concepto varchar(100) NOT NULL,
cantidad int NOT NULL,
fecha_pago date NOT NULL
)

CREATE TABLE PROYECTO
(
codigo int PRIMARY KEY NOT NULL,
rut_cliente varchar(15) FOREIGN KEY REFERENCES CLIENTE(rut),
descripcion varchar(80),
presupuesto int NOT NULL,
fecha_inicio date NOT NULL,
fecha_termino date NOT NULL
)

CREATE TABLE EQUIPO
(
rut_participante varchar(15) FOREIGN KEY REFERENCES PARTICIPANTE(rut),
codigo_proyecto int FOREIGN KEY REFERENCES PROYECTO(codigo)
)