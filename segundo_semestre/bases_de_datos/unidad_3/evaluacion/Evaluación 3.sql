-- Creación de la estructura de tablas
CREATE TABLE animal (
    codigo_animal          INTEGER NOT NULL,
    alias_animal           VARCHAR2(50) NOT NULL,
    nombre_animal          VARCHAR2(50) NOT NULL,
    especie_animal         VARCHAR2(50) NOT NULL,
    fecha_ingreso_animal   DATE NOT NULL,
    peso_animal            INTEGER NOT NULL,
    porcion_alimento_kilos FLOAT NOT NULL,
    fk_codigo_zoo          CHAR(6) NOT NULL
);

ALTER TABLE animal ADD CONSTRAINT animal_pk PRIMARY KEY ( codigo_animal );

CREATE TABLE zoo (
    codigo_zoo           CHAR(6) NOT NULL,
    nombre_zoo           VARCHAR2(150) NOT NULL,
    descripcion_zoo      VARCHAR2(500) NOT NULL,
    metros_cuadrados_zoo INTEGER NOT NULL
);

ALTER TABLE zoo ADD CONSTRAINT zoo_pk PRIMARY KEY ( codigo_zoo );

ALTER TABLE animal
    ADD CONSTRAINT animal_zoo_fk FOREIGN KEY ( fk_codigo_zoo )
        REFERENCES zoo ( codigo_zoo );

-- Insertar datos
INSERT INTO zoo VALUES(
    '1', 'Zoológico Miraflores', 'El parque zoológico Miraflores es un zoológico, ubicado en la comuna de Buin, Región Metropolitana de Chile, este contiene un parque y pronto un Acuario.', 40000
);

INSERT INTO zoo VALUES(
    '2', 'Zoológico San Bernardo', 'El parque Zoológico San Bernardo es un zoológico ubicado en la comuna San Bernardo, Chile, partió como una iniciativa personal como amantes de los animales', 100000
);

INSERT INTO animal VALUES(
    1, 'Juan', 'Leon', 'Panthera', TO_DATE('05-24-2019', 'mm-dd-yyyy'), 120, 4, '1'
);

INSERT INTO animal VALUES(
    2, 'Williams', 'Mamut', 'Mammuthus', TO_DATE('07-18-2020', 'mm-dd-yyyy'), 1000, 50, '1'
);

INSERT INTO animal VALUES(
    3, 'Cristina', 'Elefante', 'Loxodonta', TO_DATE('02-22-2020', 'mm-dd-yyyy'), 1000, 50, '1'
);

INSERT INTO animal VALUES(
    4, 'Brenda', 'Ornitorrinco', 'Ornithorhynchus', TO_DATE('05-12-2020', 'mm-dd-yyyy'), 20, 4, '1'
);

INSERT INTO animal VALUES(
    5, 'Jose', 'Panda', 'Ailuropoda', TO_DATE('02-17-2018', 'mm-dd-yyyy'), 60, 3, '1'
);

INSERT INTO animal VALUES(
    6, 'Ion', 'Flamenco', 'Phoenicopterus', TO_DATE('06-16-2018', 'mm-dd-yyyy'), 45, 5, '1'
);

INSERT INTO animal VALUES(
    7, 'Gabriel', 'Cocodrilo', 'Crocodilia', TO_DATE('02-23-2018', 'mm-dd-yyyy'), 80, 20, '1'
);

INSERT INTO animal VALUES(
    8, 'Emilia', 'Burro', 'Equus', TO_DATE('05-09-2019', 'mm-dd-yyyy'), 120, 40, '1'
);

INSERT INTO animal VALUES(
    9, 'Mauris', 'Mono', 'Cercopithecus', TO_DATE('07-17-2020', 'mm-dd-yyyy'), 45, 15, '1'
);

INSERT INTO animal VALUES(
    10, 'Ibai', 'Serpiente', 'Morelia', TO_DATE('04-09-2020', 'mm-dd-yyyy'), 8, 1, '1'
);

INSERT INTO animal VALUES(
    11, 'Daniel', 'Hipopótamo', 'Hippopotamus', TO_DATE('10-10-2020', 'mm-dd-yyyy'), 200, 45, '2'
);

INSERT INTO animal VALUES(
    12, 'Belen', 'Rana', 'Limnonectes', TO_DATE('11-11-2021', 'mm-dd-yyyy'), 4, 1, '2'
);

