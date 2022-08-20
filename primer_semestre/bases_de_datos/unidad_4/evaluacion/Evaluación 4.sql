CREATE DATABASE UNIVERSIDAD
USE UNIVERSIDAD

CREATE TABLE asignatura
(
código varchar(10) NOT NULL PRIMARY KEY,
nombre varchar(60) NOT NULL,
duración int
)

CREATE TABLE docente
(
rut varchar(15) NOT NULL PRIMARY KEY,
código_asignatura varchar(10) NOT NULL FOREIGN KEY REFERENCES asignatura(código),
nombre varchar(20) NOT NULL,
apellido varchar(20) NOT NULL,
fecha_nacimiento date,
teléfono varchar(15) NOT NULL,
correo varchar(40) NOT NULL,
dirección varchar(100) NOT NULL,
especialidad varchar(30)
)

CREATE TABLE alumno
(
rut varchar(15) NOT NULL PRIMARY KEY,
nombre varchar(20) NOT NULL,
apellido varchar(20) NOT NULL,
fecha_nacimiento date,
teléfono varchar(15) NOT NULL,
correo varchar(40) NOT NULL,
dirección varchar(100)
)

CREATE TABLE carrera
(
código varchar(10) NOT NULL PRIMARY KEY,
duración int,
nombre varchar(40) NOT NULL,
cupos int NOT NULL
)

CREATE TABLE evaluación
(
fecha date NOT NULL,
nombre varchar(30) NOT NULL,
nota float NOT NULL,
rut_alumno varchar(15) NOT NULL FOREIGN KEY REFERENCES alumno(rut),
rut_docente varchar(15) NOT NULL FOREIGN KEY REFERENCES docente(rut),
CONSTRAINT pk_evaluación PRIMARY KEY(fecha, rut_alumno, rut_docente)
)

CREATE TABLE toma_de_ramo
(
semestre varchar(30) NOT NULL,
código_asignatura varchar(10) NOT NULL FOREIGN KEY REFERENCES asignatura(código),
rut_alumno varchar(15) NOT NULL FOREIGN KEY REFERENCES alumno(rut),
CONSTRAINT pk_toma_de_ramo PRIMARY KEY(semestre, código_asignatura, rut_alumno) 
)

CREATE TABLE malla_curricular
(
código_carrera varchar(10) NOT NULL FOREIGN KEY REFERENCES carrera(código),
código_asignatura varchar(10) NOT NULL FOREIGN KEY REFERENCES asignatura(código),
CONSTRAINT pk_malla_curricular PRIMARY KEY(código_carrera, código_asignatura)
)

CREATE TABLE matrícula
(
código varchar(20) NOT NULL PRIMARY KEY,
rut_alumno varchar(15) NOT NULL FOREIGN KEY REFERENCES alumno(rut),
código_carrera varchar(10) NOT NULL FOREIGN KEY REFERENCES carrera(código)
)

INSERT INTO asignatura VALUES
('26849643', 'Historia', 80),
('32426853', 'Lenguaje', 100),
('23452552', 'Informática', 90),
('34234356', 'Matemática', 120),
('34242352', 'Inglés', 80),
('38254325', 'Música', 70),
('87954443', 'Ciencias', 80),
('56464564', 'Base de datos', 70),
('65646465', 'Arte', 50),
('83623243', 'Educación física', 50)

INSERT INTO alumno(rut, nombre, apellido, fecha_nacimiento, teléfono, correo) VALUES
('11.622.787-8', 'Maria', 'Cayancud', '1983-05-12', '+56945682795', 'maria.cayancud@gmail.com'),
('17.189.489-1', 'Benjamin', 'Mera', '1996-04-09', '+56966845978', 'benjamin.mera@gmail.com'),
('10.707.959-9', 'Maria', 'Domingez', '1965-08-12', '+56971897648', 'maria.domingez@gmail.com'),
('21.027.935-0', 'Sebastian', 'Silva', '2002-10-09', '+56975646872', 'sebastian.silva@gmail.com'),
('11.118.923-0', 'Luis', 'Martos', '1857-12-26', '+56938694572', 'luis.martos@gmail.com'),
('14.616.426-9', 'Evangelina', 'Muriel', '1967-04-08', '+56912587569', 'evangelina.muriel@gmail.com'),
('13.132.129-5', 'Cristobal', 'Alonso', '1972-02-08', '+56987296482', 'cristobal.alonso@gmail.com'),
('15.871.613-2', 'Gisela', 'Sevillano', '1996-05-07', '+56978468216', 'gisela.servillano@gmail.com'),
('11.205.123-6', 'Alonso', 'Vilches', '1987-06-10', '+56987264987', 'alonso.vilches@gmail.com'),
('23.490.621-6', 'Brais', 'Becerra', '2003-10-27', '+56971842385', 'brais.becerra@gmail.com')

INSERT INTO carrera VALUES
('1221323', 8, 'Ingeniería en informática', 120),
('8123728', 8, 'Gastronomía', 120),
('2731831', 8, 'Telecomunicaciones', 90),
('5656756', 8, 'Psicología', 90),
('8774324', 8, 'Contabilidad', 120),
('7769987', 8, 'Derecho', 80),
('8756789', 8, 'Artes visuales', 60),
('6544356', 8, 'Moda y confección', 70),
('7676892', 8, 'Medicina', 150),
('6321332', 8, 'Química', 70)

