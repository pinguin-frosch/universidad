CREATE TABLE alumno (
    rut_alumno              VARCHAR2(13) NOT NULL,
    nombre_alumno           VARCHAR2(30) NOT NULL,
    fecha_nacimiento_alumno DATE NOT NULL,
    telefono_alumno         CHAR(8) NOT NULL
);

ALTER TABLE alumno ADD CONSTRAINT alumno_pk PRIMARY KEY ( rut_alumno );

CREATE TABLE asignatura (
    codigo_asignatura      VARCHAR2(10) NOT NULL,
    nombre_asignatura      VARCHAR2(20) NOT NULL,
    descripción_asignatura VARCHAR2(200) NOT NULL
);

ALTER TABLE asignatura ADD CONSTRAINT asignatura_pk PRIMARY KEY ( codigo_asignatura );

CREATE TABLE cursa_asignatura (
    codigo_cursa_asignatura INTEGER NOT NULL,
    fk_rut_alumno           VARCHAR2(13) NOT NULL,
    fk_codigo_asignatura    VARCHAR2(10) NOT NULL,
    fecha_inicio            DATE NOT NULL,
    fecha_fin               DATE NOT NULL
);

ALTER TABLE cursa_asignatura ADD CONSTRAINT cursa_asignatura_pk PRIMARY KEY ( codigo_cursa_asignatura );

CREATE TABLE notas (
    codigo_nota         INTEGER NOT NULL,
    descripcion_nota    VARCHAR2(20) NOT NULL,
    nota_obtenida       FLOAT NOT NULL,
    fk_cursa_asignatura INTEGER NOT NULL
);

ALTER TABLE notas ADD CONSTRAINT notas_pk PRIMARY KEY ( codigo_nota );

ALTER TABLE cursa_asignatura
    ADD CONSTRAINT cursa_asignatura_alumno_fk FOREIGN KEY ( fk_rut_alumno )
        REFERENCES alumno ( rut_alumno );

ALTER TABLE cursa_asignatura
    ADD CONSTRAINT cursa_asignatura_asignatura_fk FOREIGN KEY ( fk_codigo_asignatura )
        REFERENCES asignatura ( codigo_asignatura );

ALTER TABLE notas
    ADD CONSTRAINT notas_cursa_asignatura_fk FOREIGN KEY ( fk_cursa_asignatura )
        REFERENCES cursa_asignatura ( codigo_cursa_asignatura );
        
-- Insertar alumnos(rut, nombre, nacimiento, teléfono)
        
INSERT INTO alumno VALUES(
    '21.019.385-5', 'Gabriel Barrientos', TO_DATE('14-01-2003', 'dd-mm-yyyy'), '66842540'
);

INSERT INTO alumno VALUES(
    '21.234.653-9', 'Charlotte Rodriguez', TO_DATE('20-7-2002', 'dd-mm-yyyy'), '16777017'
);

INSERT INTO alumno VALUES(
    '20.022.825-1', 'Jenifer Cantero', TO_DATE('23-01-1999', 'dd-mm-yyyy'), '98588995'
);

INSERT INTO alumno VALUES(
    '20.802.829-4', 'Alexia Morales', TO_DATE('08-08-2001', 'dd-mm-yyyy'), '56259831'
);

INSERT INTO alumno VALUES(
    '20.964.449-5', 'Gerardo Vega', TO_DATE('28-03-2002', 'dd-mm-yyyy'), '73042780'
);

-- Insertar asignaturas(código, nombre, descripción)

INSERT INTO asignatura VALUES(
    '0000', 'bases de datos', 'permite desarrollar la habilidad de interactuar con bases de datos mediante consultas avanzadas'
);

INSERT INTO asignatura VALUES(
    '1111', 'programación', 'tiene el propósito de desarrollar el pensamiento estructurado a la hora de resolver problemas'
);

INSERT INTO asignatura VALUES(
    '2222', 'cálculo', 'ayuda a desarrollar el pensamiento análitico y funcional para resolver problemas del mundo real'
);

INSERT INTO asignatura VALUES(
    '3333', 'sistemas operativos', 'enseña a trabajar en diferentes sistemas operativos según la tarea que se necesite'
);

INSERT INTO asignatura VALUES(
    '4444', 'desarrollo ágil', 'tiene como objetivo mostrar las habilidades que se necesitan a la hora de desarrollar software en equipo'
);

-- Insertar cursa_asignatura(codigo_cursa_asignatura, fk_rut_alumno, fk_codigo_asignatura, fecha_inicio, fecha_fin)

