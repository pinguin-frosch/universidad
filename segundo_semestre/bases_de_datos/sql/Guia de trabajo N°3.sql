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
    '21.019.385-5', 'Gabriel Barrientos', TO_DATE('14-01-2003', 'dd-mm-yyyy'), '66842427'
);

INSERT INTO alumno VALUES(
    '', '', TO_DATE('', 'dd-mm-yyyy'), ''
);

INSERT INTO alumno VALUES(
    '', '', TO_DATE('', 'dd-mm-yyyy'), ''
);

INSERT INTO alumno VALUES(
    '', '', TO_DATE('', 'dd-mm-yyyy'), ''
);

INSERT INTO alumno VALUES(
    '', '', TO_DATE('', 'dd-mm-yyyy'), ''
);

-- Insertar asignaturas(código, nombre, descripción)

INSERT INTO asignatura VALUES(
    '0000', 'bases de datos', 'permite desarrollar la habilidad de interactuar con bases de datos mediante consultas avanzadas'
);

INSERT INTO asignatura VALUES(
    '', '', ''
);

-- Insertar cursa_asignatura(codigo_cursa_asignatura, fk_rut_alumno, fk_codigo_asignatura, fecha_inicio, fecha_fin)

INSERT INTO cursa_asignatura VALUES(
    0, '21.019.385-5', '0000', TO_DATE('23-08-2021', 'dd-mm-yyyy'), TO_DATE('30-11-2021', 'dd-mm-yyyy')
);

INSERT INTO cursa_asignatura VALUES(
    , '', '', TO_DATE('', ''), TO_DATE('', '')
);

INSERT INTO cursa_asignatura VALUES(
    , '', '', TO_DATE('', ''), TO_DATE('', '')
);

INSERT INTO cursa_asignatura VALUES(
    , '', '', TO_DATE('', ''), TO_DATE('', '')
);

INSERT INTO cursa_asignatura VALUES(
    , '', '', TO_DATE('', ''), TO_DATE('', '')
);

-- Insertas notas(codigo_nota, descripción, nota_obtenida, fk_cursa_asignatura)

INSERT INTO notas VALUES(
    0, 'primera evaluación', 6.8, 0
);

INSERT INTO notas VALUES(
    , '', , 
);

INSERT INTO notas VALUES(
    , '', , 
);

INSERT INTO notas VALUES(
    , '', , 
);

INSERT INTO notas VALUES(
    , '', , 
);