INSERT INTO docente VALUES
('18.630.665-1', '26849643', 'Maximo', 'Vivas','1965-10-11', '+56965948098', 'maximo.vivas@blorem.edu', 'Lorem ipsum 15', 'Historia'),
('14.743.281-k', '32426853', 'Debora', 'Arjona', '1969-02-18', '+56972520407', 'debora.arjona@blorem.edu', 'Kohler Fork 4148', 'Lenguaje'),
('24.014.044-1', '23452552', 'Luis', 'Antonio', '1997-01-14', '+56965989896', 'luis.antonio@blorem.edu', 'Avery Flats 5595', 'Informática'),
('12.826.517-1', '34234356', 'Aya', 'Suarez', '1981-10-08', '+56977125292', 'aya.suarez@blorem.edu', 'Anissa Meadows 74515', 'Matemática'),
('24.004.044-1', '34242352', 'Adolfo', 'Palma', '1995-06-13', '+56979035538', 'adolfo.palma@blorem.edu', 'Citlalli Junction 8291', 'Gastronomía'),
('11.075.747-6', '38254325', 'Regina', 'Guerrero', '1977-04-14', '+56989008682', 'regina.guerrero@blorem.edu', 'Noah Ville 5662', 'Contabilidad'),
('20.761.420-3', '87954443', 'Gabriela', 'Sancho', '1999-09-07', '+56961834736', 'gabriela.sancho@blorem.edu', 'Turner Lodge 745', 'Derecho'),
('17.421.599-5', '56464564', 'Maria', 'Remedios', '2003-06-12', '+56969164594', 'maria.remedios@blorem.edu', 'Cassin Hills 010', 'Base de datos'),
('15.702.541-4', '65646465', 'Mauro', 'Alcalde', '1974-06-24', '+56965376770', 'mauro.alcalde@blorem.edu', 'Annabell Union 954', 'Geología'),
('18.669.830-4', '83623243', 'Enzo', 'Vilar', '2000-01-15', '+56981674340', 'enso.vilar@blorem.edu', 'Mayert Crossing 461', 'Telecomunicaciones')

INSERT INTO matrícula VALUES 
('ASD12376456789', '11.622.787-8', '1221323'),
('GTD97823478483', '17.189.489-1', '8123728'),
('THF32546576865', '10.707.959-9', '2731831'),
('FFT64456546686', '21.027.935-0', '5656756'),
('LTF54545646645', '11.118.923-0', '8774324'),
('VGF97765445345', '14.616.426-9', '7769987'),
('IUFR2423442424', '13.132.129-5', '8756789'),
('GFG34343243243', '11.205.123-6', '6544356'),
('DFGG9876543534', '23.490.621-6', '7676892'),
('DNSD3472348273', '15.871.613-2', '6321332')

INSERT INTO evaluación VALUES
('2021-07-08', 'Polinomios 4', 6.7, '11.622.787-8', '12.826.517-1'),
('2021-07-08', 'Polinomios 4', 4.1, '17.189.489-1', '12.826.517-1'),
('2021-07-08', 'Polinomios 4', 5.9, '10.707.959-9', '12.826.517-1'),
('2021-07-08', 'Polinomios 4', 7.0, '21.027.935-0', '12.826.517-1'),
('2021-07-20', 'Programas en Python', 5.5, '11.118.923-0', '24.004.044-1'),
('2021-07-20', 'Programas en Python', 6.3, '14.616.426-9', '24.014.044-1'),
('2021-07-20', 'Programas en Python', 6.7, '13.132.129-5', '24.014.044-1'),
('2021-08-10', 'Evaluación 4', 7.0, '11.205.123-6', '17.421.599-5'),
('2021-08-10', 'Evaluación 4', 7.0, '15.871.613-2', '17.421.599-5'),
('2021-08-10', 'Evaluación 4', 6.3, '23.490.621-6', '17.421.599-5')

INSERT INTO toma_de_ramo VALUES
('otoño', '26849643', '11.622.787-8'),
('otoño', '32426853', '17.189.489-1'),
('otoño', '23452552', '10.707.959-9'),
('otoño', '34234356', '21.027.935-0'),
('otoño', '34242352', '11.118.923-0'),
('otoño', '38254325', '14.616.426-9'),
('otoño', '87954443', '13.132.129-5'),
('primavera', '56464564', '11.205.123-6'),
('primavera', '65646465', '15.871.613-2'),
('primavera', '83623243', '23.490.621-6')

INSERT INTO malla_curricular VALUES
('1221323', '26849643'),
('8123728', '32426853'),
('2731831', '23452552'),
('5656756', '34234356'),
('8774324', '34242352'),
('7769987', '38254325'),
('8756789', '87954443'),
('6544356', '56464564'),
('7676892', '65646465'),
('6321332', '83623243')

SELECT docente.nombre + ' ' + docente.apellido AS 'Nombre docente', asignatura.nombre AS 'Nombre asignatura' FROM docente INNER JOIN asignatura ON asignatura.código = docente.código_asignatura ORDER BY asignatura.nombre

SELECT AVG(nota) AS 'Promedio de notas', nombre AS 'Nombre evaluación' FROM evaluación GROUP BY nombre