CREATE DATABASE TIENDA
USE DATABASE TIENDA

CREATE TABLE clientes(
rut varchar(15) NOT NULL PRIMARY KEY,
nombre varchar(30) NOT NULL,
fecha_nacimiento date NOT NULL,
direccion varchar(40) NOT NULL,
ciudad varchar(30) NOT NULL
)

CREATE TABLE productos(
codigo_producto int NOT NULL PRIMARY KEY,
descripcion varchar(50) NOT NULL,
valor float NOT NULL,
cantidad int NOT NULL
)

CREATE TABLE ventas(
numero_venta int NOT NULL PRIMARY KEY,
cantidad_venta int NOT NULL,
monto_venta float NOT NULL,
fecha_venta date NOT NULL,
rut_cliente varchar(15) NOT NULL FOREIGN KEY REFERENCES clientes(rut),
codigo_producto int NOT NULL FOREIGN KEY REFERENCES productos(codigo_producto)
)

INSERT INTO productos VALUES
(100, 'Televisor led', 250000, 30),
(200, 'Equipo musical', 80000, 15),
(300, 'Impresora', 50000, 60),
(400, 'Computadores', 550000, 40),
(500, 'Maquinas registradoras', 100000, 90),
(600, 'Celular', 120000, 120),
(700, 'Audífono', 10000, 200),
(800, 'Mouse', 20000, 200),
(900, 'Tablet', 80000, 40),
(1000, 'Modem', 15000, 1000)

INSERT INTO clientes VALUES
('14.235.456-6', 'Miguel Barrios', '1979-10-13', 'Arturo Prat 882', 'Los Ángeles'),
('16.433.865-1', 'Rafael Contreras', '1987-02-17', 'Santa Teresa 302', 'Santa Bárbara'),
('20.962.235-4', 'María Pulgar', '2002-03-21', 'Camilo Henríquez 403', 'Angol'),
('16.597.257-8', 'Jason Mellado', '1987-08-27','Baquedano 133', 'Quilleco'),
('9.463.982-4', 'Carolina Aguilar', '1963-10-14', 'Sargento Aldea 1002', 'Quilaco'),
('17.198.267-3', 'Oscar Sepúlveda', '1989-08-07', 'Teniente Merino 224', 'Santiago'),
('13.972.268-1', 'Natalia Quiroz', '1978-11-30', 'Valle del Elqui 773', 'Temuco'),
('15.158.782.7', 'Héctor Lorca', '1982-10-23', 'Diego Portalez 543', 'Concepción'),
('18.192.882-5', 'Elizabeth Parra', '1992-12-15', 'Freire 523', 'Mulchén'),
('21.019.973-4', 'Millaray Fernandez', '2002-05-13', 'Carrera 125', 'Renaico')

INSERT INTO ventas VALUES
(5431841, 4, 60000, '2021-06-16', '16.433.865-1', 1000),
(8684321, 1, 80000, '2021-06-14', '13.972.268-1', 200),
(5434833, 2, 200000, '2021-06-24', '18.192.882-5', 500),
(8715462, 3, 240000, '2021-06-20', '16.597.257-8', 900),
(6421153, 8, 80000, '2021-05-18', '21.019.973-4', 700),
(9863245, 1, 550000, '2021-06-28', '15.158.782.7', 400),
(1357145, 6, 120000, '2021-06-19', '14.235.456-6', 800),
(8752462, 5, 250000, '2021-05-26', '9.463.982-4', 300),
(1834578, 2, 240000, '2021-06-27', '17.198.267-3', 600),
(2815861, 1, 250000, '2021-06-11', '20.962.235-4', 100)

SELECT clientes.rut, clientes.nombre, clientes.fecha_nacimiento, clientes.direccion, clientes.ciudad, ventas.codigo_producto
FROM clientes INNER JOIN ventas ON clientes.rut = ventas.rut_cliente ORDER BY ventas.codigo_producto

SELECT AVG(cantidad_venta) AS 'Promedio de ventas', codigo_producto AS 'Código producto'
FROM ventas GROUP BY codigo_producto