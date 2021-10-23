-- Generado por Oracle SQL Developer Data Modeler 21.2.0.183.1957
--   en:        2021-10-05 13:47:48 CLST
--   sitio:      Oracle Database 21c
--   tipo:      Oracle Database 21c



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE area (
    codigo_area      INTEGER NOT NULL,
    nombre_area      VARCHAR2(30) NOT NULL,
    descripcion_area VARCHAR2(500) NOT NULL
);

ALTER TABLE area ADD CONSTRAINT area_pk PRIMARY KEY ( codigo_area );

CREATE TABLE boquilla (
    codigo_boquilla INTEGER NOT NULL,
    nombre_boquilla VARCHAR2(20),
    medida_boquilla VARCHAR2(20)
);

ALTER TABLE boquilla ADD CONSTRAINT boquilla_pk PRIMARY KEY ( codigo_boquilla );

CREATE TABLE ciudad (
    codigo_ciudad INTEGER NOT NULL,
    nombre_ciudad VARCHAR2(20)
);

ALTER TABLE ciudad ADD CONSTRAINT ciudad_pk PRIMARY KEY ( codigo_ciudad );

CREATE TABLE direccion (
    codigo_direccion    INTEGER NOT NULL,
    nombre_direccion    VARCHAR2(25),
    numero_direccion    VARCHAR2(10),
    codigo_postal       VARCHAR2(10),
    fk_codigo_proveedor INTEGER NOT NULL,
    fk_codigo_ciudad    INTEGER NOT NULL
);

ALTER TABLE direccion ADD CONSTRAINT direccion_pk PRIMARY KEY ( codigo_direccion );

CREATE TABLE impresora3d (
    codigo_impresora         INTEGER NOT NULL,
    fk_codigo_proveedor      INTEGER NOT NULL,
    fk_codigo_tipo_impresora INTEGER NOT NULL,
    nombre_impresora         VARCHAR2(30),
    version_impresora        VARCHAR2(10),
    velocidad_impresion      VARCHAR2(20),
    area_impresion           VARCHAR2(50)
);

ALTER TABLE impresora3d ADD CONSTRAINT "Impresora 3D_PK" PRIMARY KEY ( codigo_impresora );

CREATE TABLE impresoraboquilla (
    fk_codigo_impresora INTEGER NOT NULL,
    fk_codigo_boquilla  INTEGER NOT NULL
);

CREATE TABLE impresoramateriales (
    fk_codigo_impresora INTEGER NOT NULL,
    fk_codigo_material  INTEGER NOT NULL
);

CREATE TABLE impresoramodelo (
    fk_codigo_impresora INTEGER NOT NULL,
    fk_codigo_modelo    INTEGER NOT NULL
);

CREATE TABLE marca (
    codigo_marca INTEGER NOT NULL,
    nombre_marca VARCHAR2(30) NOT NULL
);

ALTER TABLE marca ADD CONSTRAINT marca_pk PRIMARY KEY ( codigo_marca );

CREATE TABLE materiales (
    codigo_material          INTEGER NOT NULL,
    nombre_material          VARCHAR2(20) NOT NULL,
    color_material           VARCHAR2(20) NOT NULL,
    diametro_material        VARCHAR2(20) NOT NULL,
    longitud_material        VARCHAR2(20) NOT NULL,
    deflexion_de_color       VARCHAR2(50) NOT NULL,
    temperatura_de_impresion VARCHAR2(20) NOT NULL,
    deformacion              VARCHAR2(50) NOT NULL,
    composicion              VARCHAR2(100) NOT NULL,
    tolerancia               VARCHAR2(50) NOT NULL,
    resistencia_traccion     VARCHAR2(50) NOT NULL,
    resistencia_al_impacto   VARCHAR2(50) NOT NULL,
    durabilidad              VARCHAR2(50) NOT NULL,
    flexibilidad             VARCHAR2(50) NOT NULL,
    resistencia_a_corrosion  VARCHAR2(50) NOT NULL,
    fk_codigo_marca          INTEGER NOT NULL,
    fk_codigo_tipo_material  INTEGER NOT NULL
);

ALTER TABLE materiales ADD CONSTRAINT materiales_pk PRIMARY KEY ( codigo_material );

CREATE TABLE modeloarea (
    fk_codigo_area   INTEGER NOT NULL,
    fk_codigo_modelo INTEGER NOT NULL
);

CREATE TABLE modelos3d (
    codigo_modelo      INTEGER NOT NULL,
    nombre_modelo      VARCHAR2(20) NOT NULL,
    utilidad_modelo    VARCHAR2(200) NOT NULL,
    tamaño_modelo      VARCHAR2(20) NOT NULL,
    relleno_porcentaje VARCHAR2(50) NOT NULL,
    color_modelo       VARCHAR2(20) NOT NULL,
    numeros_capas      VARCHAR2(50) NOT NULL,
    recurso_adjunto    VARCHAR2(100) NOT NULL
);

ALTER TABLE modelos3d ADD CONSTRAINT modelos3d_pk PRIMARY KEY ( codigo_modelo );

