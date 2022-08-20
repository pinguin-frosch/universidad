CREATE TABLE ciudad (
    codigo_ciudad INTEGER NOT NULL,
    nombre_ciudad VARCHAR2(50) NOT NULL
);

ALTER TABLE ciudad ADD CONSTRAINT ciudad_pk PRIMARY KEY ( codigo_ciudad );

CREATE TABLE empleado (
    rut_empleado     VARCHAR2(13) NOT NULL,
    nombre_empleado  VARCHAR2(50) NOT NULL,
    edad             INTEGER NOT NULL,
    sexo_empleado    VARCHAR2(10) NOT NULL,
    sueldo_empleado  INTEGER NOT NULL,
    fk_codigo_ciudad INTEGER NOT NULL
);

ALTER TABLE empleado ADD CONSTRAINT empleado_pk PRIMARY KEY ( rut_empleado );

ALTER TABLE empleado
    ADD CONSTRAINT empleado_ciudad_fk FOREIGN KEY ( fk_codigo_ciudad )
        REFERENCES ciudad ( codigo_ciudad );

-- 0. Insertar valores
INSERT INTO ciudad VALUES
(1111, 'Los Ángeles');

INSERT INTO ciudad VALUES
(2222, 'Santa Bárbara');

INSERT INTO ciudad VALUES
(3333, 'Angol');

INSERT INTO ciudad VALUES
(4444, 'Concepción');

INSERT INTO ciudad VALUES
(5555, 'Yumbel');

INSERT INTO ciudad VALUES
(6666, 'Negrete');

INSERT INTO ciudad VALUES
(7777, 'Antuco');

INSERT INTO ciudad VALUES
(8888, 'Quilaco');

INSERT INTO ciudad VALUES
(9999, 'Temuco');

INSERT INTO empleado VALUES
('12.749.614-5', 'Alexandre Lobato', 24, 'masculino', 365892, 1111);

INSERT INTO empleado VALUES
('20.945.093-3', 'Amalia Linares', 55, 'femenino', 382928, 1111);

INSERT INTO empleado VALUES
('14.702.488-6', 'Marcelo Cuellar', 51, 'masculino', 695259, 1111);

INSERT INTO empleado VALUES
('16.148.409-1', 'Claudia Vilches', 35, 'femenino', 396344, 2222);

INSERT INTO empleado VALUES
('15.328.187-4', 'Eduardo Valero', 52, 'masculino', 155907, 2222);

INSERT INTO empleado VALUES
('10.950.303-7', 'Magdalena Tapia', 30, 'femenino', 243778, 2222);

INSERT INTO empleado VALUES
('11.534.208-8', 'Norberto Carbonell', 26, 'masculino', 163467, 3333);

INSERT INTO empleado VALUES
('13.374.337-5', 'Ana Rosa Ramos', 42, 'femenino', 447985, 3333);

INSERT INTO empleado VALUES
('13.178.524-0', 'Fulgencio Espejo', 15, 'masculino', 657740, 3333);

INSERT INTO empleado VALUES
('17.181.146-5', 'Filomena Barrientos', 62, 'femenino', 411376, 4444);

INSERT INTO empleado VALUES
('12.631.365-9', 'Moussa Saiz', 68, 'masculino', 506441, 4444);

INSERT INTO empleado VALUES
('13.663.274-4', 'Fernanda Luna', 33, 'femenino', 386707, 4444);

INSERT INTO empleado VALUES
('14.845.110-9', 'Aitor Santamaria', 51, 'masculino', 683952, 5555);

INSERT INTO empleado VALUES
('10.776.404-6', 'Guadalupe Betancor', 26, 'femenino', 376418, 5555);

INSERT INTO empleado VALUES
('12.424.364-5', 'Roger Mansilla', 39, 'masculino', 535039, 5555);

INSERT INTO empleado VALUES
('17.686.170-3', 'Isabel Teruel', 54, 'femenino', 517488, 6666);

INSERT INTO empleado VALUES
('11.817.813-0', 'Ivan Lara', 68, 'masculino', 612358, 6666);

INSERT INTO empleado VALUES
('16.887.296-8', 'Lucia Mejia', 31, 'femenino', 448690, 6666);

INSERT INTO empleado VALUES
('11.596.757-6', 'Bruno Ripoll', 28, 'masculino', 304086, 7777);

INSERT INTO empleado VALUES
('15.454.752-5', 'Micaela Vargas', 28, 'femenino', 230817, 7777);