INSERT INTO cursa_asignatura VALUES(
    0, '21.019.385-5', '0000', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    1, '21.019.385-5', '1111', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-12-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    2, '21.019.385-5', '2222', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('07-01-2022', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    3, '21.234.653-9', '1111', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-12-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    4, '21.234.653-9', '2222', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('07-01-2022', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    5, '21.234.653-9', '3333', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('14-12-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    6, '20.022.825-1', '2222', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('07-01-2022', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    7, '20.022.825-1', '3333', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('14-12-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    8, '20.022.825-1', '4444', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('26-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    9, '20.802.829-4', '3333', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('14-12-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    10, '20.802.829-4', '4444', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('26-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    11, '20.802.829-4', '0000', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    12, '20.964.449-5', '4444', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('26-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    13, '20.964.449-5', '0000', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    14, '20.964.449-5', '1111', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-12-2021', 'dd-mm-yyyy')
);

-- Insertas notas(codigo_nota, descripción, nota_obtenida, fk_cursa_asignatura)

INSERT INTO notas VALUES(
    0, 'evaluación 1', 68, 0
);

INSERT INTO notas VALUES(
    1, 'evaluación 2', 70, 0
);

INSERT INTO notas VALUES(
    2, 'evaluación 1', 63, 1
);

INSERT INTO notas VALUES(
    3, 'evaluación 2', 66, 1
);

INSERT INTO notas VALUES(
    4, 'evaluación 1', 70, 2
);

INSERT INTO notas VALUES(
    5, 'evaluación 2', 69, 2
);

INSERT INTO notas VALUES(
    6, 'evaluación 1', 67, 3
);

INSERT INTO notas VALUES(
    7, 'evaluación 2', 70, 3
);

INSERT INTO notas VALUES(
    8, 'evaluación 1', 63, 4
);

INSERT INTO notas VALUES(
    9, 'evaluación 2', 65, 4
);

INSERT INTO notas VALUES(
    10, 'evaluación 1', 61, 5
);

INSERT INTO notas VALUES(
    11, 'evaluación 2', 68, 5
);

INSERT INTO notas VALUES(
    12, 'evaluación 1', 59, 6
);

INSERT INTO notas VALUES(
    13, 'evaluación 2', 62, 6
);

INSERT INTO notas VALUES(
    14, 'evaluación 1', 70, 7
);

INSERT INTO notas VALUES(
    15, 'evaluación 2', 70, 7
);

INSERT INTO notas VALUES(
    16, 'evaluación 1', 41, 8
);

INSERT INTO notas VALUES(
    17, 'evaluación 2', 59, 8
);

INSERT INTO notas VALUES(
    18, 'evaluación 1', 58, 9
);

INSERT INTO notas VALUES(
    19, 'evaluación 2', 63, 9
);

INSERT INTO notas VALUES(
    20, 'evaluación 1', 10, 10
);

INSERT INTO notas VALUES(
    21, 'evaluación 2', 58, 10
);

INSERT INTO notas VALUES(
    22, 'evaluación 1', 55, 11
);

INSERT INTO notas VALUES(
    23, 'evaluación 2', 69, 11
);

INSERT INTO notas VALUES(
    24, 'evaluación 1', 47, 12
);

INSERT INTO notas VALUES(
    25, 'evaluación 2', 70, 12
);

INSERT INTO notas VALUES(
    26, 'evaluación 1', 39, 13
);

INSERT INTO notas VALUES(
    27, 'evaluación 2', 66, 13
);

INSERT INTO notas VALUES(
    28, 'evaluación 1', 28, 14
);

INSERT INTO notas VALUES(
    29, 'evaluación 2', 43, 14
);

-- Cree una consulta que muestre el promedio obtenido por un estudiante para una asignatura en específico, este debe ser redondeado, sin decimales.
SELECT alumno.rut_alumno AS "Rut alumno", ROUND(AVG(notas.nota_obtenida)) AS "Promedio redondeado" FROM notas INNER JOIN cursa_asignatura ON notas.fk_cursa_asignatura = cursa_asignatura.codigo_cursa_asignatura INNER JOIN alumno ON cursa_asignatura.fk_rut_alumno = alumno.rut_alumno INNER JOIN asignatura ON cursa_asignatura.fk_codigo_asignatura = asignatura.codigo_asignatura WHERE asignatura.codigo_asignatura = '2222' GROUP BY alumno.rut_alumno;

-- Cree una consulta que muestre la nota más baja obtenida en una asignatura específica.
SELECT alumno.nombre_alumno AS "Nombre alumno", MIN(notas.nota_obtenida) AS "Nota más baja" FROM notas INNER JOIN cursa_asignatura ON notas.fk_cursa_asignatura = cursa_asignatura.codigo_cursa_asignatura INNER JOIN alumno ON cursa_asignatura.fk_rut_alumno = alumno.rut_alumno INNER JOIN asignatura ON cursa_asignatura.fk_codigo_asignatura = asignatura.codigo_asignatura WHERE asignatura.codigo_asignatura = '2222' GROUP BY alumno.nombre_alumno;

-- Cree una consulta que muestre la cantidad de estudiantes que existen en la base de datos.
SELECT COUNT(rut_alumno) AS "Alumnos totales" FROM alumno;

-- Cree una consulta que muestre el nombre de los estudiantes concatenado con el promedio obtenido para una asignatura en específico.
SELECT alumno.nombre_alumno || ' ' || ROUND(AVG(notas.nota_obtenida)) AS "Nombre y promedio" FROM notas INNER JOIN cursa_asignatura ON notas.fk_cursa_asignatura = cursa_asignatura.codigo_cursa_asignatura INNER JOIN alumno ON cursa_asignatura.fk_rut_alumno = alumno.rut_alumno INNER JOIN asignatura ON cursa_asignatura.fk_codigo_asignatura = asignatura.codigo_asignatura WHERE asignatura.codigo_asignatura = '2222' GROUP BY alumno.nombre_alumno;

-- Cree una consulta que muestre el concatenado: el rut, nombre y teléfono de cada alumno existente en la base de datos.
SELECT rut_alumno || ' ' || nombre_alumno || ' ' || telefono_alumno AS "Estudiantes" FROM alumno;