CREATE TABLE modelosmateriales (
    fk_codigo_modelo   INTEGER NOT NULL,
    fk_codigo_material INTEGER NOT NULL
);

CREATE TABLE proveedor (
    codigo_proveedor    INTEGER NOT NULL,
    nombre_proveedor    VARCHAR2(20),
    telefono_proveedor  VARCHAR2(10),
    email_proveedor     VARCHAR2(20),
    paginaweb_proveedor VARCHAR2(50)
);

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( codigo_proveedor );

CREATE TABLE tipoimpresora (
    codigo_tipo_impresora      INTEGER NOT NULL,
    nombre_tipo_impresora      VARCHAR2(20),
    descripcion_tipo_impresora VARCHAR2(500),
    detalle_funcionamiento     VARCHAR2(500),
    calidad_impresion          VARCHAR2(50)
);

ALTER TABLE tipoimpresora ADD CONSTRAINT tipoimpresora_pk PRIMARY KEY ( codigo_tipo_impresora );

CREATE TABLE tipomaterial (
    codigo_tipo_material      INTEGER NOT NULL,
    nombre_tipo_material      VARCHAR2(20) NOT NULL,
    descripcion_tipo_material VARCHAR2(500) NOT NULL,
    composicion_tipo_material VARCHAR2(200) NOT NULL,
    velocidad_tipo_material   VARCHAR2(25) NOT NULL
);

ALTER TABLE tipomaterial ADD CONSTRAINT tipomaterial_pk PRIMARY KEY ( codigo_tipo_material );

ALTER TABLE direccion
    ADD CONSTRAINT direccion_ciudad_fk FOREIGN KEY ( fk_codigo_ciudad )
        REFERENCES ciudad ( codigo_ciudad );

ALTER TABLE direccion
    ADD CONSTRAINT direccion_proveedor_fk FOREIGN KEY ( fk_codigo_proveedor )
        REFERENCES proveedor ( codigo_proveedor );

ALTER TABLE impresoraboquilla
    ADD CONSTRAINT impresora_boquilla_fk FOREIGN KEY ( fk_codigo_boquilla )
        REFERENCES boquilla ( codigo_boquilla );

ALTER TABLE impresoramateriales
    ADD CONSTRAINT impresora_impresora3d_fk FOREIGN KEY ( fk_codigo_impresora )
        REFERENCES impresora3d ( codigo_impresora );

ALTER TABLE impresoramateriales
    ADD CONSTRAINT impresora_materiales_fk FOREIGN KEY ( fk_codigo_material )
        REFERENCES materiales ( codigo_material );

ALTER TABLE impresora3d
    ADD CONSTRAINT impresora3d_proveedor_fk FOREIGN KEY ( fk_codigo_proveedor )
        REFERENCES proveedor ( codigo_proveedor );

ALTER TABLE impresora3d
    ADD CONSTRAINT impresora3d_tipoimpresora_fk FOREIGN KEY ( fk_codigo_tipo_impresora )
        REFERENCES tipoimpresora ( codigo_tipo_impresora );

ALTER TABLE impresoraboquilla
    ADD CONSTRAINT impresoraimpresora3d_fk FOREIGN KEY ( fk_codigo_impresora )
        REFERENCES impresora3d ( codigo_impresora );

ALTER TABLE materiales
    ADD CONSTRAINT materiales_marca_fk FOREIGN KEY ( fk_codigo_marca )
        REFERENCES marca ( codigo_marca );

ALTER TABLE materiales
    ADD CONSTRAINT materiales_tipomaterial_fk FOREIGN KEY ( fk_codigo_tipo_material )
        REFERENCES tipomaterial ( codigo_tipo_material );

ALTER TABLE impresoramodelo
    ADD CONSTRAINT "Modela_Impresora 3D_FK" FOREIGN KEY ( fk_codigo_impresora )
        REFERENCES impresora3d ( codigo_impresora );

ALTER TABLE impresoramodelo
    ADD CONSTRAINT "Modela_Modelos/Diseños_FK" FOREIGN KEY ( fk_codigo_modelo )
        REFERENCES modelos3d ( codigo_modelo );

ALTER TABLE modeloarea
    ADD CONSTRAINT modeloarea_area_fk FOREIGN KEY ( fk_codigo_area )
        REFERENCES area ( codigo_area );

ALTER TABLE modeloarea
    ADD CONSTRAINT modeloarea_modelos3d_fk FOREIGN KEY ( fk_codigo_modelo )
        REFERENCES modelos3d ( codigo_modelo );

ALTER TABLE modelosmateriales
    ADD CONSTRAINT modelos_materiales_fk FOREIGN KEY ( fk_codigo_material )
        REFERENCES materiales ( codigo_material );

ALTER TABLE modelosmateriales
    ADD CONSTRAINT modelos_modelos3d_fk FOREIGN KEY ( fk_codigo_modelo )
        REFERENCES modelos3d ( codigo_modelo );



-- Informe de Resumen de Oracle SQL Developer Data Modeler: 
-- 
-- CREATE TABLE                            16
-- CREATE INDEX                             0
-- ALTER TABLE                             27
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