INSERT INTO animal VALUES(
    13, 'Aziz', 'Canguro', 'Macropus', TO_DATE('12-12-2020', 'mm-dd-yyyy'), 90, 20, '2'
);

INSERT INTO animal VALUES(
    14, 'Arsenio', 'Ave', 'Malurus', TO_DATE('03-20-2019', 'mm-dd-yyyy'), 20, 5, '2'
);

INSERT INTO animal VALUES(
    15, 'Marwa', 'Perro', 'Canis', TO_DATE('03-05-2021', 'mm-dd-yyyy'), 15, 4, '2'
);

INSERT INTO animal VALUES(
    16, 'Albert', 'Conejo', 'Oryctolagus', TO_DATE('10-29-2021', 'mm-dd-yyyy'), 5, 1, '2'
);

INSERT INTO animal VALUES(
    17, 'Paul', 'Cabra', 'Capra', TO_DATE('09-23-2019', 'mm-dd-yyyy'), 75, 10, '2'
);

INSERT INTO animal VALUES(
    18, 'Esther', 'Vaca', 'Bos', TO_DATE('10-31-2021', 'mm-dd-yyyy'), 120, 40, '2'
);

INSERT INTO animal VALUES(
    19, 'Lina', 'Pato', 'Amazonetta', TO_DATE('10-18-2019', 'mm-dd-yyyy'), 15, 5, '2'
);

INSERT INTO animal VALUES(
    20, 'Gonzalo', 'Cerdo', 'Sus', TO_DATE('01-11-2021', 'mm-dd-yyyy'), 80, 15, '2'
);

-- Consultas
-- 1. Cree una consulta que muestre el nombre de todos los animales existentes en un zoológico en específico, el nombre de los animales debe estar en mayúsculas.
SELECT UPPER(nombre_animal) AS "Nombre animal" FROM animal WHERE fk_codigo_zoo = '2';

-- 2. Cree una consulta que muestre el alias, nombre y especie de todos los animales concatenados.
SELECT alias_animal || ' - ' || nombre_animal  || ' - ' || especie_animal AS "Alias - Nombre - Especie" FROM animal;

-- 3. Cree una consulta que muestre el nombre del zoológico acompañado de especies que tienen en sus instalaciones, deben agruparlas para evitar datos repetidos.
SELECT zoo.nombre_zoo AS "Zoológico", animal.especie_animal AS "Animales" FROM zoo INNER JOIN animal ON animal.fk_codigo_zoo = zoo.codigo_zoo GROUP BY zoo.nombre_zoo, animal.especie_animal ORDER BY zoo.nombre_zoo;

-- 4. Cree una consulta que muestre el nombre del zoológico acompañado del nombre de las especies y que también muestre la cantidad de especies que tiene el zoológico.
SELECT zoo.nombre_zoo AS "Zoológico", animal.especie_animal AS "Especies", COUNT(animal.especie_animal) AS "Cantidad de especies" FROM zoo INNER JOIN animal ON animal.fk_codigo_zoo = zoo.codigo_zoo GROUP BY zoo.nombre_zoo, animal.especie_animal ORDER BY zoo.nombre_zoo;

-- 5. Cree una consulta que muestre el nombre del zoológico concatenado con la cantidad de metros cuadrados que tiene.
SELECT nombre_zoo || ' - ' || metros_cuadrados_zoo as "Zoológico - metros cuadrados" FROM zoo;

-- 6. Cree una consulta que muestre el nombre de los animales concatenado al año que ingresó al zoológico, (solo el año).
SELECT nombre_animal || ' - ' || TO_CHAR(fecha_ingreso_animal, 'yyyy') AS "Animal - Año de ingreso" FROM animal;

-- 7. Cree una consulta que muestre el nombre del zoológico, y la suma de los kilos de comida de alimentos que debe generar por día.
SELECT zoo.nombre_zoo AS "Nombre zoológico", SUM(animal.porcion_alimento_kilos) AS "Alimento necesario diariamente (Kg)" FROM zoo INNER JOIN animal ON zoo.codigo_zoo = animal.fk_codigo_zoo GROUP BY zoo.nombre_zoo;

-- 8. Cree una consulta que muestre el alias, el nombre y la especie del animal que tenga el mayor peso.
SELECT alias_animal AS "Alias", nombre_animal AS "Nombre", especie_animal AS "Especie" FROM animal WHERE peso_animal = (SELECT MAX(peso_animal) FROM animal);