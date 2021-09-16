CREATE DATABASE TIENDA

USE TIENDA

CREATE TABLE PROVEEDOR(
rut varchar(20) PRIMARY KEY NOT NULL,
nombre varchar(20) NOT NULL,
direccion varchar(200) NOT NULL,
telefono varchar(20) NOT NULL,
pagina_web varchar(250)
)

CREATE TABLE CLIENTE(
rut varchar(20) PRIMARY KEY NOT NULL,
nombre varchar(20) NOT NULL,
direccion varchar(200) NOT NULL,
telefono varchar(20)
)

CREATE TABLE CATEGORIA(
id int PRIMARY KEY NOT NULL,
nombre varchar(30) NOT NULL,
descripcion varchar(100)
)

CREATE TABLE PRODUCTO(
id int PRIMARY KEY NOT NULL,
fk_rut varchar(20) FOREIGN KEY REFERENCES PROVEEDOR(rut),
fk_id int FOREIGN KEY REFERENCES CATEGORIA(id)
)

CREATE TABLE VENTA(
fk_id int FOREIGN KEY REFERENCES PRODUCTO(id),
fk_rut varchar(20) FOREIGN KEY REFERENCES CLIENTE(rut),
fecha datetime,
descuento float,
monto_final float,
precio float,
cantidad_vendida int,
monto_por_producto float
)