INSERT INTO empleado VALUES
('14.136.707-2', 'Abdeslam Arroyo', 67, 'masculino', 318114, 7777);

INSERT INTO empleado VALUES
('9.320.568-5', 'Felisa Toribio', 21, 'femenino', 276989, 8888);

INSERT INTO empleado VALUES
('10.802.259-0', 'Hamza Zhu', 59, 'masculino', 203466, 8888);

INSERT INTO empleado VALUES
('16.105.946-3', 'Olga Hernandez', 30, 'femenino', 456966, 8888);

INSERT INTO empleado VALUES
('10.914.130-5', 'Anastasio Barragan', 52, 'masculino', 489794, 9999);

INSERT INTO empleado VALUES
('9.403.085-4', 'Delia Toledano', 37, 'femenino', 693392, 9999);

INSERT INTO empleado VALUES
('7.974.309-7', 'Victor Pino', 57, 'masculino', 549279, 9999);

-- 1. Cree una consulta que muestre el sexo y la cantidad de empleados agrupados por el sexo del empleado.
SELECT sexo_empleado AS "Sexo", COUNT(*) AS "Cantidad por sexo" FROM empleado GROUP BY sexo_empleado;

-- 2. Cree una consulta que muestre el nombre de la ciudad y la cantidad de empleados, agrupados por el nombre de la ciudad.
SELECT ciudad.nombre_ciudad AS "Ciudad", COUNT(*) AS "Cantidad de empleados" FROM ciudad INNER JOIN empleado ON ciudad.codigo_ciudad = empleado.fk_codigo_ciudad GROUP BY ciudad.nombre_ciudad;

-- 3. Cree una consulta que obtenga el sexo y la cantidad de empleados agrupados por el sexo del empleado, se solicita que se muestren solo los pertenecientes a la ciudad de los Ángeles (deben agregar esta ciudad en la base de datos)
SELECT empleado.sexo_empleado as "Sexo", COUNT(sexo_empleado) AS "Cantidad por sexo" FROM empleado INNER JOIN ciudad ON ciudad.codigo_ciudad = empleado.fk_codigo_ciudad WHERE ciudad.nombre_ciudad = 'Los Ángeles' GROUP BY empleado.sexo_empleado;

-- 4. Cree una consulta que muestre el nombre de la ciudad y la edad de su mayor empleado.
SELECT ciudad.nombre_ciudad AS "Ciudad", MAX(empleado.edad) AS "Mayor edad" FROM ciudad INNER JOIN empleado ON ciudad.codigo_ciudad = empleado.fk_codigo_ciudad GROUP BY ciudad.nombre_ciudad;

-- 5. Cree una consulta que muestre el nombre de la ciudad, sexo y el promedio del sueldo de sus empleados, agrupados por nombre, ciudad y sexo.
SELECT ciudad.nombre_ciudad AS "Ciudad", empleado.sexo_empleado AS "Sexo", AVG(empleado.sueldo_empleado) AS "Promedio de sueldo" FROM ciudad INNER JOIN empleado ON ciudad.codigo_ciudad = empleado.fk_codigo_ciudad GROUP BY ciudad.nombre_ciudad, empleado.sexo_empleado ORDER BY ciudad.nombre_ciudad, empleado.sexo_empleado ASC;

-- 6. Cree una consulta que muestre el nombre de la ciudad y el sueldo total a pagar a todos sus empleados agrupados por ciudad.
SELECT ciudad.nombre_ciudad AS "Ciudad", SUM(empleado.sueldo_empleado) AS "Sueldo a pagar" FROM ciudad INNER JOIN empleado ON ciudad.codigo_ciudad = empleado.fk_codigo_ciudad GROUP BY ciudad.nombre_ciudad ORDER BY ciudad.nombre_ciudad ASC;

-- 7. Cree una consulta que muestre el nombre de la ciudad, el sexo y la cantidad de empleados que sean menor de edad (menor a 18 años)
SELECT ciudad.nombre_ciudad AS "Ciudad", empleado.sexo_empleado "Sexo", COUNT(*) AS "Menores a 18" FROM ciudad INNER JOIN empleado ON ciudad.codigo_ciudad = empleado.fk_codigo_ciudad WHERE empleado.edad < 18 GROUP BY ciudad.nombre_ciudad, empleado.sexo_empleado ORDER BY ciudad.nombre_ciudad, empleado.sexo_empleado;